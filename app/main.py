import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

@routes.post('/ping')
async def ping(request):
    body = await request.json()
    if 'url' not in body:
        return web.Response(text="nothing to do")
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(body['url']) as resp:
                text = await resp.text()
                return web.Response(text=text)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
