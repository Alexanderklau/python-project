import threading
from time import sleep,ctime

def loop():
    print('Start loop 0 at:',ctime())
    sleep(4)
    print('loop 0 done at:',ctime())

def loop1():
    print('Start loop 1 at:',ctime())
    sleep(2)
    print('loop 1 done at:',ctime())
def main():
    print('Starting at:',ctime())
    threading._start_new_thread(loop,())
    threading._start_new_thread(loop1,())
    sleep(6)
    print('all Done at:' ,ctime())

if __name__ == '__main__':
    main()