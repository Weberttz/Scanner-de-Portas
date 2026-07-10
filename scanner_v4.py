import socket
import time 
import argparse, json, csv

def scan_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))
    sock.close()
    return resultado == 0

def banner_grab(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))

    if resultado != 0: # se não conseguiu conectar
        return None
    
    portas_http = [80, 8080, 8000, 3000]

    if porta in portas_http: # percorre portas que precisam de request http
            sock.send("GET / HTTP/1.1\r\nHost: host\r\n\r\n".encode()) # envia os bytes 

    dados = sock.recv(1024) # recebe os bytes
    banner = dados.decode(errors="ignore") # transforma os bytes em string

    sock.close()
    return banner

def parse_args(): # arg parse para rodar por linha de comando
    parser = argparse.ArgumentParser(description="Passe os argumentos!")
    parser.add_argument("--host", default="localhost", help="Host para escanear")
    parser.add_argument("--inicio", type=int, default=1, help="Porta incial")
    parser.add_argument("--fim", type=int, default=1024)
    parser.add_argument("--output", choices=["json", "csv", "print"], default="print")
    
    return parser.parse_args()

def salvar_json(resultados, arquivo): # salvar em json
    with open(arquivo, "w") as f: # abrir o arquivo e formatar com ident 4
        json.dump(resultados, f, indent=4)

def salvar_csv(resultados, arquivo): # salvar em csv
    with open("resultado.csv", "w", newline="") as arquivo: # abrir arquivo
        writer = csv.writer(arquivo) # criar um escritor
        
        # escreve cabeçalho
        writer.writerow(["porta", "status", "banner"])
        
        # escreve cada linha formatada
        for linha in resultados:
            writer.writerow([linha["porta"], linha["status"], linha["banner"]])

def imprimir_no_terminal(resultados): # imprimir todos os resultados direto no terminal
    for resultado in resultados:
       print(f"Porta: {resultado['porta']} | Status: {resultado['status']} | Banner: {resultado['banner']}")

def main():
    args = parse_args()

    resultados = []

    for porta in range(args.inicio, args.fim + 1):
        if scan_porta(args.host, porta):
            banner = banner_grab(args.host, porta)
            resultados.append({
                "porta": porta,
                "status": "aberta",
                "banner": banner
            })

    if args.output == "json":
        salvar_json(resultados, "resultado.json")
    if args.output == "csv":
        salvar_csv(resultados, "resultado.csv")
    if args.output == "print":
        imprimir_no_terminal(resultados)

main()

# TESTES
# use 'python3 -m http.server 8080' para abrir servidor em outro terminal

# use 'python3 scanner_v4.py --host localhost --inicio 8080 --fim 8080 --output print' para apenas printar no terminal 
# use 'python3 scanner_v4.py --host localhost --inicio 8080 --fim 8080 --output json' para criar arquivo json   
# use 'python3 scanner_v4.py --host localhost --inicio 8080 --fim 8080 --output csv' para criar arquivo csv