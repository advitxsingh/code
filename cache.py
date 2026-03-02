import asyncio
from typing import Callable, Any

class AsyncMemoizer:
    def __init__(self):
        self.cache = {}
        # TODO: Add necessary synchronization primitives
        
    async def get(self, key: str, compute_func: Callable[[], Any]) -> Any:
        """
        Returns cached value if present. Otherwise, awaits compute_func().
        
        Real-World Constraints:
        1. Single-Flight: If multiple concurrent calls request a missing key, 
           compute_func MUST only execute ONCE. Others must wait for that result.
        2. Fault Tolerance: If compute_func raises an exception, ALL concurrent 
           waiters must receive the exception, and the key must be cleanly 
           reset so future calls can retry.
        """
        pass