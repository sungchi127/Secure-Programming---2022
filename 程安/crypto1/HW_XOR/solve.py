import random
from random import  randint
import time

import numpy as np
from numpy.linalg import inv
import sys
np.set_printoptions(threshold=sys.maxsize)

def negint(x):
    return -1*int(x)

outpt=[1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0]
newpt=outpt[:336]
state =randint(0, 1 << 64)
clean_opt=outpt[336:]

poly=0xda785fc480000001
comatrix=np.ndarray((64,64),dtype=int)
for i in range(64):
    for j in range(64):
        if j==0:
            if((poly)&(1 << (63-i))):
                comatrix[i][j]= 1  
            else: 
                comatrix[i][j]= 0
        elif j==i+1:
            comatrix[i][j]=1
        else:
            comatrix[i][j]=0

trans37=  comatrix.copy()

for i in range(36):
    trans37=trans37.dot(comatrix)%2
tmp=np.eye(64,64,dtype=int)
for i in range(36):
    tmp=tmp.dot(comatrix)%2
# print(tmp)
equationMatrix=np.eye(64,64,dtype=int)
for i in range(336):
    tmp=tmp.dot(trans37)%2
for i in range(64):
   equationMatrix[i]=tmp[0] 
   tmp=tmp.dot(trans37)%2
   
ansvec=outpt[336:336+64]
for i in range(64):
    col=0
    for j in range(64):
        if equationMatrix[i][j] ==1:
            col=j
            break
    for k in range(64):
        if k==i or equationMatrix[k][col]==0:
            continue
        for j in range(64):
            equationMatrix[k][j]^=equationMatrix[i][j]
        ansvec[k]^=ansvec[i]
   
ostate =equationMatrix.T.dot(ansvec)%2
ostate=int(''.join(map(str,ostate)),2)
# print(ostate)
def getbit():
    global ostate
    ostate <<= 1
    if ostate & (1 << 64):
        ostate ^= 0x1da785fc480000001
        return 1
    return 0
   
for i in range(336):
    for _ in range(36):
        getbit()
    outpt[i] ^= getbit()
        
flag=b''

ans=[]
for i in range(42):
    c=int(''.join(map(str,outpt[i*8:(i+1)*8])),2)
    ans.append(c)
flag=bytes(ans)

print(flag)     