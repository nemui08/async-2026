# foodcourt_04_wait_for.py
import asyncio
from time import ctime, time 
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301043"
    print(f"{ctime()} | --- [Task 4] Practice using wait_for to set a timeout for an order ---")
    
    try:
        #1 Order a steak (takes 4s) but enforce a strict timeout of 2.0 seconds.
        print(f"{ctime()} | [System] Order sent. ")
    except asyncio.TimeoutError:
        print(f"{ctime()} | The order took too long and was cancelled.")