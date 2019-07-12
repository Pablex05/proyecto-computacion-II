import getopt
import sys
import os

(opt,arg) = getopt.getopt(sys.argv[1:], 'i:o:')

for (op,ar) in opt:
    if op in['-i']:
        operador1 = ar
    if (op == '-o'):
        operador2 = ar
try:
    f1=open(operador1,'r')
except:
    print("*****ARCHIVO NO VALIDO entrada*******")
    os._exit(0)
try:
    f2=open(operador2,'w+')
except:
    print("*****ARCHIVO NO VALIDO salida*******")
    os._exit(0)
for variable in f1:
    try:
        variable = f1.readline()
    except:
        break
    f2.write(variable)
f1.close()
f2.close()