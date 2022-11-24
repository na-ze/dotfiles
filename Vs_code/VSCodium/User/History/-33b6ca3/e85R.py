from tkinter import*
tk = Tk()
w = 500
h = 500
w_img = 100
canvas = Canvas(tk, width=w, height=h)
tk.title("Rich dada, yeeeeh")
canvas.pack()
rich_dada=PhotoImage(file="дед.png")
id_img=canvas.create_image(50,50,image =rich_dada)
Button(tk, text = "Rich daddy").pack(side='right')
print(id_img)
#_________________
canvas.mainloop()