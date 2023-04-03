import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
client.connect(server_address)

data = {
    'Surname': 'Verma',
    'Name': 'Rohit'
}
client.sendall(json.dumps(data).encode())
response = client.recv(1024)
result = json.loads(response)

print(result)
client.close()
