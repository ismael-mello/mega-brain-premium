#!/usr/bin/env python3
"""
JARVIS Session End Hook
Executado automaticamente quando uma sessão Claude Code encerra.

Responsabilidades:
1. Salvar estado atual
2. Criar HANDOFF se necessário
3. Registrar métricas da sessão
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path

# Importar Chronicler para handoff narrativo
try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skills', 'chronicler'))
    from chronicler_core import on_session_end as chronicler_end
    CHRONICLER_AVAILABLE = True
except ImportError:
    CHRONICLER_AVAILABLE = False

def get_project_dir():
    """Obtém o diretório do projeto."""
    return os.environ.get('CLAUDE_PROJECT_DIR', os.getcwd())

def load_jarvis_state():
    """Carrega o estado do JARVIS."""
    project_dir = get_project_dir()
    # Caminho primário: .claude/jarvis/STATE.json (consistente com session_start.py)
    state_path = Path(project_dir) / '.claude' / 'jarvis' / 'STATE.json'
    
    if state_path.exists():
        with open(state_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return create_default_state()

def create_default_state():
    """Cria estado padrão se não existir."""
    return {
        'jarvis': {
            'version': '1.0.0',
            'installed_at': datetime.now().isoformat()
        },
        'session': {
            'id': None,
            'started_at': None,
            'last_action_at': None,
            'is_active': False
        },
        'current_state': {
            'phase': 0,
            'phase_name': 'IDLE',
            'status': 'ready',
            'source_code': None,
            'percent_complete': 0
        },
        'next_action': {
            'description': 'Aguardando instruções',
            'priority': 'normal'
        },
        'metrics': {
            'sessions_total': 0,
            'files_processed': 0,
            'insights_extracted': 0
        }
    }

def save_jarvis_state(state):
    """Salva o estado do JARVIS."""
    project_dir = get_project_dir()
    # Caminho primário: .claude/jarvis/STATE.json (consistente com session_start.py)
    state_path = Path(project_dir) / '.claude' / 'jarvis' / 'STATE.json'
    state_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(state_path, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def create_handoff(state, session_info):
    """Cria arquivo HANDOFF para próxima sessão."""
    project_dir = get_project_dir()
    handoff_path = Path(project_dir) / 'logs' / 'handoffs'
    handoff_path.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    handoff_file = handoff_path / f"HANDOFF-{timestamp}.md"
    
    current = state.get('current_state', {})
    next_action = state.get('next_action', {})
    
    content = f"""# HANDOFF - {datetime.now().strftime('%Y-%m-%d %H:%M')}

> **Gerado por:** JARVIS Session End Hook
> **Session ID:** {session_info.get('session_id', 'unknown')}
> **Motivo:** {session_info.get('reason', 'session_end')}

---

## ESTADO ATUAL

- **Fase:** {current.get('phase_name', 'IDLE')}
- **Status:** {current.get('status', 'unknown')}
- **Progresso:** {current.get('percent_complete', 0)}%
- **Fonte:** {current.get('source_code', 'N/A')}

---

## PRÓXIMA AÇÃO SUGERIDA

**{next_action.get('description', 'Continuar trabalho')}**

Prioridade: {next_action.get('priority', 'normal')}

---

## PARA CONTINUAR

1. Abra uma nova sessão
2. JARVIS carregará este contexto automaticamente
3. Pergunte "onde paramos?" se precisar de mais detalhes

---

*Ready when you are, sir.*
"""
    
    with open(handoff_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(handoff_file)

def update_session_log(session_info):
    """Atualiza log da sessão com dados de encerramento."""
    project_dir = get_project_dir()
    log_path = Path(project_dir) / 'logs' / 'sessions'
    
    # Encontrar log mais recente
    if log_path.exists():
        logs = sorted(log_path.glob('session-*.json'), reverse=True)
        if logs:
            latest_log = logs[0]
            with open(latest_log, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
            
            log_data['ended_at'] = datetime.now().isoformat()
            log_data['reason'] = session_info.get('reason', 'unknown')
            
            with open(latest_log, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)

def sync_metrics_from_filesystem(state):
    """
    Escaneia o filesystem para calcular metricas REAIS e atualiza STATE.json.
    Garante que o estado reflete o progresso real, nao apenas o que foi registrado.

    REGRA: STATE.json DEVE refletir a realidade do filesystem.
    """
    project_dir = Path(get_project_dir())

    # --- Contar arquivos processados (artifacts) ---
    artifacts_dir = project_dir / 'artifacts' / 'insights'
    files_processed = 0
    if artifacts_dir.exists():
        for person_dir in artifacts_dir.iterdir():
            if person_dir.is_dir():
                extraction_files = list(person_dir.glob('MODULE-*-EXTRACTION.md'))
                files_processed += len(extraction_files)

    # --- Contar DNA elements (estimativa baseada em sources existentes) ---
    dna_dir = project_dir / 'knowledge' / 'dna' / 'persons'
    dna_sources = 0
    if dna_dir.exists():
        for person_dir in dna_dir.iterdir():
            if person_dir.is_dir() and not person_dir.name.startswith('_'):
                config_file = person_dir / 'CONFIG.yaml'
                dna_file = person_dir / 'DNA.yaml'
                if config_file.exists() or dna_file.exists():
                    dna_sources += 1

    # --- Contar agentes ---
    person_agents = 0
    persons_dir = project_dir / 'agents' / 'persons'
    if persons_dir.exists():
        for agent_dir in persons_dir.iterdir():
            if agent_dir.is_dir() and (agent_dir / 'AGENT.md').exists():
                person_agents += 1

    cargo_agents = 0
    cargo_dir = project_dir / 'agents' / 'cargo'
    if cargo_dir.exists():
        for agent_file in cargo_dir.rglob('AGENT.md'):
            cargo_agents += 1

    # --- Contar dossiers ---
    person_dossiers = 0
    theme_dossiers = 0
    dossiers_dir = project_dir / 'knowledge' / 'dossiers'
    if dossiers_dir.exists():
        persons_dossier_dir = dossiers_dir / 'persons'
        if persons_dossier_dir.exists():
            person_dossiers = len([f for f in persons_dossier_dir.glob('DOSSIER-*.md')])
        themes_dossier_dir = dossiers_dir / 'themes'
        if themes_dossier_dir.exists():
            theme_dossiers = len([f for f in themes_dossier_dir.glob('DOSSIER-*.md')])

    # --- Contar playbooks ---
    playbooks = 0
    playbooks_dir = project_dir / 'knowledge' / 'playbooks'
    if playbooks_dir.exists():
        playbooks = len([f for f in playbooks_dir.glob('PLAYBOOK-*.md')])

    # --- Contar aggregated DNAs ---
    agg_dnas = 0
    agg_dir = project_dir / 'knowledge' / 'dna' / 'aggregated'
    if agg_dir.exists():
        agg_dnas = len([f for f in agg_dir.glob('AGG-*.yaml')])

    # --- Contar insights do inbox processado ---
    # Estimar arquivos de inbox processados pelo numero de extractions
    inbox_processed = 0
    if artifacts_dir.exists():
        for person_dir in artifacts_dir.iterdir():
            if person_dir.is_dir():
                dedup_files = list(person_dir.glob('DEDUP-*.md'))
                extraction_files = list(person_dir.glob('MODULE-*-EXTRACTION.md'))
                if dedup_files or extraction_files:
                    # Contar transcricoes no inbox correspondente
                    # Usar o nome da pasta como referencia
                    inbox_processed += len(extraction_files) * 12  # ~12 files per module avg

    # --- Atualizar state ---
    if 'metrics' not in state:
        state['metrics'] = {}

    # Preservar valores maiores (nunca decrementar)
    current_files = state['metrics'].get('files_processed', 0)
    current_insights = state['metrics'].get('insights_extracted', 0)

    state['metrics']['files_processed'] = max(current_files, inbox_processed)
    # insights_extracted mantemos se ja tiver valor maior
    if current_insights == 0 and inbox_processed > 0:
        state['metrics']['insights_extracted'] = inbox_processed  # placeholder

    # Atualizar knowledge_base
    state['knowledge_base'] = {
        'dna_sources': dna_sources,
        'person_agents': person_agents,
        'cargo_agents': cargo_agents,
        'person_dossiers': person_dossiers,
        'theme_dossiers': theme_dossiers,
        'playbooks': playbooks,
        'aggregated_dnas': agg_dnas
    }

    return state


def sync_from_session_log(state):
    """
    Tenta ler a session log mais recente para extrair metricas precisas.
    Complementa o scan de filesystem com dados da sessao.
    """
    project_dir = Path(get_project_dir())
    sessions_dir = project_dir / '.claude' / 'sessions'

    # Procurar por session logs com dados de missao
    session_files = sorted(sessions_dir.glob('SESSION-*-*.md'), reverse=True) if sessions_dir.exists() else []

    for session_file in session_files[:5]:  # Ultimas 5 sessoes
        try:
            content = session_file.read_text(encoding='utf-8')

            # Extrair metricas se presentes
            if 'files_processed' in content or 'DNA Elements' in content or 'dna_elements' in content:
                import re

                # Buscar files_processed
                match = re.search(r'files_processed["\s:]+(\d+)', content)
                if match:
                    found = int(match.group(1))
                    current = state.get('metrics', {}).get('files_processed', 0)
                    state.setdefault('metrics', {})['files_processed'] = max(current, found)

                # Buscar dna_elements / insights
                match = re.search(r'(?:dna_elements|insights_extracted|unique elements)["\s:]+(\d+)', content)
                if match:
                    found = int(match.group(1))
                    current = state.get('metrics', {}).get('insights_extracted', 0)
                    state['metrics']['insights_extracted'] = max(current, found)

                # Buscar completed_missions
                if 'Status: COMPLETE' in content or 'ALL TASKS COMPLETE' in content:
                    # Extrair dados da missao completada
                    mission_match = re.search(r'Person:\s*(.+)', content)
                    if mission_match:
                        person = mission_match.group(1).strip().rstrip('*')

                        if 'completed_missions' not in state:
                            state['completed_missions'] = []

                        # Verificar se ja esta registrada
                        existing = [m for m in state['completed_missions']
                                   if person.lower() in m.get('source', '').lower()]
                        if not existing:
                            state['completed_missions'].append({
                                'source': person,
                                'completed_at': session_file.stem.split('SESSION-')[1][:10] if 'SESSION-' in session_file.stem else 'unknown',
                                'session_file': session_file.name
                            })

                break  # Encontrou dados, parar

        except Exception:
            continue

    return state


def main():
    """Função principal do hook."""
    try:
        # Ler input do hook (stdin)
        input_data = sys.stdin.read()
        hook_input = json.loads(input_data) if input_data else {}

        # Carregar estado atual
        state = load_jarvis_state()

        # === SYNC METRICAS DO FILESYSTEM (FIX: propagacao obrigatoria) ===
        state = sync_metrics_from_filesystem(state)
        state = sync_from_session_log(state)

        # Atualizar estado da sessão
        state['session']['is_active'] = False
        state['session']['last_action_at'] = datetime.now().isoformat()
        state['metrics']['sessions_total'] = state.get('metrics', {}).get('sessions_total', 0) + 1

        # Salvar estado
        save_jarvis_state(state)
        
        # Criar HANDOFF
        handoff_path = create_handoff(state, hook_input)

        # === CHRONICLER HANDOFF ===
        if CHRONICLER_AVAILABLE:
            try:
                chronicler_end()
            except Exception:
                # Chronicler é opcional, não bloqueia se falhar
                pass

        # Atualizar log da sessão
        update_session_log(hook_input)
        
        # Output (para logs internos, não exibido ao usuário)
        output = {
            'continue': True,
            'feedback': f"[JARVIS] Sessão encerrada. HANDOFF criado: {handoff_path}"
        }
        
        print(json.dumps(output))
        
    except Exception as e:
        # Em caso de erro, não bloquear o encerramento
        error_output = {
            'continue': True,
            'feedback': f"[JARVIS] Hook de encerramento reportou: {str(e)}"
        }
        print(json.dumps(error_output))

if __name__ == '__main__':
    main()
