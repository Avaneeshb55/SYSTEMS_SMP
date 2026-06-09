import socket 

def run_client(host="127.0.0.1",port=65432):
    print("="*61) 
    print(" "*25+"CLIENT SIDE")
    print("="*61+"\n") 
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket :    # Create a socket using IPv4 and TCP
        client_socket.connect((host,port))                                      # To connect the server 
        print(f"Connected to the server at {host} : {port}\n")

        message = "Hello !, This is an echo test ."
        print(f"Sending the message  : {message}")                           
 
        client_socket.sendall(message.encode('utf-8'))                          # To send the message to the server

        data=client_socket.recv(1024)                                           # To receive back the sent data
        print(f"The received data is : {data.decode('utf-8')}\n")


if __name__ == "__main__" :
    run_client()


