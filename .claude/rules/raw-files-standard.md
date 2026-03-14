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
║   knowledge/external/sources/{fonte-kebab-case}/raw/                                  ║
║                                                                              ║
║   NUNCA em: archive/, inbox/, ou qualquer outro local                        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### Estrutura Padrao por Fonte

```
knowledge/external/sources/{fonte}/
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
| alex-hormozi | `knowledge/external/sources/alex-hormozi/raw/` | OK |
| jeremy-haynes | `knowledge/external/sources/jeremy-haynes/raw/` | OK |
| jeremy-miner | `knowledge/external/sources/jeremy-miner/raw/` | OK |
| russell-brunson | `knowledge/external/sources/russell-brunson/raw/` | OK (corrigido 2026-03-02) |
| cole-gordon | `knowledge/external/sources/cole-gordon/` | Sem raw (aguardando material) |
| sam-ovens | `knowledge/external/sources/sam-ovens/` | Sem raw (aguardando material) |
| 30-day-challenge | `knowledge/external/sources/30-day-challenge/raw/` | OK |
| client-accelerator | `knowledge/external/sources/client-accelerator/raw/` | OK |
| ead-closer | `knowledge/external/sources/ead-closer/raw/` | OK |
| the-scalable-company | `knowledge/external/sources/the-scalable-company/raw/` | OK |

### Regras

- **NAO PODE** criar pasta `archive/` para materiais raw
- **NAO PODE** deixar materiais raw em `inbox/` permanentemente
- **NAO PODE** colocar raw files na raiz de `knowledge/external/sources/{fonte}/`
- **DEVE** sempre usar subpasta `raw/` dentro da fonte
- **DEVE** manter estrutura de pastas original do curso/programa dentro de `raw/`
- **DEVE** atualizar `DNA-CONFIG.yaml` campo `raiz:` apontando para `knowledge/external/sources/{fonte}/raw/`

### Ao Ingerir Novo Material

```
1. Identificar fonte (pessoa ou programa)
2. Criar/verificar knowledge/external/sources/{fonte}/raw/
3. Mover material para raw/ mantendo estrutura original
4. Atualizar DNA-CONFIG.yaml com path correto
5. NUNCA usar archive/ ou inbox/ como destino permanente
```

---

**FIM DO RAW-FILES-STANDARD**
