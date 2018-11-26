from Crypto.Cipher import AES
import re

ct = open("ciphertext.txt").read()

def pad(s):
    s += chr(16 - len(s)%16)*(16 - len(s)%16)
    return s

key = "\xa2q\x8bu6Y\xa1\rT\xb7\xce\x86\x81S\xf2\xfc"
obj1 = AES.new(key, AES.MODE_ECB)

flag = obj1.decrypt(pad(ct))

print(re.search("inctf{(.*)}",flag).group(0))
