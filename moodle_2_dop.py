def new_password(num): # объявляем функцию
    password = ''
    for i in range(1, num): #подбираем первое число
        for j in range(2, num): # подбираем второе число
            if j <= i:
                continue
            if num % (i + j) == 0:
                password += str(i) + str(j) # формируем пароль
    return password
n = int(input('Введите целое число от 3 до 20: '))
result = new_password(n)
print('Пароль:', result)