import os, time, sys, multiprocessing, pipes
from multiprocessing import Process, Pipe

def f(a):
    while True:
        print("\nleyendo %d: %s " % (os.getpid(),a.recv()))
        print("------------escribir mensaje---------------")

if __name__ == '__main__':
    global line
    a, b = Pipe()
    print("------------escribir mensaje---------------")
    while True:
        for line in sys.stdin:
            p = Process(target=f, args=(a,))
            p.start()
            print("------------escribir mensaje---------------")
            b.send("%s" % line)
    p.join()
