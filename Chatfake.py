import socket
import threading
import cezar
nickname = input("Введіть ім'я користувача : ").strip()
while not nickname:
    nickname = input("Це поле не може бути порожнім : ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.150"
port = 1339
code = 1
my_socket.connect((host, port))
receive1 = input("Щоб зашифрувати повідомлення натисніть 1:")
def thread_sending():
    while True:
        message_to_send = str(input(''))
        code = int(input('Натисніть 2 щоб відправити повідомлення'))
        if message_to_send:
            if code == 2:
                message_to_send = cezar.myencode(message_to_send)
                message_with_nickname = nickname + " : " + message_to_send
            else:
                message_with_nickname = nickname + " : " + message_to_send
            my_socket.send(message_with_nickname.encode())
def thread_receiving():
    while True:
        if receive1 == 1:
            message = my_socket.recv(1024).decode()
            print(cezar.mydecode(message))
        else:
            message = my_socket.recv(1024).decode()
            print(message)
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()