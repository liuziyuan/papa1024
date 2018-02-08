# -*- coding:utf-8 -*-
"""post module"""
import papa1024 as papa


class Post(object):
    """
    sequence is board index
    name is board name
    url is board first page url
    """

    def __init__(self):
        """ Constructor """
        self.url = None
        self.name = None
        self.download_url = None
        self.download_count = None

    def set_post_base_info(self, row, domian_name):
        """ set post base infomation """
        link = row.find('.tal').find('a')
        href = link.attr('href')
        self.url = href
        self.name = link.text()
        self.download_url = self.get_download_url(domian_name + self.url)
        self.download_count = self.get_download_count(self.download_url)
        # print self.download_count
        return self

    async def async_set_post_base_info(self,session, row, domian_name):
        """ set post base infomation by async"""
        link = row.find('.tal').find('a')
        href = link.attr('href')
        self.url = href
        self.name = link.text()
        self.download_url = await self.async_get_download_url(session, domian_name + self.url)
        self.download_count = await self.async_get_download_count(session, self.download_url)
        # print self.download_count
        return self

    def get_download_count(self, url):
        """get download count function"""
        if url != None:
            doc = papa.get_doc(url)
            return self.__set_download_count(doc)
        else:
            return None

    async def async_get_download_count(self, session, url):
        """get download count function by async"""
        if url != None:
            doc = await papa.async_get_doc(session, url)
            return self.__set_download_count(doc)
        else:
            return None

    def __set_download_count(self, doc):
        text = doc.text()
        index = text.find('Downloaded:')
        index += 11
        count = list(filter(str.isdigit, text[index : index + 8]))
        count = ''.join(map(str, count))
        return count

    def get_download_url(self, url):
        """get download url"""
        # print url
        doc = papa.get_doc(url)
        return self.__set_download_url(doc)

    async def async_get_download_url(self, session, url):
        """get download url by async"""
        # print url
        doc = await papa.async_get_doc(session, url)
        return self.__set_download_url(doc)

    def __set_download_url(self, doc):
        download_url = None
        links = doc('.tpc_content').find('a')
        download_url = self.__get_rmdown_url(links)
        download_url = self.__format_rmdown(download_url)
        return download_url

    def __get_rmdown_url(self, links):
        """get rmdown download url from links of current post"""
        used_link = []
        for link in links.items():
            href = str(link.attr('href'))
            if href.find('rmdown') > 0:
                used_link.append(href)
        if len(used_link) > 0:
            # find last link
            return used_link[-1]
        else:
            return None

    def __format_rmdown(self, download_href):
        if download_href != None:
            download_href = download_href[:-2]
            download_href = download_href.replace('______', '.')
            download_href_array = download_href.split('?')
            download_href = download_href_array[1] + \
                '?' + download_href_array[2]
        return download_href
