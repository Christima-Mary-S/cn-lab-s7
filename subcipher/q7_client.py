# Reg No: 20219030
# Name: Christima Mary S
# Program No: 7

import socket
import string


# A list containing all characters
all_letters= string.ascii_letters


def encrypt(pt, key=4):
	dict1 = {}
	for i in range(len(all_letters)):
		dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]

	ct = []
	# loop to generate ciphertext
	for char in pt:
		if char in all_letters:
			temp = dict1[char]
			ct.append(temp)
		else:
			temp = char
			ct.append(temp)
			
	ct = "".join(ct)
	return ct


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
