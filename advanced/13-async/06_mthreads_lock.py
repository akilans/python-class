import threading, time
from threading import Lock, Thread

balance = 0

def deposit(l: Lock):
    global balance
    # act like some process is happening   
    # l.acquire()
    # local_balance = balance
    # local_balance += 1
    # time.sleep(0.1)
    # balance = local_balance
    # l.release()

    # with context manager
    # l.acquire() and l.release() are not needed
    with l:
        local_balance = balance
        local_balance += 1
        time.sleep(0.1)
        balance = local_balance


def main():
    lock = Lock()

    t1 = Thread(target=deposit,args=(lock,))
    t2 = Thread(target=deposit,args=(lock,))
    t3 = Thread(target=deposit,args=(lock,))

    # start all threads
    t1.start()
    t2.start()
    t3.start()

    # join all threads so main thread waits for these to end
    t1.join()
    t2.join()
    t3.join()

    print(f"Main thread Ends. Balance - {balance}")


if __name__ == "__main__":
    main()

