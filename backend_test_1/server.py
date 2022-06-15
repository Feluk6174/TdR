import aiohttp, logging
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def test(request):
	print(request.)
	data = request.match_info.get("data", "wtf")
	logging.info(data)
	return web.Response(text=f"{data}")

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', handle), web.get("/test/{data}", test), web.get('/{name}', handle)])
    web.run_app(app)