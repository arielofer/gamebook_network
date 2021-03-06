import socket
import json

HOST = '127.0.0.1'
PORT = 6543

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        data_string = socket.recv(1024)
        message = json.loads(data_string)
        if message["type"] == "input":
            answer = input(message["data"])
            answer_message = {"data": answer, "type": "input-answer"}
            answer_message_string = json.dumps(answer_message)
            socket.send(bytes(answer_message_string, 'utf-8'))
        if message["type"] == "output":
            print(message["data"])
            if message["data"] == "you reached the end - game over"\
               or message["data"] == "exiting...":
                break
