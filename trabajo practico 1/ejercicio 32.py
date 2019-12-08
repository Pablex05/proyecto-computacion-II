from concurrent.futures import ProcessPoolExecutor
import sys, getopt, time

def fib_iter(n):
    a = 1
    b = 0
    for j in range(n):
        a, b = b, a + b
    return b

def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

if __name__=="__main__":
    print("Iniciando programa")
    num = int()
    mun = int()
    (opt, arg) = getopt.getopt(sys.argv[1:], 'n:m:', ["N", "M"])
    for (op, ar) in opt:
        if op == '-n':
            num = int(ar)
        elif op == '-m':
            mun = int(ar)
    num2 = num
    mun2 = mun
    resta = int(mun - num)
    pool = ProcessPoolExecutor(resta)
    print("---------------------Iterativo:--------------------")
    t_ini_it = time.time()
    while num < mun:
        for i in range(num):
            future = pool.submit(fib_iter, num)
        num += 1
        print(future.result(), end='\t')
    t_fin_it = time.time()
    t_ejec_it = t_fin_it - t_ini_it
    print("\n \n--Tiempo de iteración: ", t_ejec_it)
    print('')
    print("---------------------Recursivo:--------------------")
    t_ini_re = time.time()
    while num2 < mun2:
        for i in range(num2):
            future = pool.submit(fib_rec, num2)
        num2 += 1
        print(future.result(), end='\t')
    t_fin_re = time.time()
    t_ejec_re = t_fin_re - t_ini_re
    print("\n \n--Tiempo de recursion: ", t_ejec_re)