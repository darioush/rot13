from __future__ import absolute_import

from ceasar import mk_ceasar


def test_empty():
    for rot in xrange(26):
        assert mk_ceasar(rot)('') == ''


def test_rot_1():
    assert mk_ceasar(1)('abc') == 'bcd'
    assert mk_ceasar(1)('xyz ABC') == 'yza BCD'
    assert mk_ceasar(1)('XYZ~abc') == 'YZA~bcd'


def test_rot_13():
    assert mk_ceasar(13)('abc') == 'nop'
    assert mk_ceasar(13)('nop') == 'abc'
    assert mk_ceasar(13)('xyz ABC') == 'klm NOP'
    assert mk_ceasar(13)('XYZ~abc') == 'KLM~nop'


def test_rot_13_undo():
    rot13 = mk_ceasar(13)
    tests = ['foo', 'BAR', 'baz', '', 'GG', ' yy ', 'The lonely wolf jumps on the moon.']
    for test in tests:
        assert rot13(rot13(test)) == test
