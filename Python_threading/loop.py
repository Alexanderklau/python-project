import threading
from time import sleep,ctime

loops = (4,2)

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)

    def loop(nloop,nsec):
        print('Start loop',nloop,'at:',ctime())
        sleep(nsec)
        print('loop',nloop,'done at:',ctime())

    def main():
        print('Starting at:',ctime())
        threads = []
        nloops = range(len(loops))

