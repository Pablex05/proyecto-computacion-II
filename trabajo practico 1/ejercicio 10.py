import os, time, signal

def handler(s, f):
    print(" ", s, f)

signal.signal(signal.SIGUSR1, handler)
signal.signal(signal.SIGUSR2, handler)
r, w = os.pipe()
proceso_b = os.fork()
if proceso_b:
    time.sleep(1)
    os.kill(proceso_b, signal.SIGUSR2)
    signal.pause()
    os.close(w)
    r = os.fdopen(r)
    print("\n A (PID=%s) leyendo: " % os.getpid())
    for line in r:
        print("%s" % line)
    r.close()
    time.sleep(5)
else:
    print("=========PROCESO ABUELO A========")
    os.close(r)
    w = os.fdopen(w, 'w')
    signal.pause()
    pidA = os.getppid()
    proceso_c = os.fork()
    if proceso_c:
        print("=========PROCESO PADRE B=======")
        w.write("Mensaje 1 PID:%s \n" % os.getpid())
        w.flush()
        w.close()
        os.kill(pidA, signal.SIGUSR2)
        time.sleep(1)
    else:
        print("==========PROCESO NIETO C ========")
        w.write("Mensaje 2 PID:%s \n" % os.getpid())
        w.flush()
        w.close()
        os.kill(pidA, signal.SIGUSR1)
        time.sleep(1)
