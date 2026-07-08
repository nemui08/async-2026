import asyncio
import httpx  
from time import ctime

async def fetch_stock_price(server_name: str):

    url = f"http://127.0.0.1:8088/price/{server_name}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=5.0)
        data = response.json()
        return f"[{data['server']}] Price: {data['price_usd']} USD"

async def main():
    tasks = [
        asyncio.create_task(fetch_stock_price("Alpha")),
        asyncio.create_task(fetch_stock_price("Beta")),
        asyncio.create_task(fetch_stock_price("Gamma"))
    ]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        print(f"{ctime()} Winner Result: {task.result()}")
    
    if pending:
        print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
        for task in pending:
            task.cancel()

            try:
                await task
            except asyncio.CancelledError:
                pass


if __name__ == "__main__":
    asyncio.run(main())