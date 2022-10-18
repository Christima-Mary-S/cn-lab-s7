import socket
  

c= socket.socket()

c.connect(('localhost',9999))

print(c.recv(1024).decode())
num1= input(" enter the number : ")
c.send(bytes(num1,'utf-8'))
print(c.recv(1024).decode())
