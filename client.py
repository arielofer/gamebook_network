import socket


HOST = '127.0.0.1'
PORT = 6543

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        message = bytes(input(), 'utf-8')
        socket.send(message)
        data = socket.recv(1024)
        if message.decode('utf-8') == "quit":
            socket.close()
            break
        print(data)
