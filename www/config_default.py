#!usr/bin/env python3
# -*- coding: utf-8 -*-

""" Default configurations. """

configs = {
    'debug': True,
    'db': {
        'host': 'localhost',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'db': 'webapp'
    },
    'session': {
        'secret': 'signature'
    }
}
