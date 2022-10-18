# Reg No: 20219030
# Name: Christima Mary S
# Program No: 7

import socket
import string


# A list containing all characters
all_letters= string.ascii_letters

def decrypt(ct, key=4):
	dict2 = {}	
	for i in range(len(all_letters)):
		dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]

	pt = []
	# loop to recover plain text
	for char in ct:
		if char in all_letters:
			temp = dict2[char]
			pt.append(temp)
		else:
			temp = char
			pt.append(temp)
			
	pt = "".join(pt)
	return pt


#localIP = "192.168.10.108"
localIP = "localhost"

localPort = 12345

bufferSize = 1024
 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("Server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0].decode("utf-8")

    address = bytesAddressPair[1]

    print(f"Encrypted message: {message}")
    decryptedMsg = decrypt(message)
    print(f"Decrypted message: {decryptedMsg}")
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientIP)

# Output:
# Server up and listening
# Encrypted message: lipps
# Decrypted message: hello
# Client IP Address:('127.0.0.1', 51003)
