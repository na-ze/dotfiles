from tkinter import *
'''import random'''
tk = Tk()
# создаём рабочую область
w = 500
h = 500
# размеры всего (тк)
w_img = 100
# размеры картинки
canvas = Canvas(tk, width=w, height=h)
# размеры самой РАБОЧЕЙ области
tk.title("Rich dada, yeeeeh")
canvas.pack()
rich_dada = PhotoImage(file="img/богатый дядя.png")
id_img = canvas.create_image(50, 50, image=rich_dada)
Button(tk, text="Rich daddy").pack(side='right')
print(id_img)
# _________________
canvas.mainloop()
