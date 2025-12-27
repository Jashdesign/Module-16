import hashlib
import hmac
import base64

def generate_checksum(params, merchant_key):
    data = "|".join(str(params[key]) for key in sorted(params))
    return base64.b64encode(
        hmac.new(merchant_key.encode(), data.encode(), hashlib.sha256).digest()
    ).decode()

def verify_checksum(params, merchant_key, checksum):
    generated = generate_checksum(params, merchant_key)
    return generated == checksum