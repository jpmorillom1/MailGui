import tkinter as tk
from tkinter import ttk
import util.generic as utl
from forms.form import FormRegister as fom
from tkinter import messagebox


class FormRegisterDesigner:

    def __init__(self):
        
        self.ventana = tk.Toplevel()
        self.ventana.title('Registro de usuario') 
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 600, 450)

        logo = utl.leer_imagen("./imagenes/logo2.png", (150, 150))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200,
                              relief=tk.SOLID, padx=10, pady=10, bg='#16fb71')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#16fb71')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuario", font=(
            'Times', 30), fg="#432959", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=(
            'Times', 14), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=10, pady=5)
        contenedor_usuario = tk.Frame(frame_form_fill, bg='#fcfcfc')
        contenedor_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(contenedor_usuario, font=('Times', 14))
        self.usuario.pack(side=tk.LEFT, padx=10, pady=10)

        dominio = tk.Label(contenedor_usuario, text="@helios.com", font=(
            'Times', 14))
        dominio.pack(side=tk.RIGHT, padx=20, pady=5)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=(
            'Times', 14), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")
        
        etiqueta_confirmation = tk.Label(frame_form_fill, text="Confirmacion", font=(
            'Times', 14), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_confirmation.pack(fill=tk.X, padx=20, pady=5)
        self.confirmation = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.confirmation.pack(fill=tk.X, padx=20, pady=10)
        self.confirmation.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Registrar", font=(
            'Times', 15), bg='#432959', bd=0, fg="#fff", command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        
        # end frame_form_fill
        self.ventana.mainloop()

    def register(self):

        usuario = self.usuario.get()
        password = self.password.get()
        con = self.confirmation.get()
        if usuario == "" or password == "" or con == "":
            self.ventana.withdraw()
            messagebox.showerror(message="Ningun campo puede estar vacio", title="Mensaje")
            self.ventana.deiconify()
        else:
            if password == con:
                fom(usuario, password)
                self.ventana.destroy()

            else:
                self.ventana.withdraw()
                messagebox.showerror(message="las contraseñas no son iguales", title="Mensaje")
                self.ventana.deiconify()
