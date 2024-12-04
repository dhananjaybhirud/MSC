import socket
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
print('Connected to {}:{}'.format(SERVER_IP, SERVER_PORT))
current_datetime = client_socket.recv(1024).decode()
print('Current date and time: {}'.format(current_datetime))
client_socket.close()
