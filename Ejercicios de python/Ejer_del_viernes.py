from tkinter import *
from tkinter import messagebox as box

class aplicacion:
    def __init__(self):
        self.ven = Tk()
        self.ven.title("Ejercicio Practico")
        self.ven.geometry("400x400+250+250")
        self.varCB = IntVar()
        
        # Checkbutton para aceptar términos y condiciones
        self.menCB = Checkbutton(self.ven, text="¿Está de acuerdo con los términos y condiciones?", 
                                 variable=self.varCB, width=35, command=self.verificar)
        self.menCB.place(x=100, y=20)
        
        # Botón "Acepto", inicialmente deshabilitado
        self.btnacept = Button(self.ven, text="Acepto", command=self.aceptar, 
                               bg="blue", fg="white", width=14, height=2, state="disabled")
        self.btnacept.place(x=100, y=60)
        
        self.ven.mainloop()

    def verificar(self):
        # Habilitar o deshabilitar el botón según el estado del Checkbutton
        if self.varCB.get() == 1:
            self.btnacept.config(state="normal")
        else:
            self.btnacept.config(state="disabled")

    def aceptar(self):
        # Mostrar un mensaje de confirmación al aceptar
        box.showinfo("Éxito", "Ha aceptado los términos y condiciones.")

app = aplicacion()