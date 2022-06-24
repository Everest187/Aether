import aiohttp, asyncio, time

data = []
tasks = []


async def req(sessions, endpoint, headers, method, json=None):
    sents = time.time()
    async with sessions.patch(endpoint, headers=headers, json=json) as fire:
        rev = time.time()
        data.append(
            {"Status": fire.status_code, "Send": sents, "Recv": rev, "Method": method}
        )


async def aeth(datas):
    sessions = aiohttp.ClientSession()
    for req_data in datas:
        tasks.append(
            asyncio.ensure_future(
                req(
                    sessions,
                    f"discord.com/{req_data['Ep']}",
                    f"Authorization: {req_data['Header']}",
                    req_data["Method"],
                    req_data["Json"],
                )
            )
        )
    await asyncio.gather(*tasks)
    await sessions.close()


def raper(token):
    datas = [
        {
            "Ep": "/api/v9/users/@me/settings",
            "Header": token,
            "Json": {"theme": "light"},
            "Method": "FlashBang",
        }
    ]
    asyncio.get_event_loop().run_until_complete(aeth(datas))
