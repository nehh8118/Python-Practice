''' 
process: program in execution, heavy weight, slower
threads: a unit of process, lightweight, limited to only one thread at a time, race conditions, GIL
GIL: lock than allows only one thread to perform at a time
'''
from multiprocessing import process
import os
import time

def squareNum():
    for i in range(100):
        i*i
        time.sleep(0.1)

processess = []
num_processes = os.cpu_count()

#create process
for i in range(num_processes):
    p = Process(target=squareNum)
    processess.append(p)

for p in processess:
    p.start()

for p in processess:
    p.join() #blockign the main thread until all processes are done
