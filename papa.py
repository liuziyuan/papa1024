# -*- coding:utf-8 -*-
import requests
from pyquery import PyQuery as pq
import spider_papa as papa

domian_name = 'http://dd.itbb.men/'
# get index doc
index_doc = papa.index.get_doc_by_domian_name(domian_name)
index_selected_area = papa.index.get_selected_area(index_doc)

# get board info by sequences
board_sequences = [0, 1, 2, 4, 5]
boards = papa.board.init(board_sequences, index_selected_area)

for board in boards:
    rows = board.get_pager_rows(domian_name + board.url, 1)
    for row in rows:
        post = papa.post.Post()
        post.set_post_base_info(row, domian_name)
# print len(board.get_pager_rows(domian_name + board.url, 1))

# test = 'http://dd.itbb.men/read.php?tid=2924053'
# download_url = papa.post.Post().get_download_url(test)
# print download_url
# print papa.post.Post().get_download_count(download_url)

# test1 = 'http://dd.itbb.men/htm_data/4/1801/2922054.html'
# download_url = papa.post.Post().get_download_url(test1)
# print download_url
# print papa.post.Post().get_download_count(download_url)

# test2 = 'http://dd.itbb.men/htm_data/4/1801/2922191.html'
# download_url = papa.post.Post().get_download_url(test2)
# print download_url
# print papa.post.Post().get_download_count(download_url)

# test3 = "http://dd.itbb.men/htm_data/2/1801/2920227.html"
# download_url = papa.post.Post().get_download_url(test3)
# print download_url
# print papa.post.Post().get_download_count(download_url)