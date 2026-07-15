import asyncio
from time import ctime, time
from light_utils import control_light

async def main():
    MY_STUDENT_ID = "6710301043"
    print(f"{ctime()} | --- [Light 2] Turn ON by delay (as_completed) ---")

    lights = ["light_1", "light_2", "light_3", "light_4"]
    start_time = time()

    tasks = [
        asyncio.create_task(control_light(MY_STUDENT_ID, light_id, "ON"))
        for light_id in lights
    ]

    for light_id in lights:
        print(f"{ctime()} | Turning ON {light_id}...")

    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"{ctime()} | Result: {result['light_id']} is {result['current_status']}")

    print(f"{ctime()} | Total time: {time() - start_time:.2f} seconds (Follows delay order).")

if __name__ == "__main__":
    asyncio.run(main())
