import signal, time

def handler(signum, frame):
    print('Esta vez me saldré, inténtalo nuevamente)'+str(signum)+"-"+ str(frame))
    signal.signal(signal.SIGINT, signal.SIG_DFL)

print(signal.getsignal(signal.SIGINT))
signal.signal(signal.SIGINT, handler)
print(signal.getsignal(signal.SIGINT))

time.sleep(100)

