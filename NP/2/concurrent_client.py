import socket
def tcp_echo_client(server_host='127.0.0.1', server_port=22222):
      #create a TCP socket
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            #connect to the server
            client_socket.connect((server_host, server_port))

            while True:
                  message = input("Enter message to send (or 'exit' to quit):")
                  if message.lower() == 'exit':
                        break
                    #send message to the server
                  client_socket.sendall(message.encode())
                    #Receive the echo from the server
                  echoed_message = client_socket.recv(1024)
                  print(f"Echoed message from server:{echoed_message.decode()}")
      client_socket.close()

if __name__=="__main__":
      tcp_echo_client ()