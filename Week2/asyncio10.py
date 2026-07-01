# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio

async def calculate_bil(customer, base_price):
    print(f"Calculating receipt for {customer}...")
    await asyncio.sleep(1)
    final_price = base_price * 1.07  # Add 7% tax
    return final_price  # Return total with tax

async def main():
    task_a = asyncio.create_task(calculate_bil("A", 100))
    task_b = asyncio.create_task(calculate_bil("B", 200))

    result_a = await task_a  # Await and get result for customer A
    result_b = await task_b  # Await and get result for customer B

    print(f"\nFinal Bill A: ${result_a:.2f}")
    print(f"Final Bill B: ${result_b:.2f}")
    print(f"Combined Total Revenue: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())