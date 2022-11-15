def say_hello(username, age):
	""" def - world for создания функции"""
	"""say_hello - название функции, ONLY на англ. языке"""
	#todo(username, age) - это ПАРАМЕТРЫ функции """
	print(f'helo {username}!')
	print(f'you age is {age}!' )
	print('-'*20)
	"""say_hello - затем мы вызваем функцию, тем самым завершаем её"""
	#todo('Valera', 20) - это же АРГУМЕНТЫ функции, мы ими задём значения параметров"""
#say_hello('Valera', 20)
#say_hello('mr.Andrey', 30)
say_hello(username='Alex', age=35)
#!это так называймые ИМЕННОВАНЫЙ аргумент,представляет собой пару в виде имени(usernamу) и значения('Alex')
#! в таком случае не возникает путаницы в праграмме Example: helo 35! 
say_hello(age= 40,username='Anna')
#а вот валерчик это уже аргумент