import os,sys,time, getopt

fifo = '/tmp/mififo'
if not os.path.exists(fifo):
    os.mkfifo(fifo)
fifo_fd = open(fifo, 'w')
fifo_fd.write(sys.argv[1])
