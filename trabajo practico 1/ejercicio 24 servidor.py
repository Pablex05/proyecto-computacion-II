import socket, sys, os, time, getopt


if __name__ == "__main__":
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print("Error al crear socket de server")
        sys.exit()
    host = "127.0.0.1" 
    puerto = ""  
    file = ""
    f = ""
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:f:', ["puerto", "archivo"])
    for(op, ar) in opt:
        if op == '-p':
            puerto = int(ar)
        elif op == '-f':
            file = str(ar) 
    serversocket.bind((host, puerto))
    print("Esperando conexion...")
    try:
        print("Abriendo archivo...")
        f = open(file, 'w')
    except IOError:
        print("Error. El archivo no se pudo abrir")
    except:
        print("Error... de algún tipo...")
    print("Esperando respuesta de cliente")
    while True:
        try:
            dato = serversocket.recv(1024) 
            log = dato.decode("ascii")
            if not dato: break
            print("Escribiendo...")
            f.write(log)
        except EOFError:
            print("Fin de línea (1)") 
            break
        except log == EOFError:
            print("Fin de línea (2)")  
            break
        else:
            if log == "--":
                print("Fin de línea (3)") 
                break
        time.sleep(1)
    print("Cerrando programa")
    serversocket.close()
