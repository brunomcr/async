import asyncio
from time import sleep
import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)


async def http_call_async2():
    element_list = ["one", "two", "tree", "four", "five"]
    for element in element_list:
        await asyncio.sleep(2)
        print(element)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)


def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org")
    print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    loop.create_task(http_call_async2())
    return HttpResponse('Non-blocking HTTP request')


def sync_view(request):
    http_call_sync()
    return HttpResponse('Blocking HTTP request')
