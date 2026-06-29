import socket
import time 
from threading import Thread

portas_abertas = []

def scan_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criar socket Ipv4 + TCP
    sock.settimeout(1) # tempo de um segundo
    resultado = sock.connect_ex((host, porta)) # tentar abrir conexão
    sock.close() # fechar socket
    if resultado == 0:
        portas_abertas.append(porta) # adiciona se estiver aberta

def main():
    threads = []
    host = "localhost"
    portas = range(1, 1025)

    print(f"Escaneando {host}...\n")
    inicio = time.time()

    for porta in portas:
        thread = Thread(target=scan_porta, args=(host, porta)) # abre nova thread 
        threads.append(thread) # adiciona à lista de threads
        thread.start()  # dispara a thread 

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

    fim = time.time()

    print(sorted(portas_abertas)) # ordena a lista de portas abertas
    print(f"\nConcluído em {fim - inicio:.2f}s") #transformar tempo de segundos legíveis

main()