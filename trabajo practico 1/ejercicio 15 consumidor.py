from multiprocessing import Process, Pipe

def hijo(elemento):
   print("el mensaje recibido es: %s" % elemento.recv())
   elemento.close()

pipe_name = '/tmp/mififo'
pipein = open(pipe_name, 'r')
lectura = pipein.readline()
r, w = Pipe()
p = Process(target=hijo, args=(r,))
p.start()
r.close()
w.send(lectura)
w.close()
p.join()


