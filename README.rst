============================
Sphinxによるドキュメント管理
============================

目的
====

Sphinxを使ったドキュメント管理の学習用。

（参考：『Pythonプロフェッショナルプログラミング第2版』）

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
    $ git -am 'Update documentation'
    $ git push origin gh-pages

    # submoduleの参照先をmasterブランチに反映
    $ cd ../../..
    $ git add sw-project/_build/html
    $ git -am 'Update submodule commit'
    $ git push origin master
