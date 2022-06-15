import aiohttp

async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return response.status, response.headers, html
            