import os, time

def hijo():
    print("************ HIJO ****************")
    print("la PID del padre: %d,\n la PID del hijo: %d\n" % (os.getppid(), os.getpid()))
    time.sleep(1)
    os._exit(0)

def padre():
    time.sleep(1)
    os._exit(0)

def proceso():
    for x in range (3):
        pid = os.fork()
        if pid == 0:
            hijo()
    padre()

proceso()