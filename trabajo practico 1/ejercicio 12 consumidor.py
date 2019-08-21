import os, time, sys


pipe_name = '/tmp/mififo'
pipein = open(pipe_name, 'r')
lectura = pipein.readline()

r, w = os.pipe()
pid = os.fork()
if pid:
    os.close(r)
    w = os.fdopen(w,"w")

    w.write(lectura)
    w.close()
    os.wait()

else:
    time.sleep(1)
    os.close(w)
    r = os.fdopen(r)
    print(" mensaje: %s" % r.readline())
    r.close()
    sys.exit(0)