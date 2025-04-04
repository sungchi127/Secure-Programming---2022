from sys import prefix
from pwn import *
from Crypto.Cipher import AES
import os

con=remote("edu-ctf.zoolab.org",10101)
# print(con.read())
result=con.read()[:-1]
# print(result)
result=result.decode("utf-8")
result=bytes.fromhex(result)
# print(result)
# result=result.decode("utf-8")
iv=result[:16]
cipher=result[16:]
total_ct=result;        #bytes型態的東西
nblock=len(total_ct)//16

# for bk in range(1,nblock):
#     bk_pt=b""
#     bk_ct=total_ct[bk*16:(bk+1)*16]
#     last_ct=total_ct[(bk-1)*16:bk*16]
#     for  idx in range (15,-1,-1):
pt=b""
for block in range(1,nblock):
    block_pt=b""
    block_ct=total_ct[block*16:(block+1)*16]
    last_ct=total_ct[(block-1)*16:block*16]
    for idx in range (15,-1,-1):
        posfix=bytes([i^j for i,j in zip(block_pt,last_ct[idx+1:])])
        prefix=last_ct[:idx]
        for i in range(128,256):
            now=prefix+bytes([i^last_ct[idx]])+posfix+block_ct
            con.sendline(now.hex().encode("ascii"))
            res=con.readline()
            if res==b"Well received :)\n":
                block_pt=bytes([i^0x80])+block_pt
                break
        else:
            print("oh-no")
            block_pt=bytes([0x80])+ block_pt
    pt+=block_pt
print(pt)
    

# byt_res=bytes.fromhex(result);
# iv, known_ciph=result[:16],result[16:];

#7個block的cipher