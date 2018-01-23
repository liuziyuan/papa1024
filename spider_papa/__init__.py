# -*- coding:utf-8 -*-
"""papa module, common function of operate page """
import requests
from pyquery import PyQuery as pq
import spider_papa.index
import spider_papa.board
import spider_papa.post

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
    
