#chat_client.py
import socket
import threading
SERVER_HOST = 'localhost'  
SERVER_PORT = 5000         
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except ConnectionResetError:
            print("Connection to the server was closed.")
            client_socket.close()
            break
def send_message(client_socket):
      while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to the server.")
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()
send_thread = threading.Thread(target=send_message, args=(client_socket,))
send_thread.start()
if __name__ == '__main__':
    start_client()