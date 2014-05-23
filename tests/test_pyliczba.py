#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyliczba
----------------------------------

Tests for `pyliczba` module.
"""

import unittest

import pyliczba


class TestKwotaSlownie(unittest.TestCase):

    def test_kwotaslownie_no_fmt(self):
        assert pyliczba.kwotaslownie(13.503535) == u"trzynaście złotych 50/100"
        assert pyliczba.kwotaslownie(1210.5045456) == u"jeden tysiąc dwieście dziesięć złotych 50/100"
        assert pyliczba.kwotaslownie(3) == u"trzy złote 0/100"

    def test_kwotaslownie_fmt(self):
        assert pyliczba.kwotaslownie(1213.501546, fmt=True) == u"jeden tysiąc dwieście trzynaście złotych pięćdziesiąt groszy"
        assert pyliczba.kwotaslownie(10.5015465, fmt=True) == u"dziesięć złotych pięćdziesiąt groszy"
        assert pyliczba.kwotaslownie(3, fmt=True) == u"trzy złote zero groszy"


if __name__ == '__main__':
    unittest.main()