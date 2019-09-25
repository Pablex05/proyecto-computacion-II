"""
Escribir un programa que lance dos procesos hijos (fork).
Uno de los procesos hijos se encargará de leer desde la entrada estándar líneas de
texto, y en la medida en que el usuario escriba, el proceso las irá enviando por un pipe
que compartirá con el otro proceso hijo.
El segundo proceso se encargará de leer desde el pipe las líneas que el primer proceso
escriba, y las irá mostrando por pantalla en el formato “Leyendo (pid: 1234):
mensaje”, donde 1234 es el pid de este segundo proceso, y “mensaje” es el contenido
leído desde el pipe.
"""

import os, time, sys, multiprocessing, pipes

def proceso():
    global line
    r, w = os.pipe()
    pid1 = os.fork()
    if pid1:
        print("******************PROCESO PADRE*****************")
    if pid1==0:
        os.close(r)
        w = os.fdopen(w,'w')
        print("------------escribir mensaje---------------")
        for line in sys.stdin:
            w.write("%s" % line)
            w.flush()
        sys.exit(0)
    pid2 = os.fork()
    if pid2==0:
        time.sleep(3)
        os.close(w)
        r = os.fdopen(r)
        for line in r:
            os.getpid()
            print("\nleyendo %d: %s " % (os.getpid(),line))
            print("------------escribir mensaje---------------")
        sys.exit(0)
    os.wait()
    os.wait()
proceso()