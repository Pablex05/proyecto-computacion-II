
import os

def proceso():

    n = int(input("ingrese un valor entero: "))
    ret = os.fork()
    if ret==0:
        valor = n
        total = int(valor) - 2
        print("el total de ", int(valor), "es: ", int(total))
        os._exit(0)
    valor = n
    total = int(valor) + 4
    print("el total de ", int(valor), "es: ", int(total))
    os.wait()
proceso()
