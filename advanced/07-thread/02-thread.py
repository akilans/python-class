import concurrent.futures
import time

# Instead of create and start thread
# use concurrent.futures threadpool


def do_something(seconds):
    print(f"Sleeping for {seconds} second")
    time.sleep(seconds)
    print("Doing work...")
    print("Done sleeping...")


before = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    # create 10 threads
    results = [executor.submit(do_something, 2) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        f.result()
after = time.perf_counter()
print(
    f"Efficient Thread asynchronus way took {round(after - before,2)} seconds")


before = time.perf_counter()
seconds_list = [5, 4, 3, 2, 1]
with concurrent.futures.ThreadPoolExecutor() as executor:
    # create 5 threads length of seconds list
    results = [executor.submit(do_something, sec)
               for sec in seconds_list]

    for f in concurrent.futures.as_completed(results):
        f.result()
after = time.perf_counter()
print(
    f"Efficient Thread asynchronus way took {round(after - before,2)} seconds")
