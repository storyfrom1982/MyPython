message = ''
active = True
while active:
    if message == 'quit':
        active = False
    elif message == 'break':
        break
    else:
        message = input("输入信息:")
        print(message)