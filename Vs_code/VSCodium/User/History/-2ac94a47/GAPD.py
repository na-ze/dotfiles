import turtle

window = turtle.Screen()
# задаём окно 

pan = turtle.Turtle()
# pan - задали карандашик

speed = 1

def Speed_up():
	global speed
# обьявляем speed глобальной  
	speed + 2


def Speed_down():
	global speed
#
	speed - 2







window.mainloop()