from tkinter import *

class Aplicacion:
    def __init__(self):
        self.ven=Tk()
        self.ven.title("Ejercicio de examen")
        self.ven.geometry("400x400+250+250")
        self.varEn=StringVar()
        self.varrb=IntVar()
        self.txt1=Entry(self.ven, textvariable=self.varEn, width=30)
        self.txt1.place(x=100, y=20)
        self.rb1=Radiobutton(self.ven, text="Cambiar vocales a 0", variable=self.varrb, value=1, command=self.vx0)
        self.rb1.place(x=100, y=60)
        self.rb2=Radiobutton(self.ven, text="Cambiar consonantes a #", variable=self.varrb, value=2, command=self.consonante)
        self.rb2.place(x=100, y=100)
        self.rb3=Radiobutton(self.ven, text="Volver a la cadena original", variable=self.varrb, value=3, command=self.origin)
        self.rb3.place(x=100, y=140)
        self.ven.mainloop()
    def vx0(self):
        vocales = "aeiouAEIOU"
        cade = self.varEn.get()
        resultado = ""
        if self.varrb.get() == 1:
            for letra in cade:
                if letra in vocales:
                    resultado += "0"
                else:
                    resultado += letra
                self.varEn.set(resultado)

    def consonante(self):
        vocales = "aeiouAEIOU"
        cade = self.varEn.get()
        resultado = ""
        if self.varrb.get() == 2:
            for letra in cade:
                if letra not in vocales and 'a' <= letra.lower() <= 'z':
                    resultado += "#"
                else:
                    resultado += letra
                self.varEn.set(resultado)
    def origin(self):
        if self.varrb.get() == 3:
            self.varEn.set(" ")  # Reset the text to its original state
app=Aplicacion()