import threading, time

balance = 0

def deposit():
    global balance
    # act like some process is happening
    local_balance = balance
    local_balance += 1
    time.sleep(0.1)
    balance = local_balance

def main():

    t1 = threading.Thread(target=deposit)
    t2 = threading.Thread(target=deposit)
    t3 = threading.Thread(target=deposit)

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


'''
Expected 
Main thread Ends. Balance - 3
Because all threads are updating same value
Output
Main thread Ends. Balance - 1
'''