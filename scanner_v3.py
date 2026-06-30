import socket
import time 

def banner_grab(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))

    if resultado != 0: # se não conseguiu conectar
        return None
    
    portas_http = [80, 8080, 8000, 3000]

    for p in portas_http: # percorre portas que precisam de request http
        if(porta == p):
            sock.send("GET / HTTP/1.1\r\nHost: host\r\n\r\n".encode()) # envia os bytes 

    dados = sock.recv(1024) # recebe os bytes
    banner = dados.decode(errors="ignore") # transforma os bytes em string

    sock.close()
    return banner

def scan_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))
    sock.close()
    return resultado == 0

def main():
    host = "localhost"
    portas_comuns = [21, 22, 80, 3000, 8000, 8080]

    print(f"Escaneando {host}...\n")
    inicio = time.time()

    for porta in portas_comuns:
        if scan_porta(host, porta):
            banner = banner_grab(host, porta)
            print(f"Porta:{porta} Banner:{banner}")


    fim = time.time()

    print(f"\nConcluído em {fim - inicio:.2f}s")

main()