from time import sleep, ctime, time
import os
import threading
import asyncio

async def update_cup_number(customer_name):
    pid = os.getpid()
    thread_name = threading.current_thread().name

    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1) # Simulate time taken to update cup number
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

async def make_coffee(customer_name):
    pid = os.getpid()
    thread_name = threading.current_thread().name

    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1) # Simulate time taken to make coffee
    print(f"{ctime()} | Coffee ready for {customer_name}!")

    await update_cup_number(customer_name) # Update cup number after making coffee

async def main():
    queue = ['A', 'B', 'C']
    start_time = time()

    print(f"{ctime()} | === Asyncio Coffee Machine ===")

    tasks = []
    for customer in queue:
        coro = make_coffee(customer)
        task = asyncio.create_task(coro, name=f"Task-{customer}")
        tasks.append(task)

    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} | Total Time: {duration:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())