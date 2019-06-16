#!usr/bin/env python

import pytest

from src import accepts


class TestAccepts:

    def test_positional(self):

        @accepts(int, int)
        def f(a, b):
            return a, b

        @accepts(int, int)
        def f(a, b):
            return a, b

        with pytest.raises(TypeError):
            f(a=1., b=1.)
        with pytest.raises(TypeError):
            f(1., 1.)
        with pytest.raises(TypeError):
            f(1., b=1.)
        assert f(1, 1) == (1, 1)

    def test_keywords(self):
        @accepts(int, b=int)
        def f(a, b):
            return a, b

        with pytest.raises(TypeError):
            f(a=1., b=1.)
        with pytest.raises(TypeError):
            f(1., 1.)
        with pytest.raises(TypeError):
            f(1., b=1.)
        assert f(1, 1) == (1, 1)

    def test_mixed(self):
        @accepts(a=int, b=int)
        def f(a, b):
            return a, b

        with pytest.raises(TypeError):
            f(a=1., b=1.)
        with pytest.raises(TypeError):
            f(1., 1.)
        with pytest.raises(TypeError):
            f(1., b=1.)
        assert f(1, 1) == (1, 1)
