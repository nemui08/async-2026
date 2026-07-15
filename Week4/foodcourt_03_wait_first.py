# foodcourt_03_wait_first.py
import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301043"
    print(f"{ctime()} | --- [Task 3] Practice using (FIRST_COMPLETED) ---")
    start_time = time()

    # 1. Send 3 orders to complete against each other.
    orders = {
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice"))
    }

    # 2. Use asyncio.wait with FIRST_COMPLETED to unblock as soon as 
    done, pending = await asyncio.wait(orders, return_when=asyncio.FIRST_COMPLETED)

    fastest_dish = list(done)[0].result()
    print(f"{ctime()} | Winner served dish: Shop: {fastest_dish['shop']} | Menu: {fastest_dish['menu']}")
    print(f"{ctime()} | Cleaning up:Canceling {len(pending)} remaining pedinf orders...")
    for t in pending:
        t.cancel()

    print(f"{ctime()} | Winner served dish: Shop: {fastest_dish['shop']} | Menu: {fastest_dish['menu']}")

    print(f"{ctime()} | Total waiting time for the first dish: {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
    