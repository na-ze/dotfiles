#----------------------------------------------------------------def#1--------------------------------------------------------------------

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
	#todo A вот 'Alex/Anna' это уже аргумент!
#----------------------------------------------------------------def#2--------------------------------------------------------------------

def number_sum(username,num1=1,num2=2):

#!Very Inportant - если в функции есть параметры со заначениями, они должны следовать строго после параметров у которых значений...
#!...по умолчанию нет, это для того, чтобы Python правильно интопретировал позиционные аргументы, если изменим порядок, то получим ошибку!

#todo(num1=1,num2=2) - для каждого параметра нашей функции мы можем задавать значения по умолчанию!
#?(num1=2,num2=7) - так если при вызове функции передаётся АРГУМЕНТ, python будет использовать его значение в качестве параметра!
#todo а если же нет[number_sum()], то будут использовать параметры по умолчанию

	print(f'Hello {username}!')
	print(num1+num2)
	print("-"*20)

number_sum('Oleg', num1=2,num2=7)
number_sum('Oleg', num1=13,num2=5)
number_sum('Oleg', num1=78,num2=349)
number_sum('Oleg')
number_sum('Oleg', num1=78)
#todo если я задам значение ток 1-му параметру, то 2-ому будет присвоено стандартное значение


number_sum(username='Olga', num1 = 78)


#----------------------------------------------------------------def#3--------------------------------------------------------------------

def check_user(username,age=0):

	print(f'Hello {username}!')


	if age >= 21:
		print('Welcom to the club')

	print('-'*20)


check_user(username='Oleg')
check_user(username='Svetlana', age=22)















