#!usr/bin/env python3
# -*- coding: utf-8 -*-

# from datetime import datetime
from aiohttp import web
import asyncio
# import os
# import json
# import time
import logging

logging.basicConfig(level=logging.INFO)  # specify the level of root logger


def index(request):
    return web.Response(body=b'<h1>Home Page</h1>', content_type='text/html')


async def init(loop):  # decorator to mark generator-based coroutines
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)  # create TCP server
    logging.info('server started at http://127.0.0.1:9000...')
    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
