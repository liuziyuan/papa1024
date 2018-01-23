# -*- coding:utf-8 -*-
"""test papa function """
import unittest
import sys
sys.path.append("../")
import spider_papa as papa


class TestMathFunc(unittest.TestCase):
    """Test papa public function"""

    def setUp(self):
        print "create index object before test.Prepare environment."
        self.domian_name = 'http://dd.itbb.men/'
        self.index = papa.index.Index(self.domian_name)
        self.index_selected_area = self.index.init_index()
        self.board = papa.board.Board(1)

    def test_domian_name(self):
        papa.get_doc(self.domian_name)

    def test_init_index(self):
        """Test function init_index()"""
        self.assertEqual(True, self.index_selected_area.find('cate_1') > 0)

    def test_set_board_info(self):
        """Test function set_board_info() on board module"""
        url = self.board.set_board_info(self.index_selected_area).url
        self.assertEqual(True, url.find('.php?fid') > 0)

    def test_board_init(self):
        """Test function init() on board module"""
        boards = papa.board.init([0, 1], self.index_selected_area)
        self.assertEqual(2, len(boards))

    def test_get_pager_rows(self):
        """Test function get_pager_rows() on board module"""
        url = self.board.set_board_info(self.index_selected_area).url
        rows = self.board.get_pager_rows(self.domian_name + url, 1)
        self.assertEqual(True, len(rows) > 50)

    def test_get_download_none(self):
        """Test function get_download_url() on post module"""
        test = self.domian_name + 'read.php?tid=2924053'
        download_url = papa.post.Post().get_download_url(test)
        count = papa.post.Post().get_download_count(download_url)
        self.assertEqual(None, download_url)
        self.assertEqual(None, count)

    def test_get_download_url(self):
        """Test function get_download_url() on post module"""
        test = self.domian_name + 'htm_data/4/1801/2922054.html'
        download_url = papa.post.Post().get_download_url(test)
        count = papa.post.Post().get_download_count(download_url)
        self.assertEqual(True, download_url.find('rmdown') > 0)
        self.assertEqual(True, count > 0)


    def test_set_post_base_info(self):
        """Test function set_post_base_info() on post module"""
        url = self.board.set_board_info(self.index_selected_area).url
        rows = self.board.get_pager_rows(self.domian_name + url, 1)
        post = papa.post.Post()
        post.set_post_base_info(rows[10], self.domian_name)
        self.assertEqual(True, len(post.url) > 0)


if __name__ == '__main__':
    unittest.main()
