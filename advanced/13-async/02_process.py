# Create 3 process one for main python script
# one for process1 & another one for process2
# Check in task manager
import multiprocessing, time
my_ps1_name = "" 
my_ps2_name = "" 


# This function takes 10 seconds to run
def func1():
    global my_ps1_name
    my_ps1_name = "Process1"
    print(f"My name is {my_ps1_name}")
    time.sleep(10)
    print("Function 1 done")

# This function runs immediately
def func2():
    global my_ps2_name
    my_ps2_name = "Process2"
    print(f"My name is {my_ps2_name}")
    time.sleep(5)
    print("Function 2 done")


# call with process
process1 = multiprocessing.Process(target=func1)
process2 = multiprocessing.Process(target=func2)

# start processs
process1.start()
process2.start()

# wait for processs to end
process1.join()
process2.join()


# any changes in the global variable will not reflect
# As it will not share the memory
# to share the data between process you need to use IPC (Inter Process Communication)
print(f"Process 1 name is {my_ps1_name}")
print(f"Process 2 name is {my_ps2_name}")


'''
Output
My name is Process1
My name is Process2
Function 2 done
Function 1 done
Process 1 name is 
Process 2 name is 
'''