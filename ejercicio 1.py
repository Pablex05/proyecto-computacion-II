import getopt
import sys

(opt,arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')
"""
print("opciones: ", opt)
print("argumentos: ", arg)
"""


for (op,ar) in opt:

    if (op == '-o'):
        if (ar == '+'):
            print("El operador: ", ar)
            operador = ar
        elif (ar == '-'):
            print("El operador: ", ar)
            operador = ar
        elif (ar == '*'):
            print("El operador: ", ar)
            operador = ar
        elif (ar == '/'):
            print("El operador:", ar)
            operador = ar
    if (op == '-n'):
        print("El numero: ", ar)
        num1 = ar
    if (op == '-m'):
        print("El numero: ", ar)
        num2 = ar
try:
    if (operador == '+'):
        total = int(num1) + int(num2)
        print(num1, "+", num2, "=", total)
    elif (operador == '-'):
        total = int(num1) - int(num2)
        print(num1, "-", num2, "=", total)
    elif (operador == '*'):
        total = int(num1) * int(num2)
        print(num1, "*", num2, "=", total)
    elif (operador == '/'):
        total = int(num1) / int(num2)
        print(num1, "/", num2, "=", total)
except:
    print("*****ELEMENTO NO VALIDO*******")


