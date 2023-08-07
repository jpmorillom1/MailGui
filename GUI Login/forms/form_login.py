import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel
import forms.form_designer as regis
import csv
import util.generic as utl

class App:
    def userRegister(self):
        regis.FormRegisterDesigner()
    
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        with open('./Registros/Registros.csv', 'r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for linea in reader:
                if linea and linea[0] == usu and linea[1] == password:
                    self.ventana.destroy()
                    MasterPanel()
                    break
            else:
                messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")           
                      
    def __init__(self):       
        self.ventana = tk.Tk()
        
        logo =utl.leer_imagen("./imagenes/logo.png", (200, 200))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#432959')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='#432959' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#432959",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14) ,fg="#000000",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#000000",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Times', 15,BOLD),bg='#432959', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))

        inicio = tk.Button(frame_form_fill, text="Registrar usuario", font=(
            'Times', 15), bg='#fcfcfc', bd=0, fg="#432959", command=self.userRegister)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.userRegister()))

        self.ventana.withdraw() 
        self.Temporal() 
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,800,500)

        #end frame_form_fill
        self.ventana.mainloop()

    def Temporal(self):
        self.ventana.withdraw() 
        temporal = tk.Toplevel(self.ventana)
        temporal.geometry("900x600") 
        utl.centrar_ventana(temporal, 900, 600)
        temporal.config(bg="#432959")
        temporal.grab_set() 
        temporal.overrideredirect(True)

        logo =utl.leer_imagen("./imagenes/temp.png", (900, 600))
        label = tk.Label(temporal, image=logo, relief="flat")

        label.place(relx=0.5, rely=0.5, anchor="center")

        self.ventana.update()
        temporal.after(3000, label.destroy())
        temporal.destroy()
        self.ventana.deiconify()


if __name__ == "__main__":
   App()