import requests
from pyquery import PyQuery as pq

# get index page url
def get_index_url(main_page):
    main_doc = pq(main_page.text)
    index_herf = main_doc('a:first').attr('href')
    return index_herf

# get doc by url
def get_doc(url):
    page = requests.get(url)
    doc = pq(page.text)
    return doc

# get board url list, return all of movie board url {}
def get_movie_board_urls(index_doc):
    movie_table = index_doc('#cate_1')
    board_hash = {0: None, 1: None, 2: None, 4: None, 5: None}
    for key in board_hash:
        board_hash[key] = movie_table.find("tr").eq(key).find('a').eq(1).attr('href')
    return board_hash

# get board posts, no pager, just first page at any board
def get_board_post_infos(board, url):
    post_infos = []
    doc = get_doc(domian_name + url)
    tr_list = doc('#ajaxtable').find('tr')
    posts = get_posts(tr_list)
    print len(posts)
    for post in posts:
        post_infos.append(get_post_info(board, post))
    return post_infos

# get posts by tr list ,return posts []
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

# get post info by board index and post, return post_info {}
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

# get post download url by href, return a href
def get_post_download_url(href):
    print href
    download_href = ''
    doc = get_doc(domian_name + href)
    links = doc('.tpc_content').find('a')
    download_href = get_rmdown_url(links)
    download_href = format_rmdown(download_href)
    return download_href

# get rmdown download url from links of current post
def get_rmdown_url(links):
    used_link = []
    for link in links.items():
        href = str(link.attr('href'))
        if href.find('rmdown') > 0:
            used_link.append(href)
    return used_link[-1]

# format rmdown url to access url
def format_rmdown(download_href):
    download_href = download_href[:-2]
    download_href = download_href.replace('______','.')
    download_href_array = download_href.split('?')
    download_href = download_href_array[1] + '?' + download_href_array[2]
    return download_href



# get main page by domain name
domian_name = 'http://dd.itbb.men/'
main_page = requests.get(domian_name)
# get index page url
index_url = get_index_url(main_page)
# get index page doc
index_doc = get_doc(domian_name + index_url)
# get board links which has bt download
board_links = get_movie_board_urls(index_doc)
# get board post list
all_posts = []
for key in board_links:
    all_posts += get_board_post_infos(key, board_links[key])
print len(all_posts)

# test = 'htm_data/4/1801/2922054.html'
# print get_post_download_url(test)

# test2 = 'htm_data/4/1801/2922191.html'
# print get_post_download_url(test2)
