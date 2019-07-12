import os, time

def hijo():
    for x in range(5):
        print("soy el hijo")
        time.sleep(1)
    os._exit(0)
def padre():
    for a in range(2):
        print("soy el padre")
        time.sleep(1)

def proceso():
    ret=os.fork()
    if ret==0:
        hijo()
    padre()
    os.wait()
    print("mi proceso hijo termino")
proceso()