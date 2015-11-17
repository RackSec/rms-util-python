import binascii
import hashlib
import hmac

import six


def hmac_sha256(key, message):
    """Calculate the HMAC-SHA256 of a message.

    Args:
        key (str): Hexadecimal-encoded signing key. The key must be at
            least 16 bytes in length.
        message (str or bytes): Arbitrary message to hash. If a Unicode
            string, will be encoded as UTF-8 before hashing.

    Returns:
        str: Hexadecimal-encoded HMAC of the message
    """

    if len(key) < 32:  # 128 / 8 * 2
        raise ValueError('Key size must be at least 128 bits')

    if isinstance(message, six.text_type):
        msg_bytes = message.encode('utf-8')
    else:
        msg_bytes = message

    key_bytes = binascii.unhexlify(key)
    return hmac.new(key_bytes, msg_bytes, hashlib.sha256).hexdigest()
