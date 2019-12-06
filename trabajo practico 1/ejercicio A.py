import socket, sys, os, time
from multiprocessing import Pool
import random, secrets, string

def generarMensaje():
    aver = secrets.token_bytes(128)
    randmsg = ''.join(random.choices(string.ascii_uppercase + string.digits, k=len(aver)))
    return randmsg
def hijo(num):
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = sys.argv[1]
        port = int(sys.argv[2])
        clientsocket.connect((host, port))
        for x in range(100):
            msg = generarMensaje()
            clientsocket.sendto(msg.encode("ascii"), (host, port))
        fin = str("exit")
        clientsocket.sendto(fin.encode("ascii"), (host, port))
        clientsocket.close()
        print("success")
        # return 1
    except:
        print("error")
        # return 0

if __name__ == "__main__":
    t_ini = time.time()
    pool = Pool(processes=20)
    rango = range(1, 20)
    pool.map(hijo, rango)
    pool.terminate()
    t_fin = time.time()
    t_ejec = t_fin - t_ini
    print("tiempo de ejecución: ", t_ejec)