from ast import Bytes


n=[0x37,0x3d,0x30,0x36,0x0a,0x25,0x03,0x30,0x12,0x42,0x2e,0x3c,0x42,0x2e,0x40,0x37,0x2e,0x24,0x2e,0x12,0x30,0x3f,0x0c,0x00]
# for k in [0,24]:
for i in range(len(n)):
    n[i]=n[i]^0x71

print(bytes(n))