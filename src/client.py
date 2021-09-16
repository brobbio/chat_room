import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))

full_msg = ''
new_msg = True
while True:
    msg = s.recv(16)
    if new_msg:
        msglen = int(msg[:10])
        new_msg = False

    full_msg = full_msg + msg.decode('utf-8')

    if len(full_msg) - 10 == msglen:
        print(full_msg[10:])
        new_msg = True
        full_msg = ''

print(full_msg)
