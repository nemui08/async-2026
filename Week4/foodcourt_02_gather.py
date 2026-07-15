import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301043"
    print(f"{ctime()} | --- [Task 2] Practice using gather to wait for all group orders ---")
    
    start_time = time()

    results = await asyncio.gather(
        send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice"),
        send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles"),
        send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")
    )
    end_time = time()
    
    for result in results:
        shop = result['shop']
        menu = result['menu']
        print(f"{ctime()} | [Pickup] Shop: {shop} | Menu: {menu} is ready!")
    
    print(f"{ctime()} | Total time: {end_time - start_time:.2f} seconds (Equals to the slowest dish).")

if __name__ == "__main__":
    asyncio.run(main())