''' 
process: program in execution, heavy weight, slower
threads: a unit of process, lightweight, limited to only one thread at a time, race conditions, GIL
GIL: lock than allows only one thread to perform at a time
'''
from threading import Thread
import os
import time

def squareNum():
    for i in range(100):
        i*i
        time.sleep(0.1)

threads = []
num_threads = 10

#create thread
for i in range(num_threads):
    p = Thread(target=squareNum) #specify args if arguments exist
    threads.append(p)

for t in threads:
    t.start()

for t in threads:
    t.join() #blockign the main thread until all processes are done
