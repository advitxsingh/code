# The Request Coalescing Challenge

A concurrency challenge that consistently defeats modern LLMs (including GPT-4 and Claude 3 Opus). 

When faced with preventing cache stampedes in async Python, LLMs overwhelmingly default to `asyncio.Lock()`. This serializes requests instead of coalescing them, failing the performance requirements and often breaking exception broadcasting.

## The Challenge
Implement `AsyncMemoizer` in `cache.py` to satisfy two constraints:
1. **Single-Flight:** Multiple concurrent requests for a missing key must only trigger the compute function *once*.
2. **Fault Tolerance:** Exceptions must broadcast to all waiting tasks, and the state must cleanly reset for future retries.

## Testing
Run the verification suite locally without human interaction:
```bash
python test_cache.py