#!usr/bin/env python3
# -*- coding: utf-8 -*-

import aiomysql
import asyncio
import logging


def log(sql, args=()):
    logging.info('SQL: %s', sql)

async def create_pool(loop, **kw):
    logging.info('create database connect pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port',3306),
        user=kw.get['user'],
        password=kw.get['password'],
        db=kw.get['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as connect:
        async with connect.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs


async def execute(sql, args, autocommit=True):
    log(sql)
    global __pool
    async with __pool.get() as connect:
        if not autocommit:
            await connect.begin()
        try:
            async with connect.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args or ())
                affected = cur.rowcount
            if not autocommit:
                await connect.commit()
        except BaseException as e:
            if not autocommit:
                await connect.rollback()
            raise e
        return affected
