# papa1024

## Description
> papa(爬爬)1024 is the web crawler application of the 1024 forum.
Through this application to learn python, including  string, array, dictionary, class, multithread, multi process and so on. Through this project, we can master various uses of Python.


## How to use it

### Command
```
python papa.py
```

### Code
```
# -*- coding:utf-8 -*-
import spider_papa as papa
import time


def post_call_back(request, result):
    """get post callback function, result is the post object"""
    print result.url
    print result.download_count

domian_name = 'http://dd.itbb.men/'
print '---------------start---------------'
t = time.time()

# get index object
index = papa.index.Index(domian_name)
# get selected area at index page
index_selected_area = index.init_index()

# get board info by sequences
board_sequences = [0, 1, 2, 4, 5]
# get board objects by sequences and index_selected_area
boards = papa.board.init(board_sequences, index_selected_area)
# execute boards process
papa.board.task_execute(boards, index.domian_name, 1, post_call_back)

print("---------------end---------------")
print(time.time() - t)
```

## Development

### Pre Installation

```
sudo pip install pipenv
```

### Recover project

```
pipenv install
```

### Unit tests

```
cd tests
python test_papa.py 
```
