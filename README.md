# 🔍 Port Scanner em Python

Scanner de portas de rede desenvolvido em Python, evoluindo de um script simples até uma ferramenta com threads, banner grabbing e output em JSON/CSV.

---

## 📁 Versões do Projeto

| Versão | Descrição |
|---|---|
| `v1_scanner.py` | Scan sequencial simples |
| `v2_scanner.py` | Scan com threads (mais rápido) |
| `v3_scanner.py` | Banner grabbing nas portas comuns |
| `v4_scanner.py` | Argparse + output em JSON/CSV |

---

## 🚀 Como usar

### Pré-requisitos

- Python 3.x
- Nenhuma biblioteca externa — só stdlib

---

### V1 — Scan sequencial

Varre as portas 1 a 1024 uma por vez e mede o tempo total.

```bash
python v1_scanner.py
```

---

### V2 — Scan com threads

Dispara múltiplas conexões em paralelo usando `ThreadPoolExecutor`, bem mais rápido que a v1.

```bash
python v2_scanner.py
```

---

### V3 — Banner Grabbing

Conecta nas portas 21 (FTP), 22 (SSH) e 80 (HTTP) e captura a mensagem de identificação do serviço.

```bash
python v3_scanner.py
```

Para testar localmente, abra um servidor em outro terminal:

```bash
python3 -m http.server 8080
```

---

### V4 — Argparse + JSON/CSV

Versão completa com argumentos de linha de comando e opções de output.

```bash
python v4_scanner.py --host localhost --inicio 1 --fim 1024 --output print
python v4_scanner.py --host localhost --inicio 8080 --fim 8080 --output json
python v4_scanner.py --host localhost --inicio 8080 --fim 8080 --output csv
```

#### Argumentos disponíveis

| Argumento | Descrição | Padrão |
|---|---|---|
| `--host` | Host a escanear | `localhost` |
| `--inicio` | Porta inicial | `1` |
| `--fim` | Porta final | `1` |
| `--output` | Formato de saída: `print`, `json`, `csv` | `print` |

#### Exemplos de output

**Print:**
```
Porta: 8080 | Status: aberta | Banner: HTTP/1.1 200 OK...
```

**JSON (`resultado.json`):**
```json
[
    {
        "porta": 8080,
        "status": "aberta",
        "banner": "HTTP/1.1 200 OK..."
    }
]
```

**CSV (`resultado.csv`):**
```
porta,status,banner
8080,aberta,HTTP/1.1 200 OK...
```

---

## 🧠 Conceitos aprendidos

- **Socket TCP** — como estabelecer conexões de rede com `socket.connect_ex()`
- **Timeout** — evitar travamento em portas que não respondem com `settimeout()`
- **Threads** — paralelismo com `threading.Thread` e `ThreadPoolExecutor`
- **Banner Grabbing** — capturar a identificação de serviços de rede
- **Protocolos** — diferença entre HTTP (cliente fala primeiro) e SSH/FTP (servidor fala primeiro)
- **Argparse** — criar interfaces de linha de comando
- **JSON/CSV** — salvar resultados em diferentes formatos

---

## ⚠️ Aviso legal

Este projeto foi desenvolvido para fins educacionais. Use apenas em redes e sistemas que você tem permissão para escanear.
