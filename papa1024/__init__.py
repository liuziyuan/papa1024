# -*- coding:utf-8 -*-
"""papa module, common function of operate page """
import requests
from pyquery import PyQuery as pq
import asyncio
import aiohttp
import papa1024.index
import papa1024.board
import papa1024.post

def get_doc(url):
    """get PyQuery object"""
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as exc:
        raise exc
    else:
        page.encoding = 'gbk'
        doc = pq(page.text)
        return doc

def is_connected(url):
    """is connected web site by url"""
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as exc:
        return False
    else:
        return True

async def async_get_doc(session, url):
    async with session.get(url) as response:
        text = await response.text(encoding='gbk')
        doc = pq(text)
        return doc

def get_aiohttp_TCPConnector(limit_size):
    if limit_size >= 0:
        return aiohttp.TCPConnector(limit=limit_size)
    else:
        return aiohttp.TCPConnector()

def get_aiohttp_ClientSession(connector):
    return aiohttp.ClientSession(connector=connector)

# def get_aiohttp_session():
#     connector = get_aiohttp_TCPConnector()
#     return get_aiohttp_ClientSession(connector)
    
