# Single process creates multiple threads
# After running check task manger
# Only one python process
import threading, time
my_th1_name = "" 
my_th2_name = "" 

# This function takes 10 seconds to run
def func1():
    global my_th1_name
    my_th1_name = "THREAD1"
    print(f"My name is {my_th1_name}")
    time.sleep(10)
    print("Function 1 done")

# This function runs immediately
def func2():
    global my_th2_name
    my_th2_name = "THREAD2"
    print(f"My name is {my_th2_name}")
    time.sleep(3)
    print("Function 2 done")



# call with thread
thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)

# start threads
thread1.start()
thread2.start()

# wait for threads to end
thread1.join()
thread2.join()

# any changes in the global variable reflects
# As it shares the memory
print(f"Thread 1 name is {my_th1_name}")
print(f"Thread 2 name is {my_th2_name}")

'''
Output
My name is THREAD1
My name is THREAD2
Function 2 done
Function 1 done
Thread 1 name is THREAD1
Thread 2 name is THREAD2
'''