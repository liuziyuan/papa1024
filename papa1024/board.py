# -*- coding:utf-8 -*-
"""board module"""
import threadpool
import multiprocessing
import asyncio
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
    """use multi process to execute with sync way"""
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

def task_async_execute(boards, domian_name, max_page_index, func_callback):
    """use multi process to execute with sync way"""
    mp_count = []
    for board in boards:
        process = multiprocessing.Process(target=board.async_board_process, args=(
            board, domian_name, max_page_index, func_callback))
        process.daemon = True
        process.start()
        mp_count.append(process)

    for process in mp_count:
        process.join()
    return

def execute(boards, domian_name, max_page_index, func_callback):
    """use main process to execute with sync way"""
    for board in boards:
        board.board_single(board, domian_name, max_page_index, func_callback)
        

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

    def async_board_process(self, board, domian_name, max_page_index, func_callback):
        url = domian_name + board.url
        for page_index in range(1, max_page_index + 1):
            loop = asyncio.get_event_loop()
            connector = papa.get_aiohttp_TCPConnector(120)
            session = papa.get_aiohttp_ClientSession(connector)
            rows = self.get_pager_rows(url, page_index)
            tasks = [self.async_set_post(session, row, domian_name, func_callback) for row in rows]
            loop.run_until_complete(asyncio.wait(tasks))
            loop.close()
            connector.close()

    def board_process(self, board, domian_name, max_page_index, pool_size, func_callback):
        """create a process that opens up a multi thread pool in this process"""
        url = domian_name + board.url
        pool = threadpool.ThreadPool(pool_size)
        args = []
        for page_index in range(1, max_page_index + 1):
            rows = self.get_pager_rows(url, page_index)
            for row in rows:
                args.append((None, {'row': row, 'domian_name': domian_name}))
        requests = threadpool.makeRequests(self.set_post, args, func_callback)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        
    def board_single(self, board, domian_name, max_page_index, func_callback):
        url = domian_name + board.url
        for page_index in range(1, max_page_index + 1):
            rows = self.get_pager_rows(url, page_index)
            for row in rows:
                post = self.set_post(row, domian_name)
                func_callback(None, post)

    def set_post(self, row, domian_name):
        """set post info and return the post object"""
        post = papa.post.Post()
        return post.set_post_base_info(row, domian_name)

    async def async_set_post(self, session, row, domian_name, func_callback):
        post = papa.post.Post()
        post = await post.async_set_post_base_info(session, row, domian_name)
        func_callback(None, post)

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
        url = self.__set_pager_url(url, page_index)
        post_rows = self.__get_post_rows(url)
        return post_rows

    async def async_get_pager_rows(self, session, url, page_index):
        """
        get pager post
        pager params : &search=&page=2
        """
        url = self.__set_pager_url(url, page_index)
        post_rows = await self.__async_get_post_rows(session, url)
        return post_rows

    def __set_pager_url(self, url, page_index):
        params = "&search=&page=" + str(page_index)
        if page_index != 1:
            url = url + params
        return url

    def __get_post_rows(self, url):
        """ get selected post list area """
        doc = papa.get_doc(url)
        trs = self.__get_trs(doc)
        rows = self.__get_selected_rows(trs)
        return rows

    async def __async_get_post_rows(self, session, url):
        """ get selected post list area by async"""
        doc = await papa.async_get_doc(session, url)
        trs = self.__get_trs(doc)
        rows = self.__get_selected_rows(trs)
        return rows

    def __get_trs(self, doc):
        return doc('#ajaxtable').find('tr')
        
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
