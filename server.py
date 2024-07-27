import socket, ast, pickle

server = socket.socket()
#host = "MYserverHARD"
host = socket.gethostname()
port = 55555  # устанавливаем порт сервера
server.bind((host, port))  # привязываем сокет сервера к хосту и порту


while True:
    server.listen(5)  # начинаем прослушиваение входящих подключений
    con, addr = server.accept()  # принимаем клиент
    try:
        while True:
            message = con.recv(400000000)  # сообщение для отправки клиенту
            message = message.decode()
            message = ast.literal_eval(message)
            if message[0] == 1:
                message.pop(0)
                otv = 0
                if message[0] == 'Ученик':
                    with open("st.pickle", "rb") as f:
                        st = pickle.load(f)
                    for i in st:
                        if i[-1] == message[-1] and i[-2] == message[-2]:
                            otv = 1
                    if otv == 0:
                        st.append(message)
                    with open('st.pickle', 'wb') as f:
                        pickle.dump(st, f)
                else:
                    with open("ch.pickle", "rb") as f:
                        ch = pickle.load(f)
                    for i in ch:
                        if i[-1] == message[-1] and i[-2] == message[-2]:
                            otv = 1
                    if otv == 0:
                        ch.append(message)
                    with open('ch.pickle', 'wb') as f:
                        pickle.dump(ch, f)
                con.send(str(otv).encode())
                con.close()
                break
            elif message[0] == 2:
                message.pop(0)
                otv = 0
                if message[0] == 'Ученик':
                    with open("st.pickle", "rb") as f:
                        st = pickle.load(f)
                    for i in st:
                        if i[-1] == message[-1] and i[-2] == message[-2]:
                            otv = 1
                else:
                    with open("ch.pickle", "rb") as f:
                        ch = pickle.load(f)
                    for i in ch:
                        if i[-1] == message[-1] and i[-2] == message[-2]:
                            otv = 1
                con.send(str(otv).encode())
                con.close()
                break
            elif message[0] == 3:
                message.pop(0)
                otv = 0
                if message[0] == "Ученик":
                    pass
                else:
                    with open("ch.pickle", "rb") as f:
                        ch = pickle.load(f)
                    for i in ch:
                        if i[-1] == message[-1] and i[-2] == message[-2]:
                            otv = i[5]
                    con.send(str(otv).encode())
                con.close()
                break
    finally:
        pass