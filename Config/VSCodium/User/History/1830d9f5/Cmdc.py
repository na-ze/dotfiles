def say_hello(username, age):
# username - это параметр функции  

    print(f'helo {username}!')
    print(f'you age is {age}!' )
    print('-'*20)

#ay_hello('Valera', 20)
#say_hello('mr.Andrey', 30)
say_hello(username='Alex', age=35)
say_hello(age= 40,username='Anna')
#а вот валерчик это уже аргумент