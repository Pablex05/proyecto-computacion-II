import getopt, sys, os, time, math
from multiprocessing import Pool

def raiz(n):
    if (n % 2 != 0):
        raiz = math.sqrt(n)
        print('LA RAIZ DEL ', n, 'ES:', raiz)

(opt,arg) = getopt.getopt(sys.argv[1:], 'n:m:')

n = ""
m = ""
for (op,ar) in opt:
    if (op == '-n'):
        n = int(ar)
    elif (op == '-m'):
        m = int(ar)
    else:
        print('************PARAMETROS INCORRECTOS*************')

pool = Pool()
pool.map(raiz, range(n, m, 1))