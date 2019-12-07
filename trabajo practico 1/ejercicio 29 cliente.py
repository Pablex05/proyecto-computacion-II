import socket, sys, os

if __name__ == "__main__":
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = sys.argv[1]
    port = int(sys.argv[2])
    print("Conectando a server")
    clientsocket.connect((host, port))
    print("Ingrese el comando ABRIR para comenzar a usar un archivo \n CERRAR para salir")
    men = input("--> ")
    dato = men.encode("ascii")
    clientsocket.sendto(dato, (host, port))
    if men == 'ABRIR' or men == 'abrir':
        while True:
            r = clientsocket.recv(1024)
            print(r.decode("ascii"))
            men = input("--> ")
            dato = men.encode("ascii")
            clientsocket.sendto(dato, (host, port))
            r = clientsocket.recv(1024)
            print(r.decode("ascii"))
            while True:
                r = clientsocket.recv(1024)
                print(r.decode("ascii"))
                men = input("--> ")
                dato = men.encode("ascii")
                clientsocket.sendto(dato, (host, port))
                if men == "cerrar" or men == "CERRAR":
                    r = clientsocket.recv(1024)
                    print(r.decode("ascii"))
                    salir = 1
                    break
                elif men == "agregar" or men == "AGREGAR":
                    r = clientsocket.recv(1024)
                    print(r.decode("ascii"))
                    agr = input("-> ")
                    dato = agr.encode("ascii")
                    clientsocket.sendto(dato, (host, port))
                elif men == "leer" or men == "LEER":
                    r = clientsocket.recv(1024)
                    print(r.decode("ascii"))
            if salir == 1: break
    print("Saliendo")
    clientsocket.close()