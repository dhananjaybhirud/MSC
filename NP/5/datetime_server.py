import socket
import datetime
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)
print('Daytime server is listening on {}:{}'.format(SERVER_IP, SERVER_PORT))
while True:
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    client_socket.send(current_datetime.encode())
    client_socket.close()