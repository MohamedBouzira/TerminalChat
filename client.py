import socket
import threading
import sys

#server socket:
serveraddr = ('127.0.0.1' , 8000)
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#username
username = input('welcome to terminalChat \n please enter your username: ')

#connect to the server 
try:
    serversocket.connect(serveraddr)
except Exception as e:
    print(e)

print('you connect to the server press ")" to exit')

#sending username:
serversocket.sendall(username.encode())


#the second thread (receiving messages):
def handling_message():
    while True:
        try:
            message = serversocket.recv(1024).decode()
            if not message:
                break
            
            sys.stdout.write(f'\r{message}\n{username}: ')      #wring in standard output > print
            sys.stdout.flush()

        except:
            break

threading.Thread(target= handling_message, daemon= True).start()

#the main thread (sending messages):
while True:
    message = input(f'{username}: ')
    if (message == ')'):
        print('exiting ...')
        serversocket.close()
        break
    serversocket.sendall(message.encode())
    