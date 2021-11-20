import base64
import hashlib
import hmac
import json
import time


def base64url_decode(target):
    rem = len(target) % 4
    if rem > 0:
        target += '=' * (4 - rem)

    return base64.urlsafe_b64decode(target)


def check_signature(key, target, signature):
    calc_signature = hmac.new(
        key.encode('utf-8'),
        target.encode('utf-8'),
        hashlib.sha256
    ).digest()

    return hmac.compare_digest(signature, calc_signature)


def decode_id_token(id_token, channel_id, channel_secret, nonce=None):
    # step 1
    header, payload, signature = id_token.split('.')

    # step 2
    header_decoded = base64url_decode(header)
    payload_decoded = base64url_decode(payload)
    signature_decoded = base64url_decode(signature)

    # step 3
    valid_signature = check_signature(channel_secret,
                                      header + '.' + payload,
                                      signature_decoded)
    if not valid_signature:
        raise RuntimeError('invalid signature')

    payload_json = json.loads(payload_decoded.decode('utf-8'))

    # step 4
    if payload_json.get('iss') != 'https://access.line.me':
        raise RuntimeError('invalid iss')

    # step 5
    if payload_json.get('aud') != channel_id:
        raise RuntimeError('invalid aud')

    # step 6
    if int(time.time()) > payload_json.get('exp'):
        raise RuntimeError('invalid exp')

    # step 7 (Optional. But strongly recommended)
    if nonce is not None:
        if payload_json.get('nonce') != nonce:
            raise RuntimeError('invalid nonce')

    return payload_json
