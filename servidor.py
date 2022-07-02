import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
porta = 2222

server.bind((host, porta))

server.listen()
client, end = server.accept()
print(f'Client IP({end[0]}) ID({end[1]}) Se conectou')
name = 'ServerHelp'

loop = True
while loop:
    msg = client.recv(1024).decode('utf-8')
    print(msg)
    mensagem = str(input('Mensagem: '))
    client.send(f'{name}: {mensagem}'.encode('utf-8'))

client.close()
server.close()
