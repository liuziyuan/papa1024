import requests
from pyquery import PyQuery as pq


def get_index_url(main_page):
    main_doc = pq(main_page.text)
    index_herf = main_doc('a:first').attr('href')
    return index_herf


def get_index_doc(index_url):
    page = requests.get(index_url)
    doc = pq(page.text)
    return doc


def get_movie_board_links(index_doc):
    movie_table = index_doc('#cate_1')
    board_hash = {0: '', 1: '', 2: '', 4: '', 5: ''}
    for key in board_hash:
        board_hash[key] = domian_name + \
            movie_table.find("tr").eq(key).find('a').eq(1).attr('href')
    return board_hash


def get_board_posts_links(link):
    print link
    return


# get main page by domain name
domian_name = 'http://dd.itbb.men/'
main_page = requests.get(domian_name)
# get index page url
index_url = get_index_url(main_page)
# get index page doc
index_doc = get_index_doc(domian_name + index_url)
# get board links which has bt download
board_links = get_movie_board_links(index_doc)
# get board post list
for key in board_links:
    get_board_posts_links(board_links[key])


