#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:54:18 2022

@author: Jesús Parera
"""
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import Lock
N = 8
def task(common,l, tid):
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        l.acquire()
        try:
            print(f'{tid}−{i}: End of non−critical Section')
            print(f'{tid}−{i}: Critical section')
            v = common.value + 1
            print(f'{tid}−{i}: Inside critical section')
            common.value = v
        finally:
            l.release()
        print(f'{tid}−{i}: End of critical section')
        
def main():
    lock = Lock()
    common = Value('i', 0)
    lp = []
    for tid in range(N):
        lp.append(Process(target=task, args=(common,lock, tid)))
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")
if __name__ == "__main__":
    main()