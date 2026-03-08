# RAW FILES STANDARD

> **Auto-Trigger:** Qualquer operacao com arquivos raw, inbox, archive, transcricoes
> **Keywords:** "raw", "archive", "inbox", "transcricao", "mover arquivo", "organizar", "download", "ingest"
> **Prioridade:** ALTA
> **Versao:** 1.0.0
> **Criado:** 2026-03-02

---

## REGRA ABSOLUTA: LOCALIZACAO PADRAO DE ARQUIVOS RAW

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   TODOS os arquivos raw/originais DEVEM ficar em:                            ║
║                                                                              ║
║   knowledge/sources/{fonte-kebab-case}/raw/                                  ║
║                                                                              ║
║   NUNCA em: archive/, inbox/, ou qualquer outro local                        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### Estrutura Padrao por Fonte

```
knowledge/sources/{fonte}/
├── _INDEX.md                    ← Indice dos documentos processados
├── 01-TEMA-A.md                 ← Documento processado
├── 02-TEMA-B.md                 ← Documento processado
└── raw/                         ← ARQUIVOS ORIGINAIS (transcricoes, PDFs, etc.)
    ├── programa-1/
    │   ├── modulo-1/
    │   │   └── transcription_aula.txt
    │   └── modulo-2/
    │       └── transcription_aula.txt
    └── programa-2/
        └── ...
```

### Fontes Existentes (Referencia)

| Fonte | Path Raw | Status |
|-------|----------|--------|
| alex-hormozi | `knowledge/sources/alex-hormozi/raw/` | OK |
| jeremy-haynes | `knowledge/sources/jeremy-haynes/raw/` | OK |
| jeremy-miner | `knowledge/sources/jeremy-miner/raw/` | OK |
| russell-brunson | `knowledge/sources/russell-brunson/raw/` | OK (corrigido 2026-03-02) |
| cole-gordon | `knowledge/sources/cole-gordon/` | Sem raw (aguardando material) |
| sam-ovens | `knowledge/sources/sam-ovens/` | Sem raw (aguardando material) |
| 30-day-challenge | `knowledge/sources/30-day-challenge/raw/` | OK |
| client-accelerator | `knowledge/sources/client-accelerator/raw/` | OK |
| ead-closer | `knowledge/sources/ead-closer/raw/` | OK |
| the-scalable-company | `knowledge/sources/the-scalable-company/raw/` | OK |

### Regras

- **NAO PODE** criar pasta `archive/` para materiais raw
- **NAO PODE** deixar materiais raw em `inbox/` permanentemente
- **NAO PODE** colocar raw files na raiz de `knowledge/sources/{fonte}/`
- **DEVE** sempre usar subpasta `raw/` dentro da fonte
- **DEVE** manter estrutura de pastas original do curso/programa dentro de `raw/`
- **DEVE** atualizar `DNA-CONFIG.yaml` campo `raiz:` apontando para `knowledge/sources/{fonte}/raw/`

### Ao Ingerir Novo Material

```
1. Identificar fonte (pessoa ou programa)
2. Criar/verificar knowledge/sources/{fonte}/raw/
3. Mover material para raw/ mantendo estrutura original
4. Atualizar DNA-CONFIG.yaml com path correto
5. NUNCA usar archive/ ou inbox/ como destino permanente
```

---

**FIM DO RAW-FILES-STANDARD**
