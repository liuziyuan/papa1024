# -*- coding:utf-8 -*-
"""index module"""
import requests
from pyquery import PyQuery as pq
import spider_papa as papa

def get_doc_by_domian_name(domian_name):
    """ get index doc by domian name """
    index_url = __get_url(domian_name)
    return __get_doc(domian_name + index_url)

def get_selected_area(index_doc):
    """ get selected area in index doc """
    return index_doc('#cate_1')


def __get_url(domian_name):
    main_page = requests.get(domian_name)
    main_doc = pq(main_page.text)
    index_herf = main_doc('a:first').attr('href')
    return index_herf

def __get_doc(index_url):
    return papa.get_doc(index_url)
