# papa1024

## Description
> papa(爬爬)1024 is the web crawler application of the 1024 forum.
Through this application to learn python, including  string, array, dictionary, class, multithread, multi process and so on. Through this project, we can master various uses of Python.


## How to use it

### Command
```
python papa.py
```

### Demo Code
```
# -*- coding:utf-8 -*-
import papa1024 as papa
import time


def post_call_back(request, result):
    """get post callback function, result is the post object"""
    print(result.url)
    print(result.download_count)

domian_name = 'http://cl.ghuws.men/'
print('---------------start---------------')
t = time.time()

# get index object
try:
    index = papa.index.Index(domian_name)
except Exception as exc:
    print(exc)
else:
    # get selected area at index page
    index_selected_area = index.init_index()

    # get board info by sequences
    board_sequences = [0, 1, 2, 4, 5]
    # get board objects by sequences and index_selected_area
    boards = papa.board.init(board_sequences, index_selected_area)

    # method 1: execute boards single process
    # papa.board.execute(boards, index.domian_name, 1, post_call_back)

    # method 2: execute boards multi process
    papa.board.task_execute(boards, index.domian_name, 1, 40, post_call_back)


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

## Deploy
1. install setuptools, then you could write setup file inherited from setuptools
```
curl https://bootstrap.pypa.io/ez_setup.py -o - | python
```
2. install twine, for upload file to pypi
```
pip install twine
```
3. sdist file
```
python setup.py sdist

twine upload dist/*
```
