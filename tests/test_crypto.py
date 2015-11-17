import re

import pytest

from rmsutil import crypto

_KEY_128 = '6d48a57072a186bc7ef0004a47a990a1'
_MESSAGE = u'Somehow I know.'


@pytest.mark.parametrize(
    'key, message',
    [
        (_KEY_128, _MESSAGE),
        (_KEY_128, _MESSAGE.encode('utf-8')),
        (_KEY_128 + 'ff', _MESSAGE),
        (_KEY_128 * 4, _MESSAGE),
    ]
)
def test_hmac_sha256(key, message):
    hmac = crypto.hmac_sha256(key, message)
    assert re.match('[a-f0-9]{64}$', hmac)


@pytest.mark.parametrize(
    'key',
    [
        '',  # empty
        _KEY_128[2:],  # less than 128 bits
        _KEY_128 + '0',  # odd length
        'k' * 32,  # non-hexadecimal
    ]
)
def test_hmac_sha256_errors(key):
    with pytest.raises((ValueError, TypeError)):
        crypto.hmac_sha256(key, _MESSAGE)
