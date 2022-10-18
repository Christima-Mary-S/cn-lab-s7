# Reg No: 20219030
# Name: Christima Mary S
# Program No: 8

import socket
import math


# Encryption
def encrypt(msg, key="CUSAT"):
	cipher = ""

	# track key indices
	k_indx = 0

	msg_len = float(len(msg))
	msg_lst = list(msg)
	key_lst = sorted(list(key))

	# calculate column of the matrix
	col = len(key)
	
	# calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# add the padding character '_' in empty
	# the empty cell of the matix
	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)

	# create Matrix and insert message and
	# padding characters row-wise
	matrix = [msg_lst[i: i + col]
			for i in range(0, len(msg_lst), col)]

	#print(f"msg_len: {msg_len}, msg_lst: {msg_lst}, key_lst: {key_lst}")
	#print(matrix)

	# read matrix column-wise using key
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx]
						for row in matrix])
		k_indx += 1
		#print(f"Cipher is now {cipher}")

	return cipher


msgFromClient = encrypt(input("Enter message: "))

bytesToSend = str.encode(msgFromClient)

#serverAddressPort = ("192.168.10.110", 12345)
serverAddressPort = ("127.0.0.1", 12345)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

print("Encrypted message sent")

# Output:
# Enter message: hello
# Encrypted message sent
