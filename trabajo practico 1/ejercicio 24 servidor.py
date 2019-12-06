import socket, sys, os, time, getopt


if __name__ == "__main__":
    # creo el socket para servidor
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print("Error al crear socket de server")
        sys.exit()
    # serversocket.settimeout(2)
    host = "127.0.0.1"  # o "localhost"
    # host = socket.gethostname()
    puerto = ""  # debe ser pasado como argumento
    file = ""
    f = ""
    # toma las opciones con getopt
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:f:', ["puerto", "archivo"])

    for(op, ar) in opt:
        if op == '-p':
            puerto = int(ar)  # almacena el numero de puerto
        elif op == '-f':
            file = str(ar)  # almacena el nombre del archivo a crear/usar

    # le doy al socket el puerto y el host usando la funcion ".bind" de serversocket:
    serversocket.bind((host, puerto))
    # serversocket.setblocking(bool(0))
    # serversocket.listen(1)
    print("Esperando conexion...")
    # (conn, direc) = serversocket.accept()

    # creo el archivo en el que se guardarán los datos:
    try:
        print("Abriendo archivo...")
        f = open(file, 'w')
    except IOError:
        print("Error. El archivo no se pudo abrir")
    except:
        print("Error... de algún tipo...")

    # serversocket.connect()
    print("Esperando respuesta de cliente")
    while True:
        # dato = conn.recv(1024)
        try:
            dato = serversocket.recv(1024)  # recive no más de 1024 bytes
            log = dato.decode("ascii")
            if not dato: break
            print("Escribiendo...")
            f.write(log)
        except EOFError:
            print("Fin de línea (1)")  # por alguna razón no salta este error
            break
        except log == EOFError:
            print("Fin de línea (2)")  # acá tampoco
            break
        else:
            if log == "--":
                print("Fin de línea (3)")  # tuve que recurrir a la vieja confiable
                break
        time.sleep(1)

    print("Cerrando programa")
    serversocket.close()