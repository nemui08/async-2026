# Objective: Label task objects explicitly to simplify logging and production tracking.
import asyncio
from time import ctime

async def background_worker():
    await asyncio.sleep(0.1)

async def main():
    task = asyncio.create_task(background_worker())
    
    # Default name is auto-generated based on the function name and a unique identifier
    print(f"{ctime()} Initial Name: {task.get_name()}") # Expected output Task-2

    # Explicitly set a custom name for the task
    task.set_name("Payment-Gateway-Validator")
    print(f"{ctime()} Updated Name: {task.get_name()}") # Expected output: Payment-Gateway-Validator

asyncio.run(main())