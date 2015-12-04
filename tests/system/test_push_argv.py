import argparse
import sys

import pytest

import rmsutil.system


def test_push_argv():
    def assert_absent():
        assert '--cats' not in sys.argv
        assert '99' not in sys.argv

    assert_absent()

    # NOTE(kgriffs): argparse is OK with args of type unicode,
    #   so push_argv isn't strict about it either.
    with rmsutil.system.push_argv(
        u'--cats', 'yes',
        '--answer', u'42',
    ):
        assert '--cats' in sys.argv
        assert 'yes' in sys.argv

        parser = argparse.ArgumentParser()
        parser.add_argument('--cats')
        parser.add_argument('--answer', type=int)

        args = parser.parse_args()
        assert args.cats == 'yes'
        assert args.answer == 42

    assert_absent()


def test_push_argv_raised():
    with pytest.raises(Exception):
        with rmsutil.system.push_argv('--cats'):
            assert '--cats' in sys.argv
            raise Exception()

    assert '--cats' not in sys.argv


def test_push_argv_requires_string_values():
    with pytest.raises(TypeError):
        with rmsutil.system.push_argv(1234):
            pass

    with pytest.raises(TypeError):
        with rmsutil.system.push_argv('-x', 1234):
            pass
