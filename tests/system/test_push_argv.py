from __future__ import unicode_literals

import sys

import pytest

import rmsutil.system


def test_push_argv():
    def assert_absent():
        assert '--cats' not in sys.argv
        assert '99' not in sys.argv

    assert_absent()

    with rmsutil.system.push_argv('--cats', '99'):
        assert '--cats' in sys.argv
        assert '99' in sys.argv

    assert_absent()


def test_push_argv_raised():
    with pytest.raises(Exception):
        with rmsutil.system.push_argv('--cats'):
            assert '--cats' in sys.argv
            raise Exception()

    assert '--cats' not in sys.argv
