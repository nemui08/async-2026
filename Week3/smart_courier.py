# Delivery System): นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง 
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้
import asyncio
from time import ctime

async def deliver_task(package_id, duration):
    try:
        print(f"{ctime()} Courier started delivering package {package_id}...")
        await asyncio.sleep(duration)
        print(f"{ctime()} Package {package_id}: Successfully delivered!")
    except asyncio.CancelledError:
        print(f"{ctime()} Package {package_id}: Delivery Canceled! Returning package to warehouse...")
        raise  

async def main():
    task = asyncio.create_task(deliver_task("P001", 5))
    task.set_name("DeliveryTask-P001")

    await asyncio.sleep(2)  # Let the delivery task run for a bit

    print(f"{ctime()} Checking task 'Express-Courier'.Is it done? {task.cancelled()}")

    if not task.done():
        print(f"{ctime()} Package {task.get_name()}: Taking too long! canceling the task...")
        task.cancel()  # Trigger cancellation
    
    try:
        await task  # Await the task to handle cancellation properly
    except asyncio.CancelledError:
        print(f"{ctime()} Final verify: Is task officially canceled? {task.cancelled()}")
    
if __name__ == "__main__":
    asyncio.run(main())