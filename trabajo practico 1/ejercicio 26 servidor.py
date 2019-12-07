import socket, sys, os, time

def hijo(clin, direc, n):
    print("hijo: ", n, " PID: ", os.getpid(), " esperando mensaje de cliente")
    while True:
        men = clin.recv(1024)
        if men.decode("ascii") == "exit" or men.decode("ascii") == "EXIT":
            clin.__exit__()
            break
        print("PID: ", os.getpid()," desde:", direc," peername: ", clin.getpeername(), "soketname:", clin.getsockname(),
              " Recibido: ", men.decode("ascii"))
    print("Fin hijo: ", n)
    clin.close()
    sys.exit(0)

if __name__ == "__main__":
    print("Abriendo servidor...")
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Error al crear socket de server")
        sys.exit()
    host = ""
    port = int(sys.argv[1])  # recibe desde linea de comando
    serversocket.bind((host, port))
    serversocket.listen(5)
    print("Escuchando - creando hijos...")
    n = int(0)
    while True:
        n = n + 1
        cs, d = serversocket.accept()
        print("coneccion desde %s" % str(d))
        print("Derivando a hijo: ", n)
        newpid = os.fork()
        if newpid == 0:
            hijo(cs, d, n)
        else:
            time.sleep(1)
            #os.wait()