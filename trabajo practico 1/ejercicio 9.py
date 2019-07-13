import os,time,signal

def handler(s,f):
    print("Soy el proceso PID %d recibi la señal %s de mi padre %d" % (os.getpid(), s, os.getppid()))
def hijo1():
    print("Soy el proceso Hijo %d " % os.getppid())
def proceso():
    signal.signal(signal.SIGUSR1, handler)
    pid = os.fork()
    if pid == 0:
        signal.pause()
        os._exit(0)
    pid1 = os.fork()
    if pid1 == 0:
        signal.pause()
        os._exit(0)
    pid2 = os.fork()
    if pid2 == 0:
        signal.pause()
        os._exit(0)
    os.kill(pid, signal.SIGUSR1)
    os.kill(pid1, signal.SIGUSR1)
    os.kill(pid2, signal.SIGUSR1)
    signal.signal(signal.SIGUSR1, handler)
    time.sleep(5)
proceso()
