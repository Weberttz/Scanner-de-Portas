import socket
import time 

def scan_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria socket Ipv4 + TCP
    sock.settimeout(1) # tempo de um segundo
    resultado = sock.connect_ex((host, porta)) # tenta abrir conexão
    sock.close() # fecha socket
    return resultado == 0

def main():
    host = "localhost"
    portas = range(1, 1025)

    print(f"Escaneando {host}...\n")
    inicio = time.time()

    for porta in portas:
        resultado = scan_porta(host, porta)

        if resultado:
            print(f"[ ABERTA ] porta {porta} ")
        else:
            print(f"[ FECHADA ] porta {porta}")

    fim = time.time()

    print(f"\nConcluído em {fim - inicio:.2f}s") # transforma tempo de segundos legíveis

main()