from multiprocessing import Process, Pipe, Lock
import threading
import time

def hijo(elemento):
   print("el mensaje recibido es: %s" % elemento.recv())
   elemento.close()

pipe_name = '/tmp/mififo'
pipein = open(pipe_name, 'r')
lectura = pipein.readline()
lock = threading.Lock()
r, w = Pipe()
p = threading.Thread(target=hijo, args=(r,))
p.start()
w.send(lectura)
w.close()
p.join()