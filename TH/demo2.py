# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
# 带锁线程
import threading
import time
import random
def worker_func():
    print('Worker thread is started at %s' %threading.current_thread())
    random.seed()
    time.sleep(random.random())
    print('Worker thread is finished at %s' % threading.current_thread())


def simple_thread_demo():
    for i in range( 10):
        threading.Thread(target=worker_func).start()#创建一个线程，target就是调用工作函数worker_func

def worker_func_lock(lock):
    lock.acquire()
    worker_func()
    lock.release()
gLock = threading.Lock()
gSem = threading.Semaphore(3)
def thread_demo_lock():
    for i in range(1,10):
        threading.Thread(target=worker_func_lock,args=[gSem]).start()

if __name__ == '__main__':
    thread_demo_lock()
    # simple_thread_demo()








# if __name__ == '__main__':