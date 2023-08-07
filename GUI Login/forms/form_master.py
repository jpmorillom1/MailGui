import tkinter as tk
from tkinter import Image, ttk
from tkinter.font import BOLD
from tkinter.tix import IMAGETEXT
import util.generic as utl
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import PhotoImage
from PIL import Image, ImageTk

class MasterPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bandeja de Entrada")
        width=1280
        height=720
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        

        # Crear el Treeview para la tabla
        self.tabla = ttk.Treeview(self, columns=("remitente", "correo", "fecha"))
        self.tabla.heading("#0", text="Botón")
        self.tabla.heading("remitente", text="Remitente")
        self.tabla.heading("correo", text="Correo")
        self.tabla.heading("fecha", text="Fecha")
        
        # Insertar datos de ejemplo en la tabla
        self.insertar_fila("Juan", "juan@example.com", "2023-08-06")
        self.insertar_fila("María", "maria@example.com", "2023-08-07")
        self.insertar_fila("Carlos", "carlos@example.com", "2023-08-08")
        self.insertar_fila("Laura", "laura@example.com", "2023-08-09")

        # Ajustar el tamaño de las columnas
        self.tabla.column("#0", width=100)
        self.tabla.column("remitente", width=150)
        self.tabla.column("correo", width=200)
        self.tabla.column("fecha", width=100)

        # Agregar scrollbars a la tabla
        scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        scroll_y.pack(side="right", fill="y")
        self.tabla.configure(yscrollcommand=scroll_y.set)

        # Mostrar la tabla
        self.tabla.place(x=260, y=100, width=1020, height=620)
        

        GLabel_241=tk.Label(self)
        GLabel_241["bg"] = "#432959"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_241["font"] = ft
        GLabel_241["fg"] = "#333333"
        GLabel_241["justify"] = "center"
        GLabel_241["text"] = "label"
        GLabel_241.place(x=0,y=0,width=1278,height=100)
        

        image = Image.open("./imagenes/icon1.png")  
        image = image.resize((50, 50))  
        photo = ImageTk.PhotoImage(image)
        GButton_382 = tk.Button(self, image=photo, command=self.GButton_382_command)
        GButton_382.image = photo  
        GButton_382["relief"] = "flat"
        GButton_382.place(x=130,y=30,width=50,height=50)

        image = Image.open("./imagenes/icon2.png")  
        image = image.resize((50, 50))  
        photo = ImageTk.PhotoImage(image)
        GButton_83=tk.Button(self, image=photo)
        GButton_83.image = photo 
        GButton_83["relief"] = "flat"
        GButton_83.place(x=190,y=30,width=50,height=50)
        GButton_83["command"] = self.GButton_83_command

        GLineEdit_820=tk.Entry(self)
        GLineEdit_820["bg"] = "#ffffff"
        GLineEdit_820["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_820["font"] = ft
        GLineEdit_820["fg"] = "#333333"
        GLineEdit_820["justify"] = "center"
        GLineEdit_820["text"] = "Buscar contactos"
        GLineEdit_820.place(x=330,y=30,width=570,height=35)

        image = Image.open("./imagenes/icon.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        GLabel_468=tk.Label(self,image=photo)
        GLabel_468.image = photo
        GLabel_468["bg"] = "#ff0000"
        GLabel_468.place(x=0,y=0,width=100,height=100)


        GLabel_647=tk.Label(self)
        GLabel_647["bg"] = "#e9efeb"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_647["font"] = ft
        GLabel_647["fg"] = "#333333"
        GLabel_647["justify"] = "center"
        GLabel_647["text"] = "label"
        GLabel_647.place(x=0,y=100,width=260,height=616)


        image = Image.open("./imagenes/panel1.png")  
        image = image.resize((260, 80))  
        photo = ImageTk.PhotoImage(image)
        GButton_843=tk.Button(self,image=photo)
        GButton_843.image = photo 
        GButton_843["relief"] = "flat"
        GButton_843["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        GButton_843["font"] = ft
        GButton_843["fg"] = "#000000"
        GButton_843["justify"] = "center"
        GButton_843["text"] = "Correo nuevo"
        GButton_843.place(x=0,y=110,width=260,height=80)
        GButton_843["command"] = self.GButton_843_command

        image = Image.open("./imagenes/panel2.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        GButton_746=tk.Button(self,image=photo)
        GButton_746.image = photo 
        GButton_746["relief"] = "flat"
        GButton_746["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_746["font"] = ft
        GButton_746["fg"] = "#000000"
        GButton_746["justify"] = "center"
        GButton_746["text"] = "Contactos"
        GButton_746.place(x=0,y=210,width=260,height=50)
        GButton_746["command"] = self.GButton_746_command


        image = Image.open("./imagenes/panel3.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        GButton_226=tk.Button(self,image=photo)
        GButton_226.image = photo 
        GButton_226["relief"] = "flat"
        GButton_226["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_226["font"] = ft
        GButton_226["fg"] = "#000000"
        GButton_226["justify"] = "center"
        GButton_226["text"] = "Grupos"
        GButton_226.place(x=0,y=260,width=260,height=50)
        GButton_226["command"] = self.GButton_226_command


        image = Image.open("./imagenes/panel4.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        GButton_544=tk.Button(self,image=photo)
        GButton_544.image = photo 
        GButton_544["relief"] = "flat"
        GButton_544["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_544["font"] = ft
        GButton_544["fg"] = "#000000"
        GButton_544["justify"] = "center"
        GButton_544["text"] = "Recibidos"
        GButton_544.place(x=0,y=330,width=260,height=50)
        GButton_544["command"] = self.GButton_544_command


        image = Image.open("./imagenes/panel5.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        GButton_251=tk.Button(self,image=photo)
        GButton_251.image = photo 
        GButton_251["relief"] = "flat"
        GButton_251["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_251["font"] = ft
        GButton_251["fg"] = "#000000"
        GButton_251["justify"] = "center"
        GButton_251["text"] = "Enviados"
        GButton_251.place(x=0,y=380,width=260,height=50)
        GButton_251["command"] = self.GButton_251_command


        image = Image.open("./imagenes/panel6.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        GButton_421=tk.Button(self,image=photo)
        GButton_421.image = photo 
        GButton_421["relief"] = "flat"
        GButton_421["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_421["font"] = ft
        GButton_421["fg"] = "#000000"
        GButton_421["justify"] = "center"
        GButton_421["text"] = "Eliminados"
        GButton_421.place(x=0,y=430,width=260,height=50)
        GButton_421["command"] = self.GButton_421_command


        GLabel_475=tk.Label(self)
        GLabel_475["bg"] = "#432959"
        ft = tkFont.Font(family='Times',size=15)
        GLabel_475["font"] = ft
        GLabel_475["fg"] = "#ffffff"
        GLabel_475["justify"] = "center"
        GLabel_475["text"] = "Bienvenido "
        GLabel_475.place(x=1070,y=30,width=200,height=35)

        

    def insertar_fila(self, remitente, correo, fecha):
        # Insertar una nueva fila en la tabla
        self.tabla.insert("", "end", values=(remitente, correo, fecha))

    def GButton_746_command(self):
        # Acción cuando se hace clic en el botón "Contactos"
        print("Botón Contactos clicado")  

    def GButton_382_command(self):
        print("command")


    def GButton_83_command(self):
        print("command")


    def GButton_843_command(self):
        print("command")


    def GButton_746_command(self):
        print("command")


    def GButton_226_command(self):
        print("command")


    def GButton_544_command(self):
        print("command")


    def GButton_251_command(self):
        print("command")


    def GButton_421_command(self):
        print("command")
    

        


   

