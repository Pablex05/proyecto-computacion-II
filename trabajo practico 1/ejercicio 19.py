import os, time, sys, multiprocessing, pipes, signal
from multiprocessing import Pipe, Process, Pool

def hijo(i):
    i = i + 1
    q.put("PID: %d \t" % (os.getpid()))
    print("Proceso %d, PID: %d" % (i, os.getpid()))
    time.sleep(i)

q = multiprocessing.Queue()
pool = Pool(processes=10)

if __name__ == "__main__":
    print("---------creando hijos-----------")
    results = pool.map(hijo, range(10))
    print("---------mostrando lista-----------")
    for x in range(10):
        print("\t" + q.get())

