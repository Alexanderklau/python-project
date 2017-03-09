# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
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






if __name__ == '__main__':
    simple_thread_demo()