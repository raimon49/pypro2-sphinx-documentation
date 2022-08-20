============================
Sphinxによるドキュメント管理
============================

.. image:: https://requires.io/github/raimon49/pypro2-sphinx-documentation/requirements.svg?branch=master
     :target: https://requires.io/github/raimon49/pypro2-sphinx-documentation/requirements/?branch=master
     :alt: Requirements Status
.. image:: https://circleci.com/gh/raimon49/pypro2-sphinx-documentation.svg?style=svg
    :target: https://circleci.com/gh/raimon49/pypro2-sphinx-documentation
    :alt: CircleCI Status

目的
====

Sphinxを使ったドキュメント管理の学習用。

参考：
    * 『Pythonプロフェッショナルプログラミング第2版』
    * 『Pythonプロフェッショナルプログラミング第3版』（CircleCI部分）

ホスティング先
==============

http://raimon49.github.io/pypro2-sphinx-documentation/

構成
====

::

    |-- README.rst
    |-- requirements.txt
    `-- sw-project
        |-- Makefile
        |-- _build
        |   |-- doctrees
        |   `-- html       (gh-pages branch)
        |-- _static
        |-- _templates
        |-- conf.py
        |-- index.rst
        |-- make.bat
        |-- path.rst
        |-- sample.rst
        `-- src

ビルド・更新手順
================

ホスティング先である `GitHub Pages <http://raimon49.github.io/pypro2-sphinx-documentation/>`_ への反映手順。

.. code-block:: bash

    # HTMLファイルの更新
    $ make html

    # gh-pagesブランチへの反映
    $ cd sw-project/_build/html
    $ git checkout gh-pages
    $ git commit -am 'Update documentation'
    $ git push origin gh-pages

    # submoduleの参照先をmasterブランチに反映
    $ git checkout master
    $ cd ../../..
    $ git add sw-project/_build/html
    $ git commit -am 'Update submodule commit'
    $ git push origin master
