from tkinter import *
from tkinter import messagebox as box
class aplicacion:
    def __init__(self):
        self.ven = Tk()
        self.ven.title("Ejercicio Practico")
        self.ven.geometry("400x400+250+250")
        self.ven.config(bg="purple")
        self.varEn= StringVar()
        self.txt1 = Entry(self.ven, textvariable=self.varEn, width=20)
        self.txt1.place(x=100, y=20)
        self.lblnom = Label(self.ven, text="Nombre", bg="purple", fg="white")
        self.lblnom.place(x=100, y=50)
        self.lblnom2=Label(self.ven, bg="yellow", fg="purple",width=20)
        self.lblnom2.place(x=100, y=80)
        self.lblape = Label(self.ven, text="Apellido", bg="purple", fg="white")
        self.lblape.place(x=100, y=110)
        self.lblape2=Label(self.ven, bg="yellow", fg="purple",width=20)
        self.lblape2.place(x=100, y=130)
        self.btnmos=Button(self.ven, text="Mostrar", command=self.mostrar, bg="blue", fg="white", width=20,height=2)
        self.btnmos.place(x=100, y=160)
        self.btnlimp=Button(self.ven, text="Limpiar", command=self.limpiar, bg="blue", fg="white", width=20,height=2)
        self.btnlimp.place(x=100, y=210)
        self.btnsal=Button(self.ven, text="Salir", command=self.salir, bg="blue", fg="white", width=20,height=2)
        self.btnsal.place(x=100, y=260)
        self.ven.mainloop()
    def mostrar(self):
        txt = self.varEn.get()
        es = txt.find(" ")
        if es != -1:
            nom = txt[:es]
            ape = txt[es + 1:]
        else:
            nom = txt
            ape = ""
        self.lblnom2.config(text="Nombre: " + nom)
        self.lblape2.config(text="Apellido: " + ape)
    def limpiar(self):
        self.varEn.set("")
        self.lblnom2.config(text="")
        self.lblape2.config(text="")
    def salir(self):
        op=box.askokcancel("Salir", "Realmente desea salir?")
        if op==True:
            self.ven.destroy()

app = aplicacion()