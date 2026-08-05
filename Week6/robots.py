import asyncio
import time
import httpx

# ==========================================
# 1. Configuration & Constants
# ==========================================
STUDENT_ID = "6710301043" 
BASE_URL = "http://172.16.2.117:8088"

# กำหนดลำดับชิ้นส่วนและหุ่นยนต์
PARTS = ["A", "B", "C"]
ROBOTS = ["robot_1", "robot_2", "robot_3", "robot_4"]

# ==========================================
# 2. Async Functions Development
# ==========================================

async def reset_factory(client: httpx.AsyncClient):
    """ส่ง Request เพื่อทำการ Reset สถานะของหุ่นยนต์ทั้งหมดของรหัสนักเรียนนี้"""
    # TODO: เติมโค้ดการส่ง POST request ไปยัง /student/{STUDENT_ID}/reset

    endpoint = f"{BASE_URL}/reset"
    response = await client.post(endpoint, timeout=10.0)
    if response.status_code == 200:
            return response.json()
    else:
        return {"status": "ERROR", "detail": f"HTTP Error {response.status_code}"}

async def grab_part(client: httpx.AsyncClient, robot_id: str, part: str):
    """สั่งให้หุ่นยนต์หยิบชิ้นส่วน 1 ชิ้น"""
    # TODO: เติมโค้ดส่ง POST request ไปยัง /student/{STUDENT_ID}/robot/{robot_id}/grab
    # พร้อมแนบ JSON Payload {"part": part}
    
    endpoint = f"{BASE_URL}/robot/{robot_id}/grab"
    response  = await client.post(endpoint)

    if response.status_code == 200:
        return response.json()
    else:
        return {"status": "ERROR", "detail": f"HTTP Error {response.status_code}"}


async def run_robot_task(client: httpx.AsyncClient, robot_id: str):
    """สั่งให้หุ่นยนต์ 1 ตัว ทำการหยิบชิ้นส่วน A, B, และ C ตามลำดับ"""
    # TODO: วนลูปหยิบชิ้นส่วนใน PARTS ตามลำดับเรียงกัน (Sequential inside single robot)
    
    for robot in ROBOTS:
        await grab_part(robot_id=robot, part="A")
        await grab_part(robot_id=robot, part="B")
        await grab_part(robot_id=robot, part="C")

async def main():
    """ฟังก์ชันหลักสำหรับเริ่มการทำงานของหุ่นยนต์ทั้ง 4 ตัวแบบ Async"""
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=10.0) as client:
        print("Resetting Factory...")
        await reset_factory(client)
        
        start_time = time.time()
        print("Starting Async Robot Operation...")
        
        # TODO: สั่งรัน run_robot_task ของหุ่นยนต์ทั้ง 4 ตัวพร้อมกันโดยใช้ asyncio.gather
        
        elapsed_time = time.time() - start_time
        print(f"Finished all tasks in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())