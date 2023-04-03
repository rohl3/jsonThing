import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAdd = ('localhost', 5000)
server.bind(serverAdd)

server.listen(1)

client, clientAddress = server.accept()
data = client.recv(1024)
dataJSON = json.loads(data)
print(dataJSON)
result = {
    'Name': 'Rohit',
    'Surname': 'Verma'
}
resultJSON = json.dumps(result)
client.sendall(resultJSON.encode())
client.close()
server.close()
