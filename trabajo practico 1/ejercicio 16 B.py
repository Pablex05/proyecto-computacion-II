import os, time, sys, multiprocessing, pipes, signal
from multiprocessing import Pipe, Process


fifo = '/tmp/mififo'
if not os.path.exists(fifo):
    os.mkfifo(fifo)
r = open(fifo, 'r')
while True:
    print("-----------------mensaje--------------------")
    r = open(fifo, 'r')
    lectura = r.readline()
    print("AA: %s" % lectura)
    r.close()
    print("------------escribir mensaje---------------")
    w = open(fifo, 'w')
    x = sys.stdin.readline()
    w.write(x)
    w.flush()
    w.close()




