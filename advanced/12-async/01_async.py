import asyncio

async def main():
    # register async task
    task = asyncio.create_task(print_num())
    print("A")
    # blocker so call print_num()
    await asyncio.sleep(1)
    print("B")
    output = await task
    print(output)

async def print_num():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return "Hello"

if __name__ == "__main__":
    asyncio.run(main())

"""
A
1
B
2
Hello
"""
