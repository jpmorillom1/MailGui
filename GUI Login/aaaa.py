import tkinter as tk
from tkinter import PhotoImage

app = tk.Tk()
app.title("Label con imagen")

imagen = PhotoImage(file="F:/GUI Login/imagenes/icon.png")

GLabel_468 = tk.Label(app, image=imagen, bg="#ff0000", text="LOGO", compound="top", font=("Times", 10), fg="#333333", justify="center")
GLabel_468.place(x=0, y=0, width=100, height=100)

app.mainloop()