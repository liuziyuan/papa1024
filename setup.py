import os
from setuptools import setup

def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()

setup(name='papa1024',
      version='1.0.6',
      description='papa1024 is the web crawler application of the 1024 forum.',
      long_description=read('README.rst'),
      license='MIT',
      author='liuziyuan',
      author_email='liuziyuan.room@gmail.com',
      url='https://github.com/liuziyuan/papa1024',
      packages = ['papa1024'],
      install_requires=['requests>=2.18.4', 'pyquery>=1.4.0', 'threadpool>=1.3.2', 'aiohttp>=2.3.10'],
      classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
      )
)