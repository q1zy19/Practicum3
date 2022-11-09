#!/usr/bin/env python
# coding: utf-8

# In[2]:


import socket
import random

while True:
    port = input('Введите порт для подключения клиента: ')
    if port.isdigit():
        if 1024 <= int(port) <= 65535:
            port = int(port)
            with open("ports.txt", "r+") as pfile:
                pfile.write(str(port))
            break
        else:
            print('Значение порта должно быть между 1024 и 65535')
    else:
        print('Неверное значение порта')

while True:
    flag=False
    host=input('Введите хост: ')
    phost=host.split('.')
    for i in range(len(phost)):
            if  len(phost) == 4:
                if phost[i].isdigit():
                    if 0 <= int(phost[i]) <= 255:
                        flag = True
                    else:
                        flag = False
                        break
                else:
                    flag=False
                    break
            else:
                break
    if flag==True:
        break

    print('Неверное значение')
file=open('Сlient.txt', 'a+')
cli=0
with open('Сlient.txt','r') as f:
    for line in f:
        list_words = line.split()
        if host in line:
            name = list_words[-2]
            passwd=list_words[-1]
            cli = 1
if cli!=1:
    name = input('Введите имя: ')
    passwd = input('Сlient: ')
    file.write(host + ' ')
    file.write(name + ' ')
    file.write(passwd+ ' ')
file.close()
while True:
    if_passwd=input('Введите ваш пароль: ')
    if if_passwd!=passwd:
        print('Неверный пароль')
    else:
        break
while True:
    with open("ports.txt", "r") as pfile:
        lines = pfile.readlines()
        port = int(lines[-1])
    with socket.socket() as sock:
        print('Добро пожаловать,'+name+'!')
        sock.connect((host, port))
        print("Полученные данные от клиента: ")
        while True:
            msg = input('Введите значение (end для выхода)')
            if msg == 'end':
                break
            sock.send(msg.encode())
            print("Отправление данных серверу")
            data = sock.recv(1024)
            print('Получение данных от сервера:', repr(data))
    print("Соединение с сервером прервано")
    break
pfile=open('ports.txt','w')
pfile.close()


# In[ ]:




