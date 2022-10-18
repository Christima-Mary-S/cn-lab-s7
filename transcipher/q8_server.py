# Reg No: 20219030
# Name: Christima Mary S
# Program No: 8

import socket
import math


# Decryption
def decrypt(cipher, key="CUSAT"):
	msg = ""

	# track key indices
	k_indx = 0

	# track msg indices
	msg_indx = 0
	msg_len = float(len(cipher))
	msg_lst = list(cipher)

	# calculate column of the matrix
	col = len(key)
	
	# calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# convert key into list and sort
	# alphabetically so we can access
	# each character by its alphabetical position.
	key_lst = sorted(list(key))

	# create an empty matrix to
	# store deciphered message
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	#print(f"msg_len: {msg_len}, msg_lst: {msg_lst}, key_lst: {key_lst}")
	#print(dec_cipher)

	# Arrange the matrix column wise according
	# to permutation order by adding into new matrix
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1
		#print(f"dec_cipher is now: {dec_cipher}")

	# convert decrypted msg matrix into a string
	try:
		msg = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot",
						"handle repeating words.")

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]

	return msg


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
# Encrypted message: lhloe
# Decrypted message: hello
# Client IP Address:('127.0.0.1', 57717)
