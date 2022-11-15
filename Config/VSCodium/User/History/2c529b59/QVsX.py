from tkinter import*
tk = Tk()
w = 500
h = 500
w_img = 100
canvas = Canvas(tk, width=w, height=h)
tk.title("donute")
canvas.pack()
ponchick = PhotoImage(file="img/donut.png")
id_img = canvas.create_image(50,50, image=ponchick)
print(id_img)
canvas.mainloop()