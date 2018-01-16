import requests
from pyquery import PyQuery as pq

def get_index_url(main_page):
    main_doc = pq(main_page.text)
    index_herf = main_doc('a:first').attr('href')
    return index_herf

def get_doc(url):
    page = requests.get(url)
    doc = pq(page.text)
    return doc

def get_movie_board_urls(index_doc):
    movie_table = index_doc('#cate_1')
    board_hash = {0: '', 1: '', 2: '', 4: '', 5: ''}
    for key in board_hash:
        board_hash[key] = movie_table.find("tr").eq(key).find('a').eq(1).attr('href')
    return board_hash

def get_board_post_infos(board, url):
    post_infos = []
    doc = get_doc(domian_name + url)
    tr_list = doc('#ajaxtable').find('tr')
    posts = get_posts(tr_list)
    print len(posts)
    for post in posts:
        post_infos.append(get_post_info(board, post))
    return post_infos

def get_posts(tr_list):
    index = 0
    common_topic_index = 0
    posts = []
    for tr in tr_list.items():
        index += 1
        if tr.attr('class') == 'tr2':
            common_topic_index = index
            index = 0
            break
    for tr in tr_list.items():
        index += 1
        if index > common_topic_index and tr.attr('class') == 'tr3 t_one tac':
            posts.append(tr)
    return posts

def get_post_info(board, post):
    post_info = {}
    link = post.find('.tal').find('a')
    post_info['board'] = board
    href = link.attr('href')
    post_info['href'] = href
    post_info['text'] = link.text()
    post_info['download_href'] = get_post_download_url(href)
    print post_info['download_href']
    return post_info

def get_post_download_url(href):
    print href
    download_href = ''
    doc = get_doc(domian_name + href)
    # download_href = doc('.tr1 .do_not_catch').eq(0).find('a:last').attr('href')
    a_index = doc('.tpc_content').children('a').length - 1
    download_href = doc('.tpc_content').children('a').eq(a_index).attr('href')
    if download_href != None:
        download_href = format_rmdown(download_href)
    return download_href

def format_rmdown(download_href):
    download_href = download_href[:-2]
    download_href = download_href.replace('______','.')
    download_href_array = download_href.split('?')
    download_href = download_href_array[1] + '?' + download_href_array[2]
    return download_href



# get main page by domain name
domian_name = 'http://dd.itbb.men/'
# main_page = requests.get(domian_name)
# # get index page url
# index_url = get_index_url(main_page)
# # get index page doc
# index_doc = get_doc(domian_name + index_url)
# # get board links which has bt download
# board_links = get_movie_board_urls(index_doc)
# # get board post list
# all_posts = []
# for key in board_links:
#     all_posts += get_board_post_infos(key, board_links[key])
# print len(all_posts)

test = 'htm_data/4/1801/2922054.html'
print get_post_download_url(test)

test2 = 'htm_data/4/1801/2922191.html'
print get_post_download_url(test2)
