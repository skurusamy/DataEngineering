import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 3600))
msg = raw_input("Enter your message: Say bye to leave- ")
print(msg)
while msg.upper() != 'BYE':
	client.send(msg)
	msg = raw_input("Enter your message: Say bye to leave- ")
client.close()
