from threading import Thread , Lock
import time 

database_value = 0

# add lock method to update global variable sequentially 
def increase(lock):
    global database_value
    # lock certain process until complete other threads will not execute until lock release
    with lock :
        local_copy = database_value
        local_copy += 1
        time.sleep(1)
        database_value = local_copy

if __name__=='__main__':

    lock = Lock()
    print("start value : ", database_value)

    #define two threads
    thread1 = Thread(target=increase , args=(lock,))
    thread2 = Thread(target=increase , args=(lock,))

    # start two threads
    thread1.start()
    thread2.start()

    # wait for the threads
    thread1.join()
    thread2.join()

    # main thread
    print("end value : ", database_value)
