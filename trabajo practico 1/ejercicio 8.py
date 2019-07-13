

import os,time,signal

def handler(s,f):
    print("\t")
def hijo1():
    while True:
        print("Soy el proceso hijo1 con PID= %d: ping" % (os.getpid()))
        time.sleep(5)
        os.kill(pid2, signal.SIGUSR1)
        signal.pause()

def hijo2():
    while True:
        print("Soy el proceso hijo2 con PID= %d: pong" % (os.getpid()))
        os.kill(pid1, signal.SIGUSR1)
        signal.pause()
        time.sleep(5)

signal.signal(signal.SIGUSR1,handler)
pid1=os.fork()
pid2=os.fork()

if pid1 == 0:
    hijo1()
elif pid2 == 0:
    hijo2()
else:
    print("Iniciando padre")
    while True:
        os.kill(pid1, signal.SIGUSR1)
        time.sleep(5)
