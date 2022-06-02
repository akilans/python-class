import threading
import time


def do_something():
    print("Sleeping for 1 second")
    time.sleep(1)
    print("Doing work...")
    print("Done sleeping...")

# Method 1


# Normal way - synchronous
before = time.perf_counter()
do_something()
do_something()
do_something()
after = time.perf_counter()
print(f"Normal synchronus way took {round(after - before,2)} seconds")


# Method 2
# Use thread - Asynchronous
before = time.perf_counter()
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t3 = threading.Thread(target=do_something)

# Start thread
t1.start()
t2.start()
t3.start()

# Wait for thread to complete
t1.join()
t2.join()
t3.join()
after = time.perf_counter()
print(f"Thread asynchronus way took {round(after - before,2)} seconds")


# Method 3
before = time.perf_counter()
threads = []

for _ in range(3):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

after = time.perf_counter()
print(
    f"Efficient Thread asynchronus way took {round(after - before,2)} seconds")
