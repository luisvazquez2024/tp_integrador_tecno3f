import tkinter as tk
from tkinter import ttk

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=480,height=320)
        self.root = root
        self.pack()

    def label_form(self):
        pass
    
    def input_form(self):
        pass

    def guardar_campos(self):
        pass

    def mostrar_tabla(self):
        pass

    def editar_registro(self):
       pass
    
    def eliminar_registro(self):
        pass