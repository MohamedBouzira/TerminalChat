import socket 
import threading

#list of the clients that currenctly on server
clients = []

#server address and port
host = '127.0.0.1'
port = 8000

#waiting for connection
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.bind((host,port))
clientsocket.listen(5)
print(f'server is listening on {port}')

#send message to all the clients
def broadcast(client,message,username):
    for c in clients:
        if (c != client):
            try:
                c.sendall(f'{username}: {message}'.encode())
            except:
                clients.remove(c)
                c.close()


#the second thread (receiving messages and broadcast it):
def handle_client(client):
    username = client.recv(1024).decode()
    print(f'new connection from : {username} , {addr}')

    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(f'{username}: {message}')
            
            broadcast(client,message,username)
        
        except:
            break

    
    print(f'{username} disconnected...')
    client.close()
    clients.remove(client)


#main thread (add clients to list )
while True:
    client, addr = clientsocket.accept()
    clients.append(client)
    threading.Thread(target= handle_client, args=(client,)).start()