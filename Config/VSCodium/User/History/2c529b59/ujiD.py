from tkinter import*
tk = Tk()
w = 500
h = 800
w_img = 1000
canvas = Canvas(tk, width=w, height=h)
tk.title("donute")
canvas.pack()
ponchick = PhotoImage(file="img/donut.png")
id_img = canvas.create_image(400,400, image=ponchick)
print(id_img)
canvas.mainloop()