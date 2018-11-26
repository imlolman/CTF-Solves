from Crypto.Util.number import *
from Crypto.PublicKey import RSA
#import gmpy2
#from secret import flag

ciphertext = open("ciphertext.txt")
# p = getPrime(512)
# q = getPrime(512)
# n = p*q
# size() from Crypto.Util.number tells the size of the number (in bits)
# size1 = size(n)

e = 3

obj1 = RSA.importKey(open("publickey.pem").read())
n = obj1.n
e = obj1.e
size1 = size(n)
print(size1)
#assert GCD(e, (p-1)*(q-1)) == 1

# m = bytes_to_long(flag)
# ciphertext = long_to_bytes(pow(m, e, n))

# obj1 = open("ciphertext.txt",'w')
# obj1.write(ciphertext)

# publickey = RSA.construct((n, long(e)))
# # Read this documentation on how to construct and import PEM files using pycrypto
# # Public Key encryption: https://www.dlitz.net/software/pycrypto/api/2.6/toc-Crypto.PublicKey.RSA-module.html
# # Construct PEM files: https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.PublicKey.RSA-module.html#construct
# # Import PEM files: https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.PublicKey.RSA-module.html#importKey
# f = open("publickey.pem",'w')
# f.write(publickey.exportKey("PEM"))



#RSA Public-Key: (1023 bit)
#Modulus:
#58:e7:43:a4:01:31:8e:5b:e5:59:5c:73:08:a9:ab:7f:82:4d:c5:28:b9:b3:27:24:f6:35:fa:b9:59:fd:d5:20:e7:1f:6c:4c:af:2a:80:90:7f:17:f0:b8:c6:62:25:6d:a3:f4:78:b7:b2:47:14:c0:8a:2f:17:42:d6:83:c6:90:ec:45:ef:9f:51:04:6c:7f:5d:97:b9:71:2d:08:0c:f0:05:a8:b3:f3:87:fd:b4:d0:ee:12:c0:10:41:51:97:c9:fe:a1:79:38:bf:34:0c:5c:0f:26:4f:72:28:73:cd:18:62:7a:15:b9:5e:d9:7b:17:1a:04:15:b5:d8:32:de:31
#Exponent: 3 (0x3)
