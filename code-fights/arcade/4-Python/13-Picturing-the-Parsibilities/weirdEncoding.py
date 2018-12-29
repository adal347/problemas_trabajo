from base64 import b64decode

def weirdEncoding(encoding, message):
    return b64decode(message,encoding ).decode("utf-8")
