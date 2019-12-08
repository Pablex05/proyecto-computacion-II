import socket, sys, getopt, threading

def abrir(name, c):
    try:
        print("Abriendo archivo...")
        f = open(name, 'a+')
        men = str("Serv: Archivo abierto\n")
        c.send(men.encode('ascii'))
        return f
    except IOError:
        men = str("Serv: IOError. El archivo no se pudo abrir")
        c.send(men.encode('ascii'))
        zo = str(0)
        c.send(zo.encode("ascii"))
        return IOError
    except:
        men = str("Serv: Error... de algún tipo...")
        c.send(men.encode('ascii'))
        zo = str(0)
        c.send(zo.encode("ascii"))
        return 0

def hilo(clin, direc, n):
    print("hilo: ", n, " esperando cliente")
    while True:
        men = clin.recv(1024)
        tarea = men.decode("ascii")
        if tarea == 'abrir' or tarea == 'ABRIR':
            msg = str("Serv: ingrese nombre de archivo a abrir: ")
            clin.send(msg.encode('ascii'))
            men = clin.recv(1024)
            aux = men
            nom = men.decode("ascii")
            file = abrir(nom, clin)
            if file == IOError or file == 0:
                clin.__exit__()
                break
            while True:
                msg = str("Serv: Ingrese una opcion: Agregar - Leer - Cerrar")
                clin.send(msg.encode('ascii'))
                men = clin.recv(1024)
                tarea = men.decode("ascii")
                if tarea == "agregar" or tarea == "AGREGAR":
                    men = str("Serv: Ingrese el contenido que desea agregar al archivo")
                    clin.send(men.encode("ascii"))
                    recibido = clin.recv(1024)
                    agregacion = recibido.decode("ascii")
                    try:
                        file.write(agregacion)
                        file.write("\n")
                        men = str("Serv: Escritura en archivo exitosa\n")
                        clin.send(men.encode("ascii"))
                    except:
                        men = str("Serv: Error al escribir archivo\n")
                        clin.send(men.encode("ascii"))
                elif tarea == "leer" or tarea == "LEER":
                    file.close()
                    file = open(aux, 'r+')
                    men = str("Serv: Leyendo archivo...")
                    clin.send(men.encode("ascii"))
                    leido = file.read()
                    clin.send(leido.encode("ascii"))
                    file.close()
                    file = open(aux, 'a+')
                elif tarea == "cerrar" or tarea == "CERRAR":
                    men = str("Serv: Cerrando archivo...")
                    clin.send(men.encode("ascii"))
                    file.close()
                    clin.__exit__()
                    break
            if tarea == "cerrar" or tarea == "CERRAR":
                break
    print("Fin hilo: ", n)
    clin.close()
    clin.__exit__()
    sys.exit(0)

if __name__ == "__main__":
    print("Abriendo servidor...")
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Error al crear socket de server")
        sys.exit()
    host = ''
    port = ''
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ["puerto",])
    for (op, ar) in opt:
        if op == '-p':
            port = int(ar)
    serversocket.bind((host, port))
    serversocket.listen(5)
    print("Esperando conexiones - creando hilos...")
    n = int(0)
    while True:
        n = n + 1
        cs, d = serversocket.accept()
        print("coneccion desde %s" % str(d))
        print("Derivando a hilo: ", n)
        thr = threading.Thread(target=hilo, args=(cs, d, n))
        thr.start()
