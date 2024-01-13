import multiprocessing

def calculate_sum_of_squares(start, end, result_queue):
    result = 0
    for i in range(start, end + 1):
        result += i * i
    result_queue.put(result)

def main():
    start_range = 1
    end_range = 2
    num_processes = multiprocessing.cpu_count()

    processes = []
    result_queue = multiprocessing.Queue()

    for i in range(num_processes):
        process = multiprocessing.Process(target=calculate_sum_of_squares, args=(start_range, end_range, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Retrieve partial results from the queue and calculate the final result
    final_result = 0
    while not result_queue.empty():
        final_result += result_queue.get()

    print(f"Sum of squares from {start_range} to {end_range}: {final_result}")

if __name__ == "__main__":
    main()
