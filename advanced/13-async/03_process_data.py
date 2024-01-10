
import multiprocessing, time
my_ps1_name = ""  


# This function takes 10 seconds to run
def func1(result_array,double_value):
    for i in range(3):
        result_array[i] = i+1
    double_value.value = 2.0
    #string_value.value = "Hello Akilan"

    time.sleep(2)
    print("Function 1 done")


# call with process
result_array = multiprocessing.Array('i',3)
double_value = multiprocessing.Value('d',1.0)
#string_value = multiprocessing.Value('c_char_p',"Hello")
process1 = multiprocessing.Process(target=func1,args=(result_array,double_value))
# start processs
process1.start()

# wait for processs to end
process1.join()

# share data between main process and child process
print(f"result_array -> {result_array[:]} - double_value ->{double_value.value}")


'''
Output
My name is Process1
My name is Process2
Function 2 done
Function 1 done
Process 1 name is 
Process 2 name is 
'''