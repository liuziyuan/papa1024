# -*- coding:utf-8 -*-
"""board module"""
import threadpool
import multiprocessing
import papa1024 as papa


def init(board_sequences, index_selected_area):
    """init boards by board_sequences"""
    boards = []
    for seq in board_sequences:
        board = Board(seq)
        board.set_board_info(index_selected_area)
        boards.append(board)
    return boards


def task_execute(boards, domian_name, max_page_index, pool_size, func_callback):
    """execute process"""
    mp_count = []
    for board in boards:
        process = multiprocessing.Process(target=board.board_process, args=(
            board, domian_name, max_page_index, pool_size, func_callback))
        process.daemon = True
        process.start()
        mp_count.append(process)

    for process in mp_count:
        process.join()
    return

class Board(object):
    """
    sequence is board index
    name is board name
    url is board first page url
    """

    def __init__(self, sequence):
        self.sequence = sequence
        self.name = None
        self.url = None
        self.posts = []

    def board_process(self, board, domian_name, max_page_indexs, pool_size, func_callback):
        """createa board_process """
        url = domian_name + board.url
        pool = threadpool.ThreadPool(pool_size)
        args = []
        for page_index in range(1, max_page_indexs + 1):
            rows = self.get_pager_rows(url, page_index)
            for row in rows:
                args.append((None, {'row': row, 'domian_name': domian_name}))
        requests = threadpool.makeRequests(self.__set_post, args, func_callback)
        [pool.putRequest(req) for req in requests]
        pool.wait()

    def __set_post(self, row, domian_name):
        """set post info and return the post object"""
        post = papa.post.Post()
        return post.set_post_base_info(row, domian_name)

    def set_board_info(self, index_selected_area):
        """ set board url and name """
        link = index_selected_area.find("tr").eq(self.sequence).find('a').eq(2)
        self.url = link.attr('href')
        self.name = link.text()
        return self

    def get_pager_rows(self, url, page_index):
        """
        get pager post
        pager params : &search=&page=2
        """
        params = "&search=&page=" + str(page_index)
        if page_index != 1:
            url = url + params
        post_rows = self.__get_post_rows(url)
        return post_rows

    def __get_post_rows(self, url):
        """ get selected post list area """
        doc = papa.get_doc(url)
        trs = doc('#ajaxtable').find('tr')
        rows = self.__get_selected_rows(trs)
        return rows

    def __get_selected_rows(self, trs):
        index = 0
        common_topic_index = 0
        rows = []
        for row in trs.items():
            index += 1
            if row.attr('class') == 'tr2':
                common_topic_index = index
                index = 0
                break
        for row in trs.items():
            index += 1
            if index > common_topic_index and row.attr('class') == 'tr3 t_one tac':
                rows.append(row)
        return rows
