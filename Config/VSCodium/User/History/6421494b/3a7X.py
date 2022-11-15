from tkinter import *
'''import random'''
tk = Tk()
# создаём область
w = 500
h = 500
# размеры всего (тк)
w_img = 10
# размеры картинки
canvas = Canvas(tk, width=w, height=h)
# размеры самой РАБОЧЕЙ области
tk.title("Rich dada, yeeeeh")
#!задаём название tk
canvas.pack()
# размещаем какой-то элемент на Canvas с помощью pack()
rich_dada = PhotoImage(file="img/богатый дядя.png")
# todo с помощью PhotoImage() мы задаём фотографию, дальше мы задаём путь к фотке (file="путь к файлу")
id_img = canvas.create_image(50, 50, image=rich_dada)
'''id_img - это мы обращаемся к картинке дальше, =canvas. мы указавыем где эта картинка, дальше create_image() делаем картинку видимой! на канвасе'''
#!потом мы в() задём сначала размеры, потом мы присваеваем имееного этому id_img название image=rich_dada
Button(tk, text="Rich daddy").pack(side='right')
# Button - задаём кнопку
# (tk, text="Rich daddy") - указываем сначала где она будет находиться (tk), а потом сам текст text="Rich daddy"
# .pack(side='right') - где мы распологаем фотку, а в () указываем КОНКРЕТНО (side='right')
print(id_img)
# _________________
canvas.mainloop()
# мы сами выбираем когда мы закроется окно
# иначе оно закроется сразу же
