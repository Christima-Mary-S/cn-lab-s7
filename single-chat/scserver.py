import socket

s = socket.socket()
print("socket created")

s.bind(('localhost',9999))

s.listen(3)
print("waiting for connection")

while True:
  c,addr = s.accept()
  print("connected with", addr)
  
  c.send(bytes('connected'))
  num2 = int(c.recv(1024).decode())
  print('the number is: ', num2)
  
  if(num2 % 2 ==0):
    c.send(bytes('is even'))
  else:
    c.send(bytes('is odd'))
 
  c.close()
