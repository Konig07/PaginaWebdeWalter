from tkinter import *

class aplicacion:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Ejercicio Practico")
        self.ventana.geometry("400x400+250+250")
        self.ventana.config(bg="lightblue")
        self.varEn= StringVar()
        self.txt1 = Entry(self.ventana, textvariable=self.varEn, width=20)
        self.txt1.place(x=100, y=50)
        self.varb=IntVar()
        self.rb1 = Radiobutton(self.ventana, text="Vocales", variable=self.varb, value=1, bg="lightblue")
        self.rb1.place(x=100, y=100)
        self.rb2 = Radiobutton(self.ventana, text="Consonantes", variable=self.varb, value=2, bg="lightblue")
        self.rb2.place(x=100, y=130)
        self.lbl1 = Label(self.ventana,font=("Blackkader ITC", 10),bg="purple", fg="white", width=25, height=4)
        self.lbl1.place(x=100, y=160)
        self.btn1 = Button(self.ventana, text="Vocales/Consonantes", command=self.mostrar, bg="blue", fg="white", width=20,height=2)
        self.btn1.place(x=100, y=230)
        self.ventana.mainloop()
    def mostrar(self):
        vocales = "aeiou"
        cadena = self.varEn.get()
        resultado = " "
        if self.varb.get() == 1:
            for letra in cadena:
                if letra.lower() in vocales:
                    resultado += letra + " "
            self.lbl1.config(text="Vocales: " + resultado)
        elif self.varb.get() == 2:
            for letra in cadena:
                if letra.lower() not in vocales:
                    resultado += letra + " "
            self.lbl1.config(text="Consonantes: " + resultado)
app = aplicacion()