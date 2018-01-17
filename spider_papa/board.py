# -*- coding:utf-8 -*-
"""board module"""
import spider_papa as papa


def init(board_sequences, index_selected_area):
    """init boards by board_sequences"""
    boards = []
    for seq in board_sequences:
        board = Board(seq)
        board.set_board_info(index_selected_area)
        boards.append(board)
    return boards


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

    def set_board_info(self, index_selected_area):
        """ set board url and name """
        link = index_selected_area.find("tr").eq(self.sequence).find('a').eq(2)
        self.url = link.attr('href')
        self.name = link.text()
        return

    def get_pager_rows(self, url, page_index):
        """
        get pager post
        pager params : &search=&page=2
        """
        params = "&search=&page=" + str(page_index)
        if page_index <> 1:
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
