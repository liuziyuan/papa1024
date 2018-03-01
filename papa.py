# -*- coding:utf-8 -*-
import papa1024 as papa
import time


def post_call_back(request, result):
    """get post callback function, result is the post object"""
    print(result.url)
    print(result.download_count)

domian_name = 'http://pp.wedid.us/'
print('---------------start---------------')
t = time.time()

# get index object
try:
    index = papa.index.Index(domian_name)
except Exception as exc:
    print(exc)
else:
    # get selected area at index page
    index_selected_area = index.init_index()

    # get board info by sequences
    board_sequences = [0, 1, 2, 4, 5]
    # get board objects by sequences and index_selected_area
    boards = papa.board.init(board_sequences, index_selected_area)

    # method 1: execute boards single process
    # papa.board.execute(boards, index.domian_name, 1, post_call_back)

    # method 2: execute boards multi process, any process created a thread pool to get http requests
    papa.board.task_execute(boards, index.domian_name, 1, 40, post_call_back)

    # method 3: execute boards multi process, any process created a coroutine to get http requests
    # papa.board.task_async_execute(boards, index.domian_name, 1, post_call_back)

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
