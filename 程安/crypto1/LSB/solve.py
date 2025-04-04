from pwn import *
from Crypto.Util.number import *

p = remote("edu-ctf.zoolab.org",10102)
n = p.recvline().strip()
n = int(n)
e = p.recvline().strip()
e = int(e)
c = p.recvline().strip()
c = int(c) 
a = 0
plaintext = 0
cnt = 0
i=0
while True:
    inv = pow(3,-1,n)
    cc = (c * pow(inv,e*i,n)) % n
    p.sendline(str(cc))
    m = p.recvline().strip()[:]
    print(m)
    m = int(m)
    nexta = (m - (a*inv) % n) % 3
    print ("Number:" + str(i))
    if nexta == 0:
        cnt += 1
        if cnt == 10:
            break
    else:
        cnt = 0
    a = a*inv + nexta
    plaintext = 3**i*nexta + plaintext
    print (long_to_bytes(plaintext))
    i += 1
print (long_to_bytes(plaintext))