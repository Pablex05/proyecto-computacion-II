import socket, sys, os, time, getopt

if __name__ == "__main__":
    # creo el socket para servidor
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Error al crear socket de server")
        sys.exit()
    host = ""  # la ip en el server es "127.0.0.1"
    puerto = ""  # debe ser pasado como argumento
    f = ""
    # toma las opciones con getopt
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:a:', ["puerto", "host"])

    for(op, ar) in opt:
        if op == '-p':
            puerto = int(ar)  # aalmacena el numero de puerto
        elif op == '-a':
            host = str(ar)  # almacena el nombre del archivo a crear/usar

    # le doy al socket el puerto y el host usando la funcion ".bind" de serversocket:
    # clientsocket.bind((host, puerto))
    print("Conectando a server")
    clientsocket.connect((host, puerto))

    # creación y envío de mensaje
    mensaje = []
    print("Ingrese un mensaje:")
    while True:
        # dato = input()
        # mensaje.append(dato.encode("ascii"))
        try:
            mensaje.append(input().encode("ascii"))
        except EOFError:
            mensaje.append(("--").encode("ascii"))  # "--" la vieja confiable
            print("except 1")
            break
        except KeyboardInterrupt:
            print("except 2")
            break

    print("Enviando mensaje")
    for linea in mensaje:
        clientsocket.sendto(linea, (host, puerto))
        time.sleep(1)
    print("Cerrando programa")
    clientsocket.close()