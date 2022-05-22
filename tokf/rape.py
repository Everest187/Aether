from tokf.reqs import aeth
import asyncio

def raper(token):
	datas = [{"Ep": "/api/v9/users/@me/settings", "Header": token, "Json": {"theme": "light"}, "Method": "FlashBang"}]
	asyncio.get_event_loop().run_until_complete(aeth(datas))