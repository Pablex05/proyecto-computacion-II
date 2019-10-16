import os, time, sys, pipes, signal, threading, multiprocessing
from multiprocessing import Process, Lock


def hijo(l):

    print("hijo %s = %d del hilo %d" % (l,  os.getpid(), threading.current_thread()._ident))
    time.sleep(1)



if __name__ == "__main__":
    lock = threading.Lock()
    p1 = threading.Thread(target=hijo, args=(1,))
    p2 = threading.Thread(target=hijo, args=(2,))
    p3 = threading.Thread(target=hijo, args=(3,))
    print("========================================================")
    print("Padre ID:", os.getppid())
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()