import httpx

async def control_light(student_id: str, light_id: str, status: str = "ON") -> dict:
    url = f"http://172.16.2.117:8088/api/{student_id}/lights/{light_id}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"status": status}, timeout=10.0)
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "ERROR", "detail": f"HTTP Error {response.status_code}"}
    except Exception as e:
        return {"status": "ERROR", "detail": f"Connection failed: {e}"}
