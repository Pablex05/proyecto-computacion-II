import socket, sys, os, time, getopt

if __name__ == "__main__":
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print("Error al crear socket de server")
        sys.exit()
    host = "" 
    puerto = "" 
    f = ""
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:a:', ["puerto", "host"])

    for(op, ar) in opt:
        if op == '-p':
            puerto = int(ar) 
        elif op == '-a':
            host = str(ar) 
    print("Conectando a server")
    clientsocket.connect((host, puerto))
    mensaje = []
    print("Ingrese un mensaje:")
    while True:
        try:
            mensaje.append(input().encode("ascii"))
        except EOFError:
            mensaje.append(("--").encode("ascii"))
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
