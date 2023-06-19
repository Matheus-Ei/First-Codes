#Imports
from tkinter import *


#Inicio
Fatorial = Tk()
Fatorial.geometry('200x200')


#Codigo

#Caixas de pergunta
Caixa_de_Pergunta_1 = Entry(Fatorial)
Caixa_de_Pergunta_1.place(x=1, y=30)

#Função
def FATORIAL():
    CAIXA_DE_PERGUNTA_1 = int(Caixa_de_Pergunta_1.get())

    Resultado_1 = (CAIXA_DE_PERGUNTA_1)-1
    Resultado = Resultado_1*CAIXA_DE_PERGUNTA_1

    if (CAIXA_DE_PERGUNTA_1 != 1):
        while (Resultado_1 != 1):
            Resultado_1 = (Resultado_1)-1
            Resultado = Resultado_1*Resultado
    elif (CAIXA_DE_PERGUNTA_1 <= 1):
        Resultado=1


    Texto_mostrado = Label(Fatorial, text='O resultado é de {}'.format(Resultado))
    Texto_mostrado.place(x=10, y=150)

#Botão
Botão_da_função_fatorial = Button(Fatorial, text="Calcular", command=lambda:FATORIAL())
Botão_da_função_fatorial.place(x=110, y=30)


#Fim
Fatorial.mainloop()