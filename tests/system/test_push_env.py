from __future__ import unicode_literals

import os

import pytest

import rmsutil.system


def test_push_env():
    def assert_absent():
        assert 'OLIVAW_HOST' not in os.environ
        assert 'OLIVAW_USERNAME' not in os.environ
        assert 'OLIVAW_PASSWORD' not in os.environ

    assert_absent()

    with rmsutil.system.push_env(
        OLIVAW_HOST='127.0.0.1',
        OLIVAW_USERNAME='user',
        OLIVAW_PASSWORD='pwd',
    ):
        assert os.environ['OLIVAW_HOST'] == '127.0.0.1'
        assert os.environ['OLIVAW_USERNAME'] == 'user'
        assert os.environ['OLIVAW_PASSWORD'] == 'pwd'

        with rmsutil.system.push_env(OLIVAW_PASSWORD='overridden'):
            assert os.environ['OLIVAW_PASSWORD'] == 'overridden'

        assert os.environ['OLIVAW_PASSWORD'] == 'pwd'

    assert_absent()


def test_push_env_raises():
    with pytest.raises(Exception):
        with rmsutil.system.push_env(
            OLIVAW_HOST='127.0.0.1',
        ):
            assert os.environ['OLIVAW_HOST'] == '127.0.0.1'
            raise Exception()

    assert 'OLIVAW_HOST' not in os.environ
