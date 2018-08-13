import codecs

def messageFromBinaryCode(code):
    decrypt = [code[i:i+8] for i in range(0, len(code), 8)]
    for i in range(len(decrypt)):
        decrypt[i] = hex(int(decrypt[i], 2))
        decrypt[i] = codecs.decode(decrypt[i][2:], "hex")
        decrypt[i] = decrypt[i].decode("utf-8")
    return "".join(decrypt)
