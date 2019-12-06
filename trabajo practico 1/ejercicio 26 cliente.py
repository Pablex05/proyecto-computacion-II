import socket, sys, os


if __name__ == "__main__":
    # crea socket pa' cliente
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # toma los parámetros de la línea de comandos
    host = sys.argv[1]
    port = int(sys.argv[2])
    print("Conectando a server")
    clientsocket.connect((host, port))
    while True:
        men = input("- Ingrese mensaje: ")
        dato = men.encode("ascii")
        clientsocket.sendto(dato, (host, port))
        if men == "exit" or men == "EXIT":
            break
    clientsocket.close()
