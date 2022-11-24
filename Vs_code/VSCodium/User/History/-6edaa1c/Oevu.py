def check_user(username,age=0):

	print(f'Hello {username}!')


	if age >= 21:
		print('Welcom to the club')

	print('-'*20)


check_user(username='Oleg', age=10)
check_user(username='Svetlana', age=22)

