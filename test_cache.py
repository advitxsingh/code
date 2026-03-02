import asyncio
from cache import AsyncMemoizer

async def test_single_flight():
    memo = AsyncMemoizer()
    call_count = 0

    async def db_query():
        nonlocal call_count
        call_count += 1
        await asyncio.sleep(0.1) 
        if call_count == 1:
            raise ConnectionError("Database timeout")
        return "Query Result"

    # Test 1: Concurrency & Exception Propagation
    results = await asyncio.gather(
        memo.get("user_123", db_query),
        memo.get("user_123", db_query),
        memo.get("user_123", db_query),
        return_exceptions=True
    )
    
    assert call_count == 1, f"Thundering herd! Func called {call_count} times."
    assert all(isinstance(r, ConnectionError) for r in results), "Exceptions did not propagate to all waiters."

    # Test 2: State Recovery
    res = await memo.get("user_123", db_query)
    
    assert call_count == 2, "Failed to retry after previous failure."
    assert res == "Query Result", "Did not return correct result."

if __name__ == "__main__":
    asyncio.run(test_single_flight())
    print("Pass!")