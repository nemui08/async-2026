# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)
import asyncio
from time import ctime

async def fetch_stock_price(server_name, delay):
    await asyncio.sleep(delay)
    return f"[{server_name}] Price: 150 USD"

async def main():
    task = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0)),
        asyncio.create_task(fetch_stock_price("Beta", 0.8)),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5))
    }

    done, pending = await asyncio.wait(task, return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        print(f"{ctime()} Winner Result: {task.result()}")

    for task in pending:
        task.cancel()
        print(f"{ctime()} Cleaning up {len(pending)} pending task...") # Expected output: 2

asyncio.run(main())
