import socket
import time

while True:
    enderecoIP = socket.gethostbyname(socket.gethostname())
    if enderecoIP == "127.0.0.1":
        print("Desconectado, seu endereço de IP é o localhost: " + enderecoIP)
    else:
        print("Conectado, seu endereço de IP é: " + enderecoIP)
    time.sleep(2)
