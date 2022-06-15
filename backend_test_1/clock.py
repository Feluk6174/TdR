import aiohttp
import asyncio
import time
import functions as fn

async def main():
    while True:
        r = await fn.request("http://0.0.0.0:8080/test/hello world")
        print(r)

asyncio.run(main())
#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())