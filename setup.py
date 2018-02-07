from setuptools import setup

setup(name='papa1024',
      version='1.0.4',
      description='papa1024 is the web crawler application of the 1024 forum.',
      license='MIT',
      author='liuziyuan',
      author_email='liuziyuan.room@gmail.com',
      url='https://github.com/liuziyuan/papa1024',
      packages = ['papa1024'],
      install_requires=['requests>=2.18.4', 'pyquery>=1.4.0', 'threadpool>=1.3.2']
     )