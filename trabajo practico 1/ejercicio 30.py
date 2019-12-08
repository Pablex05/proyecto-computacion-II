import getopt
import os, time, sys, multiprocessing
from multiprocessing import Lock

def hijo(i,arch,l,iter):
    lista = ["","A","B","C","D","E","F","G","H","I","J","K","M","N","O","P"]
    print("Proceso %d, PID: %d letra %s" % (i, os.getpid(), lista[i]))
    for x in range(iter):
        arch.write(lista[i])
        time.sleep(1)
    arch.close()
    sys.exit(0)

i = 0
if __name__ == "__main__":
    p = []
    lock = Lock()
    (opt, arg) = getopt.getopt(sys.argv[1:], 'r:f:')
    for (op, ar) in opt:
        if op == '-r':
            iteraciones = int(ar)
        if op == '-f':
            archivo = str(ar)
    f = open(archivo, 'w+')
    lock.acquire()
    for x in range(15):
        i = i + 1
        p.append(multiprocessing.Process(target=hijo, args=(i,f,lock,iteraciones)))
    print("---------creando hijos-----------")
    for x in range(15):
        p[x].start()
    lock.release()
    for x in range(15):
        p[x].join()
