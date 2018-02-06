# -*- coding:utf-8 -*-
"""papa module, common function of operate page """
import requests
from pyquery import PyQuery as pq
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
