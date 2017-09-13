#!/usr/bin/python
import sys
KEY = 'musZTXmxV58UdwiKt8Tp'

def xor_str(x, y):
    if len(x) > len(y):
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x[:len(y)], y)])
    else:
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x, y[:len(x)])])

def decode(file_name):
    with open(file_name) as fp:
        content = fp.read()
    l = len(content)
    HEX_KEY = KEY.encode('hex')
    k = len(HEX_KEY)
    expanded_key = HEX_KEY * (l//k + 1)
    decoded_content = xor_str(expanded_key, content)
    print(decoded_content.decode("hex"))

if __name__ == "__main__":
    file_name=sys.argv[1]
    decode(file_name)
