import socket

def run_server(host="127.0.0.1",port=65432) :
    print("="*61) 
    print(" "*25+"SERVER SIDE")
    print("="*61+"\n") 
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket :   # Create the socket object
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)      # To allow the immediate use of the port after stopping the server
        server_socket.bind((host,port))                                        # Bind the socket to the host and port
        server_socket.listen()                                                 # Enable the server for connection
        print(f"The server is listening on {host} : {port}\n")                    

        conn , adr=server_socket.accept()                                      # Wait for an incoming connection

        with conn :
            print(f"The server is connected to {adr}\n")
           
            while True :

                data=conn.recv(1024)                                          # Receive data from the client (buffer size of 1024 bytes)

                if not data :                                                 # No data means the client closed the connection
                    print(f"The connection is closed by {adr}\n")
                    break

                print(f"The received message is : {data.decode('utf-8')}")    

                conn.sendall(data)                                            # Echo back the data to the client
                print(f"Echoed back             : {data.decode('utf-8')}\n")



if __name__ == "__main__" :
    run_server()



                

          





