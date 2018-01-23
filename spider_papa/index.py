# -*- coding:utf-8 -*-
"""index module"""
import spider_papa as papa

# def init(domian_name):
#     """create an index objext and return a index selected area"""
#     index = Index(domian_name)
#     return index.init_index()

class Index(object):
    """forum class"""
    def __init__(self, domian_name):
        """ Constructor """
        self.domian_name = domian_name

    def init_index(self):
        """init index, return index selected area"""
        index_doc = self.__get_doc_by_domian_name()
        return self.__get_selected_area(index_doc)

    def __get_doc_by_domian_name(self):
        """ get index doc by domian name """
        index_url = self.__get_url()
        return self.__get_doc(self.domian_name + index_url)

    def __get_selected_area(self, index_doc):
        """ get selected area in index doc """
        return index_doc('#cate_1')

    def __get_url(self):
        main_doc = papa.get_doc(self.domian_name)
        index_herf = main_doc('a:first').attr('href')
        return index_herf

    def __get_doc(self, index_url):
        return papa.get_doc(index_url)



