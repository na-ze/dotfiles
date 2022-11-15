from tkinter import*
tk = Tk()
w = 1000
h = 1000
canvas = Canvas(tk, width=w, height=h)
tk.title("donute")
canvas.pack()
ponchick = PhotoImage(file="img/donut.png")
id_img = canvas.create_image(50,50, image=ponchick)
print(id_img)
canvas.mainloop()