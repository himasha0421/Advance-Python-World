from threading import Thread , Lock  , current_thread
import time 
from queue import Queue

"""
using queue we can exchange data between threads in 
thread safe enviroment
"""

def worker(q,lock):
    while True :
        value = q.get()
        with lock :
            # do some processing
            print(f'{current_thread().name} got {value}')
        q.task_done()


if __name__=='__main__':

    q= Queue()
    lock = Lock()

    num_threads = 10 

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        # background threads dies when main thread dies
        thread.daemon = True
        thread.start()

    for i in range(1,21):
        q.put(i)

    q.join()

    print("end main")
