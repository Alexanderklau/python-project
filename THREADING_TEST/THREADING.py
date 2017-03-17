# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import threading
import time
import random
def work_func():
    print('worker thread is %s' % threading.current_thread())
    random.seed()
    time.sleep(random.random())
    print('worker finished at %s' % threading.current_thread())
# def simple_thread_done():
#     for i in range(10):
#         threading.Thread(target=work_func()).start()
def worker_func_loop(lock):
    lock.acquire()
    work_func()
    lock.release()
gLock = threading.Lock()

def thread_worker():
    for i in range(10):
        threading.Thread(target=worker_func_loop,args=[gLock]).start()
if __name__ == '__main__':
    thread_worker()
    # worker_func_loop()