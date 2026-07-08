# Objective: Stop an ongoing execution prematurely by triggering a cancellation exception.
import asyncio
from time import ctime

async def background_loop():
    try:
        print(f"{ctime()} Worker: Starting long infinite process...")
        while True:
            await asyncio.sleep(1)
            print(f"{ctime()} Worker: Still ticking...")
    except asyncio.CancelledError:
        # Injected cancellation exception will be caught here, allowing for clean-up logic before exiting
        print(f"{ctime()} Worker: Interrupted! Executing clean-up logic before exit...")

async def main():
    task = asyncio.create_task(background_loop())
    await asyncio.sleep(2.5) # Let the background task run for a bit
    
    print(f"{ctime()} Main: Changing plans, canceling the worker task now!")
    task.cancel() # Inject the cancellation exception
    await asyncio.sleep(0.1) # Allow time for the cancellation to be processed

asyncio.run(main())