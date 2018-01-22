# -*- coding:utf-8 -*-
import spider_papa as papa
import time
from threading import Thread
import multiprocessing

domian_name = 'http://dd.itbb.men/'
print '---------------start---------------'
t = time.time()
# get index doc
index_doc = papa.index.get_doc_by_domian_name(domian_name)
index_selected_area = papa.index.get_selected_area(index_doc)

# get board info by sequences
board_sequences = [0, 1, 2, 4, 5]
boards = papa.board.init(board_sequences, index_selected_area)

mp_count = []

for board in boards:
    p = multiprocessing.Process(target=papa.board.board_process, args=(
        board, domian_name,1))
    p.daemon = True
    p.start()
    mp_count.append(p)

for p in mp_count:
    p.join()

print("---------------end---------------")
print(time.time() - t)


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
