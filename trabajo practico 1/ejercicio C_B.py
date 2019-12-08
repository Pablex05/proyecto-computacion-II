import socket, sys, os

if __name__ == "__main__":
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = sys.argv[1]
    port = int(sys.argv[2])
    print("Conectando.....")
    print("escriba un mensaje.....")
    clientsocket.connect((host, port))
    while True:
        men = input("-->: ")
        dato = men.encode("ascii")
        clientsocket.sendto(dato, (host, port))
        if men == "cambio" or men == "cambio":
            print("==============================")
            while True:
                men = clientsocket.recv(1024)
                print("Mensaje AA: ", men.decode("ascii"))
                if men.decode("ascii") == "cambio" or men.decode("ascii") == "CAMBIO":
                    print("==============================")
                    break
        if men == "exit" or men == "EXIT":
            print("fin de conversacion")
            clientsocket.__exit__()
            break
    clientsocket.__exit__()
    clientsocket.close()
    sys.exit(0)
