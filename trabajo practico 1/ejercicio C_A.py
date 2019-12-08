import socket, sys, os, time
import threading


def hijo(clin, direc):
    men = clin.recv(1024)
    print("Mensaje BB: ", men.decode("ascii"))
    aux = ""
    while True:
        men = clin.recv(1024)
        if aux != men.decode("ascii"):
            print("Mensaje BB: ", men.decode("ascii"))
        aux = men
        if men.decode("ascii") == "cambio" or men.decode("ascii") == "CAMBIO":
            print("==============================")
            while True:
                men = input("-->: ")
                clin.send(men.encode("ascii"))
                if men == "cambio" or men == "cambio":
                    print("==============================")
                    break
            if men == "exit" or men == "EXIT":
                print("fin de conversacion")
                serversocket.__exit__()
                break
        if aux == "EXIT" or aux == "exit":
            print("fin de conversacion")
            serversocket.__exit__()
            break
    clin.__exit__()
    clin.close()
    sys.exit(0)


if __name__ == "__main__":
    print("Abriendo chat...")
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Error al crear socket de server")
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])
    serversocket.bind((host, port))
    serversocket.listen(1)
    print("Esperando conexion....")
    while True:
        cs, d = serversocket.accept()
        print("coneccion desde %s" % str(d))
        print("==============================")
        thr = threading.Thread(target=hijo, args=(cs, d))
        thr.start()
    serversocket.__exit__()
    sys.exit(0)