import socket
import requests
def parse(req):
	first_line = str(req.split('\r'))
	header_line = first_line.split(" ")
	request_type =  header_line[0]
	host_name = header_line[1]
	print(request_type,host_name)
	#return host_name
# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 3600

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    req = client_connection.recv(1024).decode()
    print(req)
    parse(req)
    #response = requests.get(host_name)
    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\nHello World'
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()
