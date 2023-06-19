from tkinter import *

#Window
window=Tk()
window.geometry('2100x900')
window.title("Calcular a area²")

#funcion
def click1(msg1):
    n1=int(e.get())
    n2=int(e1.get())
    resultado=n1*n2

    t["text"]="O resultado é da area²:"
    t["text"]=t["text"]+str(resultado)

#Text_Box
e1=Entry(window, width=20)
e1.place(x=400, y=200)
e=Entry(window, width=20)
e.place(x=800, y=200)

#Text
t=Label(window, width=50, text="O resultado é da area²:", font='Italian, 20')
t.place(x=250,y=450)

ms=1

#Button
b=Button(window, width=20, text='Calcular', font='Italian, 20', command=lambda: click1('msg1'))
b.place(x=470,y=550)

#End
window.mainloop()