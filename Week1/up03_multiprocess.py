from time import sleep, ctime, time
import os
import threading
import multiprocessing

def update_cup_number(customer_name):
    pid = os.getpid()
    thread_name = threading.current_thread().name

    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1) # Simulate time taken to update cup number
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    pid = os.getpid()
    thread_name = threading.current_thread().name

    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1) # Simulate time taken to make coffee
    print(f"{ctime()} | Coffee ready for {customer_name}!")

    update_cup_number(customer_name) # Update cup number after making coffee

def main():
    queue = ['A', 'B', 'C']
    start_time = time()

    print(f"{ctime()} | === Multi-processing Coffee Machine ===")

    processes = []
    for customer in queue:
        p = multiprocessing.Process(target=make_coffee, args=(customer,), name=f"Process-{customer}")
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"{ctime()} | Total Time: {duration:.2f} seconds")

if __name__ == "__main__":
    main()