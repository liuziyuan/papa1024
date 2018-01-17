# papa1024

## Description
> papa(爬爬)1024 is the web crawler application of the 1024 forum.
Through this application to learn python, including  string, array, dictionary, class, multithread, multi process and so on. Through this project, we can master various uses of Python.


## How to use it
```
domian_name = 'http://dd.itbb.men/'
# get index doc
index_doc = papa.index.get_doc_by_domian_name(domian_name)
index_selected_area = papa.index.get_selected_area(index_doc)

# get board info by sequences
board_sequences = [0, 1, 2, 4, 5]
boards = papa.board.init(board_sequences, index_selected_area)

for board in boards:
    rows = board.get_pager_rows(domian_name + board.url, 1)
    for row in rows:
        post = papa.post.Post()
        post.set_post_base_info(row, domian_name)
```

## Development

### Pre Installation

```sudo pip install pipenv```

### Recover project

```pipenv install```
