# coding=utf-8
import os,time,signal

def handler(s,f):
    print("\nhijo recibio la señal...\n")

def hijo():
    print("Iniciando hijo")
    while True:
        print("Hijo esperando...")
        signal.pause()

def proceso():
    signal.signal(signal.SIGUSR1, handler)
    pid = os.fork()
    if pid == 0:
        hijo()
    else:
        print("Iniciando padre")
        x=0
        while (x==0):
            os.kill(pid, signal.SIGUSR1)
            time.sleep(5)
            if (x!=0):
                break

        print("Padre matando al hijo...")
        os.kill(pid, signal.SIGTERM)
        print("Padre terminando...")

proceso()
