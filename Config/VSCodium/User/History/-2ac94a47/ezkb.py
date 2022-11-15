import turtle

window = turtle.Screen()
# задаём окно 

pen = turtle.Turtle()
# pen - задали карандашик
# почему turtle, потмоу что pen и есть черпешка
speed = 1

def Speed_up():
	global speed
# обьявляем speed глобальной  
	speed + 2


def Speed_down():
	global speed
#
	speed - 2

#---------------------------------------------------------------------------------------------------------------------------------------

def Move_up():
	x = pen.position()[0]
# мы поднимаем черепашку по кординатом(y) на 1, а по (x) на 0
	y = pen.position()[1]





def MOve_down():
	x = pen.position()[0]
	y = pen.position()[-1]




window.mainloop()