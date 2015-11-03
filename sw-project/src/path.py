# -*- coding: utf-8 -*-


def commonprefix(path_list):
    """
    パスの `path_list` の中の共通する最長のプレフィックスを
    （パス名の1文字1文字を判断して）返します。

        >>> commonprefix(['/usr/bin/python', '/usr/local/bin/python'])
        '/usr/'
        >>> commonprefix(['/usr/bin/python'])
        '/usr/bin/python'

    これは一度に1文字を扱うため、不正なパスを返すことがあるかも
    しれませんので注意してください。

        >>> commonprefix(['/usr/local/bin/python', '/usr/local/bin/pylint'])
        '/usr/local/bin/py'
    """
    if not path_list:
        return ''

    s1 = min(path_list)
    s2 = max(path_list)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]

    return s1
