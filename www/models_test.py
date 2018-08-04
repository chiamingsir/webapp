#!usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='webapp')
    u = User(name='Test', email='test@example.com', passwd='password', image='about:blank')
    await u.save()

async def show(loop):
    await asyncio.sleep(1)
    await orm.create_pool(loop, user='www-data', password='www-data', db='webapp')
    rs = await User.findAll();
    print('Find User: %s' % rs)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop), show(loop)]))
loop.run_forever
