import socket

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

print(s.recv(1024))
for data in ['lau','yemilice','sarah']:
    s.send(data)
    print(s.recv(1024))
s.send('exit')
s.close()