from tkinter import messagebox
import tkinter as tk
import csv

class FormRegister:

    @staticmethod
    def guardar_Archivo(Registros, usuario, password):
        with open(Registros, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            writer.writerow([usuario+"@helios.com", password])

    @staticmethod
    def verificar(Registros, usuario, password):
        existe = False
        with open(Registros, 'r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for linea in reader:
                if linea and linea[0] == usuario:
                    existe = True
                    break
        return existe
    
    def __init__(self, usuario, password):
        archivo = './Registros/Registros.csv'
        existe = FormRegister.verificar(archivo, usuario, password)
        if not existe:
            FormRegister.guardar_Archivo(archivo, usuario, password)
        else:
            messagebox.showerror(message="El usuario ya existe", title="Mensaje")
