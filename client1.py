import socket

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
porta = 2222

name = str(input('Digite seu nick: '))
print('entrando no BatePapo')
cliente.connect((host, porta))

loop = True
while loop:
    mensagem = str(input('Mensagem: '))
    cliente.send(f'{name}: {mensagem}'.encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    print(msg)

cliente.close()
