import socket
import threading

def handle_client(client_socket, client_address):
      print(f"New connection from {client_address}")

      with client_socket:
           while True:
                 #Receive message from the client
                 message = client_socket.recv(1024)
                 if not message:
                     break
                 print(f"Received message from {client_address} : {message.decode()}")

                 # Send the message back to the client (echo)
                 client_socket.sendall(message)
                
      print(f"Connection from {client_address} closed")

def tcp_concurrent_echo_server(host='127.0.0.1', port=22222):
      #create a TCP socket
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(5)  #Listen for incoming connections
            print(f"TCP server listening on {host}:{port}")

            while True:
                    #Accept  a connection from a client
                    client_socket,client_address=server_socket.accept()
                    client_thread = threading .Thread(target=handle_client, args=(client_socket,client_address))
                    client_thread.start()
      server_socket.close()

if __name__ == "__main__" :
        tcp_concurrent_echo_server()