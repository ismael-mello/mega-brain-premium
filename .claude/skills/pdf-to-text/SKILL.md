> **Auto-Trigger:** Quando usuario pede para ler/analisar arquivo PDF
> **Keywords:** "pdf", "ler pdf", "analisar pdf", "converter pdf", "extrair pdf", "abrir pdf"
> **Prioridade:** ALTA
> **Tools:** Bash, Read

# PDF to Text Converter

Converte PDF para texto puro (.txt) antes de ler, evitando limite de 20 paginas e reduzindo tokens consumidos.

## Quando Ativar

- Usuario menciona arquivo `.pdf`
- Usuario pede para "ler", "analisar", "extrair" conteudo de PDF
- Arquivo PDF tem mais de 10 paginas

## Quando NAO Ativar

- Arquivo ja e `.txt`, `.md`, `.docx`
- Usuario quer apenas ver imagens/graficos do PDF (nao suportado)
- PDF ja foi convertido anteriormente (verificar se `.txt` existe)

## Como Usar

### Conversao Automatica

Quando detectar um PDF, executar ANTES de ler:

```bash
python3 ".claude/skills/pdf-to-text/convert_pdf.py" "<caminho_do_pdf>"
```

### Opcoes

```bash
# Converter para texto (default)
python3 ".claude/skills/pdf-to-text/convert_pdf.py" "arquivo.pdf"

# Converter para markdown (preserva headings)
python3 ".claude/skills/pdf-to-text/convert_pdf.py" "arquivo.pdf" --output md

# Converter apenas paginas especificas
python3 ".claude/skills/pdf-to-text/convert_pdf.py" "arquivo.pdf" --pages 1-10
```

### Output

O script cria um arquivo `.txt` (ou `.md`) na mesma pasta do PDF original.
Exemplo: `documento.pdf` → `documento.txt`

### Fluxo Completo

```
1. Usuario: "analisa esse PDF: C:\Users\...\doc.pdf"
2. JARVIS: Executa convert_pdf.py → gera doc.txt
3. JARVIS: Le doc.txt com Read tool (sem limite de paginas)
4. JARVIS: Analisa conteudo normalmente
```

## Dependencias

- Python 3
- PyMuPDF (`pip install pymupdf`) - ja instalado

## Limitacoes

- Nao extrai imagens ou graficos
- Tabelas complexas podem perder formatacao
- PDFs escaneados (imagem) precisam de OCR (nao suportado)
