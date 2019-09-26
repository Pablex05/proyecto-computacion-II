import os, time, sys, multiprocessing, pipes, signal
from multiprocessing import Pipe, Process


q = multiprocessing.Queue()

print("---------creando hijos-----------")
i = 0
for x in range(10):
    pid = os.fork()
    i=i+1

    if pid == 0:
        q.put("PID: %d \t" %(os.getpid()))
        print("Proceso %d, PID: %d" %(i,os.getpid()))
        time.sleep(i)
        sys.exit(0)
for x in range(10):
    os.wait()
print("----------mostrando cola----------")
for x in range(10):
    print("\t" + q.get())