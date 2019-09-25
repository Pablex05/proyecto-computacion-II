import os, time, sys, multiprocessing, pipes, signal

def hijo(i):

    print("hijo %s = %d" % (i,  os.getpid()))
    time.sleep(1)


if __name__ == "__main__":

    p1 = multiprocessing.Process(target=hijo, args=(1,))
    p2 = multiprocessing.Process(target=hijo, args=(2,))
    p3 = multiprocessing.Process(target=hijo, args=(3,))
    print("========================================================")
    print("Parent ID", os.getppid())
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

