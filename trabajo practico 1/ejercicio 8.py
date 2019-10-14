
import os, time, sys, multiprocessing, pipes, signal
from multiprocessing import Pipe, Process, Pool

def handler(s,f):
    return
signal.signal(signal.SIGUSR1,handler)
def hijo1(pid):
    while True:
        print('==========================================')
        print('Soy proceso Hijo 1 con PID=%s: "ping" ' %(os.getpid()))
        os.kill(pid,signal.SIGUSR1)
        time.sleep(5)
def hijo2():
    while True:
        print('Soy proceso Hijo 2 con PID=%s: "pong" ' %(os.getpid()))
        print('==========================================')
        signal.pause()
pid = os.getpid()
p1 = Process(target=hijo1, args=(pid,))
p2 = Process(target=hijo2)
p1.start()
p2.start()
while True:
    os.kill(p2.pid, signal.SIGUSR1)
    signal.pause()