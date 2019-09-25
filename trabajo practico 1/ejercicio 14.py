import os, time, sys, multiprocessing, pipes
from multiprocessing import Process, Pipe

def proceso():
    global line
    r, w = os.pipe()
    pid1 = os.fork()
    if pid1:
        print("******************PROCESO PADRE*****************")
        pid2 = os.fork()
        if pid2 == 0:
            time.sleep(3)
            os.close(w)
            r = os.fdopen(r)
            for line in r:
                os.getpid()
                print("\nleyendo %d: %s " % (os.getpid(), line))
                print("------------escribir mensaje---------------")
            sys.exit(0)
    if pid1==0:
        os.close(r)
        w = os.fdopen(w,'w')
        print("------------escribir mensaje---------------")
        for line in sys.stdin:
            w.write("%s" % line)
            w.flush()
        sys.exit(0)
    os.wait()
    os.wait()
proceso()

def f(a):
    for line in r:
        print("\nleyendo %d: %s " % (a.recv(), line))
        print("------------escribir mensaje---------------")
    sys.exit(0)

if __name__ == '__main__':
    global line
    a, b = Pipe()
    p = Process(target=f, args=(a,))
    p.start()
    for line in sys.stdin:
        print("------------escribir mensaje---------------")
        b.send("%s" % line)
    sys.exit(0)

