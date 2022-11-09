#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import socket
import random

ports=[]
pfile=open('ports.txt','w')

def myServ():
    while True:
        while os.stat('ports.txt').st_size == 0:
            True
        host = ''
        with open("ports.txt", "r") as pfile:
            lines = pfile.readlines()
            port = int(lines[-1])
        if port not in ports:
            ports.append(port)
        else:
            while True:
                port = random.randint(1024, 65535)
                if port not in ports:
                    ports.append(port)
                    pfile = open("ports.txt", "a+")
                    pfile.write("\n" + str(port))
                    pfile.close()
                    break
        with open("ports.txt", "r") as pfile:
            lines = pfile.readlines()
            port = int(lines[-1])
        with socket.socket() as sock:
            sock.bind((host, port))
            print("", port)
            sock.listen()
            conn, addr = sock.accept()
            print('Подключение...', host)
            with conn:
                msg = ''
                while True:
                    data = conn.recv(1024)
                    print("Получение данных от клиента", data)
                    if not data:
                        break
                    msg = data.decode()
                    print("Отправление данных клиенту")
                    conn.send(data)
        print("Отключение...")
        cont = input("Нажмите enter чтобы продолжить или введите end чтобы остановить")
        if cont == 'end':
            break
        else:
            continue

print("Запуск сервера")
myServ()
print("Прекращение работы сервера")
pfile.close()


# In[ ]:




