from tkinter import*
tk = Tk()
w = 100
h = 100
canvas = Canvas(tk, width=w, height=h)
tk.title("donute")
canvas.pack()
ponchick = PhotoImage(file="img/donut.png")
id_img = canvas.create_image(100,100, image=ponchick)
print(id_img)
canvas.mainloop()