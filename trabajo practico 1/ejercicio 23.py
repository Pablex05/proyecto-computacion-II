import os, time, sys, pipes, signal, threading, multiprocessing
from multiprocessing import Process, Lock

def hijo(i):
    q.put("PID: %d \t" % (os.getpid()))
    print("Proceso %d, PID: %d del hijo %d" % (i, os.getpid(),threading.current_thread()._ident))
    time.sleep(i)
    sys.exit(0)

q = multiprocessing.Queue()
i = 0
if __name__ == "__main__":
    p = []
    for x in range(10):
        i = i + 1
        p.append(threading.Thread(target=hijo, args=(i,)))
    print("---------creando hijos-----------")
    for x in range(10):
        p[x].start()
    for x in range(10):
        p[x].join()
    print("---------mostrando lista-----------")
    for x in range(10):
        print("\t" + q.get())
