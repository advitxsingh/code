import asyncio
from typing import Callable, Any

class AsyncMemoizer:
    def __init__(self):
        self.cache = {}
        self.futures = {}

    async def get(self, key: str, compute_func: Callable[[], Any]) -> Any:
        if key in self.cache:
            return self.cache[key]

        if key in self.futures:
            return await self.futures[key]

        loop = asyncio.get_running_loop()
        fut = loop.create_future()
        self.futures[key] = fut

        try:
            result = await compute_func()
            self.cache[key] = result
            fut.set_result(result)
            return result
        except Exception as e:
            fut.set_exception(e)
            raise
        finally:
            self.futures.pop(key, None)