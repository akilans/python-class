import asyncio
import random

async def main():
    print_num_tasks = []
    for num in range(1, 6):
        print_num_tasks.append(print_num(num))
    # # gathering func [call print_num 5 times]
    await asyncio.gather(*print_num_tasks)

async def print_num(num):
    # waiting some rand seconds
    wait_time = random.randint(1, 5)
    print(f"{num} - Waitng for {wait_time} seconds...")
    await asyncio.sleep(wait_time)
    print(f"Number - {num}")

if __name__ == "__main__":
    asyncio.run(main())

"""
1 - Waitng for 3 seconds...
2 - Waitng for 5 seconds...
3 - Waitng for 5 seconds...
4 - Waitng for 3 seconds...
5 - Waitng for 5 seconds...
Number - 1
Number - 4
Number - 2
Number - 3
Number - 5
"""
