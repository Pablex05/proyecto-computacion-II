import os, time, sys, multiprocessing, pipes, signal
from multiprocessing import Pipe, Process


fifo = '/tmp/mififo'
if not os.path.exists(fifo):
    os.mkfifo(fifo)
print("------------escribir mensaje---------------")
w = open(fifo, 'w')
for x in sys.stdin:
    w = open(fifo, 'w')
    w.write(x)
    w.flush()
    w.close()
    r = open(fifo, 'r')
    print("-----------------mensaje--------------------")
    lectura = r.readline()
    print("BB: %s" % lectura)
    r.close()
    print("------------escribir mensaje---------------")








