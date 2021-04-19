import hashlib
import base64


def encoderofstring(str):
    #str = "monkey"
    sha512_bytes = hashlib.sha512(str.encode())

    print(sha512_bytes.hexdigest())

    base64_bytes = base64.b64encode(sha512_bytes.hexdigest().encode())

    print(base64_bytes.decode())

    return base64_bytes.decode()




