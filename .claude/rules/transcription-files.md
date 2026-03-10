# TRANSCRIPTION FILES STANDARD

> **Auto-Trigger:** Verificação de arquivos de transcrição, inbox scan, file content check
> **Keywords:** "transcription", "arquivo vazio", "empty", "wc -l", "0 lines", "inbox", "raw files", "conteúdo"
> **Prioridade:** ALTA
> **Versão:** 1.0.0
> **Criado:** 2026-03-10

---

## REGRA ABSOLUTA: NUNCA USAR `wc -l` PARA VERIFICAR CONTEÚDO

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  TRANSCRIÇÕES SÃO ARQUIVOS DE UMA ÚNICA LINHA SEM TERMINADOR                ║
║                                                                              ║
║  wc -l → retorna 0 linhas  ← ENGANOSO (parece vazio, não está)             ║
║  wc -c → retorna N bytes   ← CORRETO (mede conteúdo real)                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### Por quê isso acontece

Transcriptions exportadas de ferramentas como Whisper, ClickUp, ou outros serviços frequentemente geram **um único bloco de texto sem `\n` (newline)**. O comando `wc -l` conta newlines — se não há nenhum, retorna `0`, simulando arquivo vazio.

### Diagnóstico correto

```bash
# ❌ ERRADO — pode reportar 0 mesmo com 90KB de conteúdo
wc -l arquivo.txt

# ✅ CORRETO — sempre use bytes para detectar conteúdo
wc -c arquivo.txt

# ✅ MELHOR — loop completo para scan de pasta
for f in /path/to/folder/*.txt; do
  echo "$(wc -c < "$f") bytes | $(basename "$f")"
done

# ✅ ALTERNATIVA — verificar se arquivo tem conteúdo real
python3 -c "
import pathlib
p = pathlib.Path('arquivo.txt')
print(f'{p.stat().st_size} bytes: {p.name}')
"
```

### Como LER arquivos sem line terminators

```bash
# ❌ head/tail não funcionam (tudo é "linha 1")
head -n 10 arquivo.txt  # imprime o arquivo inteiro

# ✅ Python — único método confiável para chunks
python3 -c "
import pathlib
content = pathlib.Path('C:/path/to/arquivo.txt').read_text(encoding='utf-8')
chunk_size = 5000
for i in range(0, len(content), chunk_size):
    print(f'--- CHUNK {i//chunk_size + 1} ---')
    print(content[i:i+chunk_size])
"
```

### Regras Absolutas

- **NÃO PODE** declarar arquivo como vazio baseado em `wc -l = 0`
- **NÃO PODE** usar `wc -l` como check de conteúdo em qualquer pipeline
- **DEVE** sempre usar `wc -c` (bytes) ou `stat` para checar se arquivo tem conteúdo
- **DEVE** usar Python para ler transcrições longas sem line terminators
- **DEVE** ao reportar status de arquivos, sempre mostrar bytes: `X bytes | nome.txt`

### Formato de Report Correto

```
❌ ERRADO:
   "7 arquivos vazios (0 bytes)"  ← baseado em wc -l

✅ CORRETO:
   74279 bytes | transcription_1_-_Story_Selling-005.txt
   59875 bytes | transcription_2_-_How_To_Tell_A_Story.txt
   ...
```

---

**FIM DO TRANSCRIPTION-FILES-STANDARD**
