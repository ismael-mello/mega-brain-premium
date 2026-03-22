#!/usr/bin/env python3
"""
TEAM CREATION TRIGGER v1.0
============================
Monitors AGG (aggregated DNA) files and auto-creates cargo agent teams
when a domain accumulates enough knowledge (frameworks, heuristics, etc.).

Pipeline: AGG-*.yaml → Threshold check → Team scaffolding → Agent creation

When an AGG reaches MIN_ELEMENTS_THRESHOLD, the system auto-scaffolds
a team of cargo agents specialized in that domain.

Version: 1.0.0
Date: 2026-03-22
"""

import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# PATHS
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

try:
    sys.path.insert(0, str(BASE_DIR))
    from core.paths import AGENTS_CARGO, KNOWLEDGE_EXTERNAL, LOGS
except ImportError:
    AGENTS_CARGO = BASE_DIR / "agents" / "cargo"
    KNOWLEDGE_EXTERNAL = BASE_DIR / "knowledge" / "external"
    LOGS = BASE_DIR / "logs"

AGG_DIR = KNOWLEDGE_EXTERNAL / "dna" / "aggregated"
TEAM_STATE_PATH = BASE_DIR / ".claude" / "mission-control" / "TEAM-CREATION-STATE.json"
TEAM_LOG = LOGS / "team-creation.jsonl"

# ---------------------------------------------------------------------------
# THRESHOLDS
# ---------------------------------------------------------------------------
MIN_ELEMENTS_THRESHOLD = 50  # Minimum DNA elements to trigger team creation
MIN_SOURCES_THRESHOLD = 2    # Minimum expert sources contributing

# ---------------------------------------------------------------------------
# DOMAIN → TEAM TEMPLATES
# ---------------------------------------------------------------------------
# Each domain maps to a team of roles that should exist when knowledge is sufficient.
# "roles" = list of (role_slug, role_name, archetype, tagline, nivel)

TEAM_TEMPLATES: dict[str, dict] = {
    "vendas": {
        "team_name": "Equipe de Vendas",
        "icon": "💰",
        "roles": [
            ("closer", "Closer", "SALES", "Fecha negócios usando métodos dos experts", "sales"),
            ("sdr", "SDR", "SALES", "Prospecção e qualificação de leads", "sales"),
            ("sales-manager", "Sales Manager", "SALES", "Gestão de equipe e pipeline", "sales"),
            ("cro", "CRO", "C-LEVEL", "Revenue strategy e unit economics", "c-level"),
        ],
    },
    "traffic": {
        "team_name": "Equipe de Tráfego Pago",
        "icon": "🎯",
        "roles": [
            ("media-buyer", "Media Buyer", "MARKETING", "Opera campanhas e distribui orçamento", "marketing"),
            ("paid-media-specialist", "Paid Media Specialist", "MARKETING", "Criativos, testes A/B, otimização", "marketing"),
            ("cmo", "CMO", "C-LEVEL", "Estratégia de marketing e posicionamento", "c-level"),
        ],
    },
    "copywriting": {
        "team_name": "Equipe de Copywriting",
        "icon": "✍️",
        "roles": [
            ("copywriter", "Copywriter", "MARKETING", "Escreve copy que converte", "marketing"),
            ("cmo", "CMO", "C-LEVEL", "Estratégia de comunicação e brand voice", "c-level"),
        ],
    },
    "offers": {
        "team_name": "Equipe de Ofertas",
        "icon": "🎁",
        "roles": [
            ("cro", "CRO", "C-LEVEL", "Engenharia de ofertas e pricing", "c-level"),
            ("cmo", "CMO", "C-LEVEL", "Posicionamento e value stack", "c-level"),
            ("closer", "Closer", "SALES", "Pitch e apresentação de ofertas", "sales"),
        ],
    },
    "outbound": {
        "team_name": "Equipe de Outbound",
        "icon": "📞",
        "roles": [
            ("sdr", "SDR", "SALES", "Cold outreach e cadências", "sales"),
            ("sales-manager", "Sales Manager", "SALES", "Gestão de pipeline outbound", "sales"),
            ("cro", "CRO", "C-LEVEL", "Estratégia de aquisição outbound", "c-level"),
        ],
    },
    "storytelling": {
        "team_name": "Equipe de Storytelling",
        "icon": "📖",
        "roles": [
            ("copywriter", "Copywriter", "MARKETING", "Narrativas que vendem", "marketing"),
            ("cmo", "CMO", "C-LEVEL", "Brand storytelling e posicionamento", "c-level"),
        ],
    },
    "brand-strategy": {
        "team_name": "Equipe de Brand Strategy",
        "icon": "🏛️",
        "roles": [
            ("cmo", "CMO", "C-LEVEL", "Estratégia de marca e identidade", "c-level"),
        ],
    },
    "executive-leadership": {
        "team_name": "Equipe Executiva",
        "icon": "👔",
        "roles": [
            ("cro", "CRO", "C-LEVEL", "Revenue e growth strategy", "c-level"),
            ("cfo", "CFO", "C-LEVEL", "Financial strategy e cash flow", "c-level"),
            ("cmo", "CMO", "C-LEVEL", "Marketing strategy", "c-level"),
            ("coo", "COO", "C-LEVEL", "Operações e processos", "c-level"),
        ],
    },
    "gestao-financeira": {
        "team_name": "Equipe Financeira",
        "icon": "💵",
        "roles": [
            ("cfo", "CFO", "C-LEVEL", "Gestão financeira e unit economics", "c-level"),
        ],
    },
    "movement": {
        "team_name": "Equipe de Movement Building",
        "icon": "🌊",
        "roles": [
            ("cmo", "CMO", "C-LEVEL", "Community building e brand movement", "c-level"),
        ],
    },
    "data-growth": {
        "team_name": "Equipe de Data & Growth",
        "icon": "📊",
        "roles": [
            ("cro", "CRO", "C-LEVEL", "Growth metrics e analytics", "c-level"),
            ("cmo", "CMO", "C-LEVEL", "Marketing analytics e attribution", "c-level"),
        ],
    },
    "money-models": {
        "team_name": "Equipe de Revenue Models",
        "icon": "🏗️",
        "roles": [
            ("cfo", "CFO", "C-LEVEL", "Modelagem financeira e pricing", "c-level"),
            ("cro", "CRO", "C-LEVEL", "Revenue architecture", "c-level"),
        ],
    },
    "lideranca": {
        "team_name": "Equipe de Liderança",
        "icon": "🎖️",
        "roles": [
            ("coo", "COO", "C-LEVEL", "Liderança operacional", "c-level"),
        ],
    },
    "design": {
        "team_name": "Equipe de Design",
        "icon": "🎨",
        "roles": [
            ("cmo", "CMO", "C-LEVEL", "Design strategy e brand", "c-level"),
        ],
    },
}

# ---------------------------------------------------------------------------
# AGG SCANNER
# ---------------------------------------------------------------------------


def scan_agg_files() -> list[dict]:
    """Scan all AGG-*.yaml files and extract domain stats."""
    agg_stats = []
    if not AGG_DIR.exists():
        return agg_stats

    for agg_file in sorted(AGG_DIR.glob("AGG-*.yaml")):
        try:
            content = agg_file.read_text(encoding="utf-8")
            data = yaml.safe_load(content)
            if not data:
                continue

            domain = data.get("dominio", agg_file.stem.replace("AGG-", "").lower())
            total = data.get("total_elementos", 0)
            sources = data.get("fontes_consolidadas", [])
            version = data.get("versao", "0.0.0")

            agg_stats.append({
                "file": agg_file.name,
                "domain": domain,
                "total_elementos": total,
                "num_sources": len(sources),
                "version": version,
                "sources": [s.get("fonte", "unknown") for s in sources],
            })
        except (yaml.YAMLError, KeyError, TypeError):
            continue

    return agg_stats


# ---------------------------------------------------------------------------
# TEAM STATE MANAGEMENT
# ---------------------------------------------------------------------------


def load_team_state() -> dict:
    """Load current team creation state."""
    if TEAM_STATE_PATH.exists():
        return json.loads(TEAM_STATE_PATH.read_text(encoding="utf-8"))
    return {"teams_created": {}, "last_scan": None}


def save_team_state(state: dict) -> None:
    """Save team creation state."""
    TEAM_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    TEAM_STATE_PATH.write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# AGENT SCAFFOLDING
# ---------------------------------------------------------------------------

AGENT_MD_TEMPLATE = """# {role_name}

> **Tipo:** CARGO (HÍBRIDO)
> **Nível:** {nivel}
> **Domínio primário:** {domain}
> **Criado:** {date}
> **Template:** Auto-generated by Team Creation Trigger v1.0
> **Status:** SCAFFOLD — needs enrichment via /jarvis-full or manual pipeline

---

## PARTE 0: ÍNDICE

| Parte | Nome | Status |
|-------|------|--------|
| 1 | Composição Atômica | ⏳ Pendente |
| 2 | Gráfico de Identidade | ⏳ Pendente |
| 3 | Mapa Neural (DNA) | ⏳ Pendente |
| 4 | Núcleo Operacional | ⏳ Pendente |
| 5 | Sistema de Voz | ⏳ Pendente |
| 6 | Motor de Decisão | ⏳ Pendente |
| 7 | Interfaces de Conexão | ⏳ Pendente |
| 8 | Protocolo de Debate | ⏳ Pendente |
| 9 | Memória Experiencial | ⏳ Pendente |
| 10 | Expansões e Referências | ⏳ Pendente |

---

## PARTE 1: COMPOSIÇÃO ATÔMICA

**Cargo:** {role_name}
**Archetype:** {archetype}
**Tagline:** {tagline}
**Domínios:** {domain}

### Fontes DNA (auto-detected from AGG-{agg_domain})

{sources_table}

---

## METADADOS

| Campo | Valor |
|-------|-------|
| **Gerado por** | team_creation_trigger.py v1.0 |
| **Data** | {date} |
| **AGG fonte** | AGG-{agg_domain}.yaml |
| **Elementos no domínio** | {total_elements} |
| **Status** | SCAFFOLD |
"""

SOUL_MD_TEMPLATE = """# SOUL: {role_name}

> **Cargo:** {role_name}
> **Nível:** {nivel}
> **Gerado:** {date}
> **Status:** SCAFFOLD — precisa de enriquecimento

---

## QUEM SOU EU

Eu sou o {role_name} do sistema. Minha especialidade é {tagline}.

## SISTEMA DE VOZ

- Tom: Profissional e direto
- Vocabulário: Técnico do domínio {domain}
- Approach: Data-driven, baseado nas fontes do DNA

## O QUE ACREDITO

*Pendente — será populado após enriquecimento via pipeline.*
"""

MEMORY_MD_TEMPLATE = """# MEMÓRIA: {role_name}

> **Agente:** `/agents/cargo/{nivel}/{slug}/AGENT.md`
> **Criada:** {date}
> **Última atualização:** {date}
> **Total de registros:** 0 (scaffold)
> **Versão:** 1.0.0

---

## METADADOS DE CONTEXTO

### Projeto Atual
| Campo | Valor |
|-------|-------|
| **Domínio primário** | {domain} |
| **Status** | SCAFFOLD — pendente enriquecimento |

---

## PADRÕES DECISÓRIOS

| ID | Situação | Decisão Padrão | chunk_id | PATH_RAIZ | Confiança |
|----|----------|---|---|---|---|

*Pendente — será populado após enriquecimento via pipeline.*

---

## HABILIDADES DISTRIBUÍDAS

> Habilidades extraídas automaticamente pelo Skill Distribution Engine.

| ID | Habilidade | Domínios | Fonte | Relevância |
|----|-----------|---------|-------|------------|

*Pendente — será populado pelo skill_distribution.py.*
"""

DNA_CONFIG_TEMPLATE = """# DNA-CONFIG: {role_name}
# Auto-generated by Team Creation Trigger v1.0
# Status: SCAFFOLD — needs enrichment

cargo: "{role_name}"
versao: "1.0.0"
nivel: "{nivel}"
natureza: "HIBRIDO"
data_criacao: "{date}"
ultima_atualizacao: "{date}"
status: "SCAFFOLD"

dominio_primario: "{domain}"
agg_fonte: "AGG-{agg_domain}.yaml"

fontes:
{sources_yaml}
"""


def scaffold_agent(
    slug: str,
    role_name: str,
    nivel: str,
    archetype: str,
    tagline: str,
    domain: str,
    agg_domain: str,
    total_elements: int,
    sources: list[str],
    dry_run: bool = False,
) -> dict:
    """Create the 4 files for a new cargo agent scaffold."""
    agent_dir = AGENTS_CARGO / nivel / slug
    date = datetime.now(UTC).strftime("%Y-%m-%d")

    if agent_dir.exists() and (agent_dir / "AGENT.md").exists():
        return {"status": "exists", "path": str(agent_dir.relative_to(BASE_DIR))}

    # Build sources table for AGENT.md
    sources_table = "| Fonte | Path |\n|-------|------|\n"
    for src in sources:
        sources_table += f"| {src} | knowledge/external/dna/persons/{src}/ |\n"

    # Build sources YAML for DNA-CONFIG
    sources_yaml = ""
    for src in sources:
        sources_yaml += f'  - fonte: "{src}"\n'
        sources_yaml += f'    path: "knowledge/external/dna/persons/{src}/"\n'
        sources_yaml += f"    peso: 0.70\n"
        sources_yaml += f"    status: \"pendente_enriquecimento\"\n"

    if dry_run:
        return {
            "status": "would_create",
            "path": str(agent_dir.relative_to(BASE_DIR)),
            "files": ["AGENT.md", "SOUL.md", "MEMORY.md", "DNA-CONFIG.yaml"],
        }

    # Create directory and files
    agent_dir.mkdir(parents=True, exist_ok=True)

    (agent_dir / "AGENT.md").write_text(
        AGENT_MD_TEMPLATE.format(
            role_name=role_name,
            nivel=nivel.upper(),
            domain=domain,
            date=date,
            archetype=archetype,
            tagline=tagline,
            agg_domain=agg_domain.upper(),
            total_elements=total_elements,
            sources_table=sources_table,
            slug=slug,
        ),
        encoding="utf-8",
    )

    (agent_dir / "SOUL.md").write_text(
        SOUL_MD_TEMPLATE.format(
            role_name=role_name,
            nivel=nivel.upper(),
            date=date,
            tagline=tagline,
            domain=domain,
        ),
        encoding="utf-8",
    )

    (agent_dir / "MEMORY.md").write_text(
        MEMORY_MD_TEMPLATE.format(
            role_name=role_name,
            nivel=nivel,
            slug=slug,
            date=date,
            domain=domain,
        ),
        encoding="utf-8",
    )

    (agent_dir / "DNA-CONFIG.yaml").write_text(
        DNA_CONFIG_TEMPLATE.format(
            role_name=role_name,
            nivel=nivel.upper(),
            date=date,
            domain=domain,
            agg_domain=agg_domain.upper(),
            sources_yaml=sources_yaml if sources_yaml else "  []  # No sources yet\n",
        ),
        encoding="utf-8",
    )

    return {
        "status": "created",
        "path": str(agent_dir.relative_to(BASE_DIR)),
        "files": ["AGENT.md", "SOUL.md", "MEMORY.md", "DNA-CONFIG.yaml"],
    }


# ---------------------------------------------------------------------------
# MAIN TRIGGER PIPELINE
# ---------------------------------------------------------------------------


def check_and_create_teams(dry_run: bool = False) -> dict:
    """Main entry: scan AGGs, check thresholds, scaffold missing agents.

    Returns summary of actions taken.
    """
    results = {
        "timestamp": datetime.now(UTC).isoformat(),
        "aggs_scanned": 0,
        "teams_triggered": [],
        "agents_created": [],
        "agents_existing": [],
        "below_threshold": [],
    }

    state = load_team_state()
    agg_stats = scan_agg_files()
    results["aggs_scanned"] = len(agg_stats)

    for agg in agg_stats:
        domain = agg["domain"]
        total = agg["total_elementos"]
        num_sources = agg["num_sources"]

        # Check thresholds
        if total < MIN_ELEMENTS_THRESHOLD or num_sources < MIN_SOURCES_THRESHOLD:
            results["below_threshold"].append({
                "domain": domain,
                "elements": total,
                "sources": num_sources,
                "needs_elements": max(0, MIN_ELEMENTS_THRESHOLD - total),
                "needs_sources": max(0, MIN_SOURCES_THRESHOLD - num_sources),
            })
            continue

        # Domain qualifies — check team template
        template = TEAM_TEMPLATES.get(domain)
        if not template:
            continue

        team_info = {
            "domain": domain,
            "team_name": template["team_name"],
            "icon": template["icon"],
            "elements": total,
            "sources": num_sources,
            "roles_checked": [],
        }

        # Scaffold each role in the team
        for role_slug, role_name, archetype, tagline, nivel in template["roles"]:
            result = scaffold_agent(
                slug=role_slug,
                role_name=role_name,
                nivel=nivel,
                archetype=archetype,
                tagline=tagline,
                domain=domain,
                agg_domain=agg["file"].replace("AGG-", "").replace(".yaml", ""),
                total_elements=total,
                sources=agg["sources"],
                dry_run=dry_run,
            )

            team_info["roles_checked"].append({
                "role": role_name,
                "slug": role_slug,
                **result,
            })

            if result["status"] == "created":
                results["agents_created"].append(f"{nivel}/{role_slug}")
            elif result["status"] == "exists":
                results["agents_existing"].append(f"{nivel}/{role_slug}")

        results["teams_triggered"].append(team_info)

        # Update state
        if not dry_run:
            state["teams_created"][domain] = {
                "date": datetime.now(UTC).isoformat(),
                "elements": total,
                "sources": num_sources,
                "roles": [r[0] for r in template["roles"]],
            }

    # Save state
    if not dry_run:
        state["last_scan"] = datetime.now(UTC).isoformat()
        save_team_state(state)

        # Append to log
        TEAM_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(TEAM_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(results, ensure_ascii=False) + "\n")

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    """CLI entry point."""
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    print("=" * 60)
    print("TEAM CREATION TRIGGER v1.0")
    print("=" * 60)

    if dry_run:
        print("[DRY RUN] No files will be created.\n")

    results = check_and_create_teams(dry_run=dry_run)

    print(f"\nAGGs scanned: {results['aggs_scanned']}")
    print(f"Teams triggered: {len(results['teams_triggered'])}")
    print(f"Agents created: {len(results['agents_created'])}")
    print(f"Agents existing: {len(results['agents_existing'])}")
    print(f"Below threshold: {len(results['below_threshold'])}")

    if results["teams_triggered"]:
        print(f"\n{'-' * 50}")
        for team in results["teams_triggered"]:
            print(f"\n  {team['team_name']} ({team['domain']})")
            print(f"   Elements: {team['elements']} | Sources: {team['sources']}")
            for role in team["roles_checked"]:
                status_tag = "[NEW]" if role["status"] == "created" else "[OK]" if role["status"] == "exists" else "[?]"
                print(f"   {status_tag} {role['role']}: {role['status']}")

    if verbose and results["below_threshold"]:
        print(f"\n{'-' * 50}")
        print("Below threshold:")
        for bt in results["below_threshold"]:
            print(f"  {bt['domain']}: {bt['elements']} elements, {bt['sources']} sources")
            if bt["needs_elements"] > 0:
                print(f"    needs {bt['needs_elements']} more elements")
            if bt["needs_sources"] > 0:
                print(f"    needs {bt['needs_sources']} more sources")

    print(f"\nState: {TEAM_STATE_PATH}")
    print(f"Log: {TEAM_LOG}")
    print("Done.")


if __name__ == "__main__":
    main()
