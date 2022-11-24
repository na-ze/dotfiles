from tkinter import*
tk = Tk()
w = 1000
h = 1000
w_img = 500
canvas = Canvas(tk, width=w, height=h)
tk.title("donute")
canvas.pack()
ponchick = PhotoImage(file="img/donut.png")
id_img = canvas.create_image(400,400, image=ponchick)
print(id_img)
canvas.mainloop()