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
        self.tabla = ttk.Treeview(self, columns=("0","remitente", "correo", "fecha"))
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
        self.tabla.column("#0", width=20)
        self.tabla.column("remitente", width=150)
        self.tabla.column("correo", width=200)
        self.tabla.column("fecha", width=100)
        # Agregar scrollbars a la tabla
        scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        scroll_y.pack(side="right", fill="y")
        self.tabla.configure(yscrollcommand=scroll_y.set)
        # Mostrar la tabla
        self.tabla.place(x=260, y=100, width=1020, height=620)
        


        LabelBarraSuperior=tk.Label(self)
        LabelBarraSuperior["bg"] = "#432959"
        ft = tkFont.Font(family='Times',size=10)
        LabelBarraSuperior["font"] = ft
        LabelBarraSuperior["fg"] = "#333333"
        LabelBarraSuperior["justify"] = "center"
        LabelBarraSuperior["text"] = "label"
        LabelBarraSuperior.place(x=0,y=0,width=1280,height=100)
        

        image = Image.open("./imagenes/icon1.png")  
        image = image.resize((50, 50))  
        photo = ImageTk.PhotoImage(image)
        BotonAddContact = tk.Button(self, image=photo, command=self.BotonAddContact_command)
        BotonAddContact.image = photo  
        BotonAddContact["relief"] = "flat"
        BotonAddContact.place(x=130,y=30,width=50,height=50)

        image = Image.open("./imagenes/icon2.png")  
        image = image.resize((50, 50))  
        photo = ImageTk.PhotoImage(image)
        BotonAddGroup=tk.Button(self, image=photo)
        BotonAddGroup.image = photo 
        BotonAddGroup["relief"] = "flat"
        BotonAddGroup.place(x=190,y=30,width=50,height=50)
        BotonAddGroup["command"] = self.BotonAddGroup_command
        
        image = Image.open("./imagenes/icon.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        LabelLogo=tk.Label(self,image=photo)
        LabelLogo.image = photo
        LabelLogo["bg"] = "#ff0000"
        LabelLogo.place(x=0,y=0,width=100,height=100)

        LineEditBuscador=tk.Entry(self)
        LineEditBuscador["bg"] = "#ffffff"
        LineEditBuscador["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        LineEditBuscador["font"] = ft
        LineEditBuscador["fg"] = "#333333"
        LineEditBuscador["justify"] = "center"
        LineEditBuscador["text"] = "Buscar contactos"
        LineEditBuscador.place(x=330,y=30,width=570,height=35)

        


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
        BotonEnviar=tk.Button(self,image=photo)
        BotonEnviar.image = photo 
        BotonEnviar["relief"] = "flat"
        BotonEnviar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        BotonEnviar["font"] = ft
        BotonEnviar["fg"] = "#000000"
        BotonEnviar["justify"] = "center"
        BotonEnviar["text"] = "Correo nuevo"
        BotonEnviar.place(x=0,y=110,width=260,height=80)
        BotonEnviar["command"] = self.BotonEnviar_command

        image = Image.open("./imagenes/panel2.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        BotonContactos=tk.Button(self,image=photo)
        BotonContactos.image = photo 
        BotonContactos["relief"] = "flat"
        BotonContactos["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        BotonContactos["font"] = ft
        BotonContactos["fg"] = "#000000"
        BotonContactos["justify"] = "center"
        BotonContactos["text"] = "Contactos"
        BotonContactos.place(x=0,y=210,width=260,height=50)
        BotonContactos["command"] = self.BotonContactos_command


        image = Image.open("./imagenes/panel3.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        BotonGrupos=tk.Button(self,image=photo)
        BotonGrupos.image = photo 
        BotonGrupos["relief"] = "flat"
        BotonGrupos["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        BotonGrupos["font"] = ft
        BotonGrupos["fg"] = "#000000"
        BotonGrupos["justify"] = "center"
        BotonGrupos["text"] = "Grupos"
        BotonGrupos.place(x=0,y=260,width=260,height=50)
        BotonGrupos["command"] = self.BotonGrupos_command


        image = Image.open("./imagenes/panel4.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        BotonRecibidos=tk.Button(self,image=photo)
        BotonRecibidos.image = photo 
        BotonRecibidos["relief"] = "flat"
        BotonRecibidos["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        BotonRecibidos["font"] = ft
        BotonRecibidos["fg"] = "#000000"
        BotonRecibidos["justify"] = "center"
        BotonRecibidos["text"] = "Recibidos"
        BotonRecibidos.place(x=0,y=330,width=260,height=50)
        BotonRecibidos["command"] = self.BotonRecibidos_command


        image = Image.open("./imagenes/panel5.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        BotonEnviados=tk.Button(self,image=photo)
        BotonEnviados.image = photo 
        BotonEnviados["relief"] = "flat"
        BotonEnviados["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        BotonEnviados["font"] = ft
        BotonEnviados["fg"] = "#000000"
        BotonEnviados["justify"] = "center"
        BotonEnviados["text"] = "Enviados"
        BotonEnviados.place(x=0,y=380,width=260,height=50)
        BotonEnviados["command"] = self.BotonEnviados_command


        image = Image.open("./imagenes/panel6.png")  
        image = image.resize((260, 50))  
        photo = ImageTk.PhotoImage(image)
        BotonEliminados=tk.Button(self,image=photo)
        BotonEliminados.image = photo 
        BotonEliminados["relief"] = "flat"
        BotonEliminados["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        BotonEliminados["font"] = ft
        BotonEliminados["fg"] = "#000000"
        BotonEliminados["justify"] = "center"
        BotonEliminados["text"] = "Eliminados"
        BotonEliminados.place(x=0,y=430,width=260,height=50)
        BotonEliminados["command"] = self.BotonEliminados_command


        LabelBienvenido=tk.Label(self)
        LabelBienvenido["bg"] = "#432959"
        ft = tkFont.Font(family='Times',size=15)
        LabelBienvenido["font"] = ft
        LabelBienvenido["fg"] = "#ffffff"
        LabelBienvenido["justify"] = "center"
        LabelBienvenido["text"] = "Bienvenido "
        LabelBienvenido.place(x=1070,y=30,width=200,height=35)

        

    def insertar_fila(self, remitente, correo, fecha):
        # Insertar una nueva fila en la tabla
        self.tabla.insert("", "end", values=(remitente, correo, fecha))


    def BotonAddContact_command(self):
        print("command")


    def BotonAddGroup_command(self):
        print("command")


    def BotonEnviar_command(self):
        print("command")


    def BotonContactos_command(self):
        print("command")


    def BotonGrupos_command(self):
        print("command")


    def BotonRecibidos_command(self):
        print("command")


    def BotonEnviados_command(self):
        print("command")


    def BotonEliminados_command(self):
        print("command")
    

        


   

