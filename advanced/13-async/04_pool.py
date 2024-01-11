from multiprocessing import Pool
import time

def my_fun(n):
    time.sleep(10)
    return n**2


def main():
    p = Pool()
    num_list = [1,2,3,4,5]
    result = p.map(my_fun,num_list) # it creates 5 process
    print(result)

if __name__ == "__main__":
    main()