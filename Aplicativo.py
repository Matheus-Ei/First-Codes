#Start
from tkinter import *

#Color
color={'black':'#32373e', 'blac':'#006400','white':'#d3d3d3' }

#Window1
window1=Tk()
window1.title('Aplicativo do Matheus')
window1.config(bg=color['black'])




#Calculadora_funcion
def Funcion(F):
    window2=Tk()
    window2.title('Calculadora')
    window2.geometry('250x150')
    window2.config(bg=color['black'])
    def funcio(y):
        n1=float(e.get())
        n2=float(e1.get())
        n3=e2.get()
        if n3=='+':
            Resultado=n1+n2
        if n3=='-':
            Resultado=n1-n2
        if n3=='*':
            Resultado=n1*n2
        if n3=='/':
            Resultado=n1/n2
        t1=Label(window2, width=30, text='O resultado é de %s'%(Resultado),font='italian, 10')
        t1.place(x=10,y=10)
        t1.config(bg=color['black'])
    e2=Entry(window2,width=1)
    e2.place(x=75,y=90)
    e2.config(bg=color['blac'])
    e1=Entry(window2, width=5)
    e1.place(x=115, y=90)
    e1.config(bg=color['blac'])
    e=Entry(window2, width=5)
    e.place(x=10, y=90)
    e.config(bg=color['blac'])
    t1=Label(window2, width=30, text='Coloque os valores nos campos abaixo',font='italian, 10')
    t1.place(x=10,y=10)
    t1.config(bg=color['black'])
    b1=Button(window2, width=10, text='Calcular',command=lambda:funcio('y'))
    b1.place(x=30,y=50)
    b1.config(bg=color['blac'])
    window2.mainloop()

#Avestack funcion
def Funcion1(F1):
#Window
    menu_window=Tk()
    menu_window.geometry('400x250')
    menu_window.title('Avestack 2.0')
    menu_window.config(bg=color['black'])

#Menu_Funcion

#Converçao_alimentar_menu
    def converção_alimentar_funcion(Converção_alimentar):
        converção=Tk()
        converção.geometry('400x200')
        converção.title('Avestack 2.0')
        converção.config(bg=color['black'])
        menu_text_1=Label(converção, width='20', text='converção alimentar', font='Arial 20 bold')
        menu_text_1.place(x=60,y=5)
        menu_text_1.config(bg=color['black'],fg=color['white'])
        def converção_button1(cb):
            n1=int(c1.get())
            n2=int(c2.get())
            n3=int(c3.get())
            n4=int(c4.get())
            Ps=n1-n2
            Ps1=n3/Ps
            Convercao=Ps1/n4
            L=Label(converção, width='40', text='A converção alimentar dos frangos é %s'%(Convercao))
            L.place(x=1,y=40)
            L.config(bg=color['black'])
        converção_button=Button(converção, width='10', text='Calcular', command=lambda:converção_button1('cb'))
        converção_button.place(x=5,y=10)
        converção_button.config(bg=color['blac'])
        c1=Entry(converção, width=10)
        c1.place(x=40, y=150)
        c1.config(bg=color['blac'])
        c2=Entry(converção, width=10)
        c2.place(x=260, y=150)
        c2.config(bg=color['blac'])
        c3=Entry(converção, width=10)
        c3.place(x=40, y=90)
        c3.config(bg=color['blac'])
        c4=Entry(converção, width=10)
        c4.place(x=260, y=90)
        c4.config(bg=color['blac'])
        L1=Label(converção, width='30', text='Diga o numero de ave alojadas',font='arial 8')
        L1.place(x=15, y=130)
        L1.config(bg=color['black'])
        L2=Label(converção, width='30', text='Diga o numero de aves mortas',font='arial 8')
        L2.place(x=190, y=130)
        L2.config(bg=color['black'])
        L3=Label(converção, width='30', text='Diga quanta ração foi consumida(Kg)',font='arial 8')
        L3.place(x=15, y=70)
        L3.config(bg=color['black'])
        L4=Label(converção, width='25', text='Diga o peso medio(Kg)',font='arial 8')
        L4.place(x=210, y=70)
        L4.config(bg=color['black'])
        converção.mainloop()

#Peso_medio_menu
    def Peso_medio_funcion(Peso_medio):
        converção=Tk()
        converção.config(bg=color['black'])
        converção.geometry('290x300')
        converção.title('Avestack 2.0')
        def Peso_button(peso):
            n1=float(e1.get())
            n2=float(e2.get())
            n3=float(e3.get())
            n4=float(e4.get())
            n5=float(e5.get())
            n6=float(e6.get())
            n7=float(e7.get())
            n8=float(e8.get())
            nm1=(n1+n2+n3+n4)/4
            nm2=(n5+n6+n7+n8)/4
            res1=(nm1+nm2)/2
            l=Label(converção, width='25',text='O peso medio foi de %s'%(res1), font='arial 10 bold')
            l.place(x=95,y=25)
            l.config(bg=color['black'],fg=color['white'])
        converção_button=Button(converção, width='10', text='Calcular', command=lambda:Peso_button('peso'))
        converção_button.place(x=5,y=10)
        converção_button.config(bg=color['blac'])
        l=Label(converção, width='20', text='Preencha cada peso:', font='arial 13 bold')
        l.place(x=85,y=20)
        l.config(bg=color['black'],fg=color['white'])
        e1=Entry(converção, width='20')
        e1.place(x=10,y=100)
        e1.config(bg=color['blac'])
        e2=Entry(converção, width='20')
        e2.place(x=150,y=100)
        e2.config(bg=color['blac'])
        e3=Entry(converção, width='20')
        e3.place(x=10,y=150)
        e3.config(bg=color['blac'])
        e4=Entry(converção, width='20')
        e4.place(x=150,y=150)
        e4.config(bg=color['blac'])
        e5=Entry(converção, width='20')
        e5.place(x=10,y=200)
        e5.config(bg=color['blac'])
        e6=Entry(converção, width='20')
        e6.place(x=150,y=200)
        e6.config(bg=color['blac'])
        e7=Entry(converção, width='20')
        e7.place(x=10,y=250)
        e7.config(bg=color['blac'])
        e8=Entry(converção, width='20')
        e8.place(x=150,y=250)
        e8.config(bg=color['blac'])
        converção.mainloop()


#IEP_menu
    def IEP_funcion(IEP):
        converção=Tk()
        converção.config(bg=color['black'])
        converção.geometry('400x600')
        converção.title('Avestack 2.0')
        converção.mainloop()


    #Consumo_de_raçao_menu
    def Consumo_de_raçao_funcion(Consumo_de_raçao):
        converção=Tk()
        converção.config(bg=color['black'])
        converção.geometry('400x600')
        converção.title('Avestack 2.0')
        converção.mainloop()


#Metas_de_CA_menu
    def Metas_de_CA_funcion(Metas_de_CA):
        converção=Tk()
        converção.config(bg=color['black'])
        converção.geometry('400x600')
        converção.title('Avestack 2.0')
        converção.mainloop()


#Metas_de_peso_menu
    def Metas_de_peso_funcion(Metas_de_peso):
        converção=Tk()
        converção.config(bg=color['black'])
        converção.geometry('290x480')
        converção.title('Avestack')
        List_raças=["Macho","Femea","Misto"]
        w=StringVar()
        w.set(List_raças[0])
        op_raças=OptionMenu(converção,w,*List_raças)
        op_raças.place(x=190,y=10)
        op_raças.config(bg=color['white'])
        def Listas(listas):
            W1=w.get()
            if W1=='Macho':
                l1=Label(converção, width=20, text='Dia 1: 53 g', font='arial 10')
                l1.place(x=50,y=120)
                l1.config(bg=color['blac'])
                l2=Label(converção, width=20, text='Dia 7: 179 g', font='arial 10')
                l2.place(x=50,y=160)
                l2.config(bg=color['blac'])
                l3=Label(converção, width=20, text='Dia 14: 475 g', font='arial 10')
                l3.place(x=50,y=200)
                l3.config(bg=color['blac'])
                l4=Label(converção, width=20, text='Dia 21: 938 g', font='arial 10')
                l4.place(x=50,y=240)
                l4.config(bg=color['blac'])
                l5=Label(converção, width=20, text='Dia 28: 1531 g', font='arial 10')
                l5.place(x=50,y=280)
                l5.config(bg=color['blac'])
                l6=Label(converção, width=20, text='Dia 35: 2217 g', font='arial 10')
                l6.place(x=50,y=320)
                l6.config(bg=color['blac'])
                l7=Label(converção, width=20, text='Dia 42: 2953 g', font='arial 10')
                l7.place(x=50,y=360)
                l7.config(bg=color['blac'])
                l8=Label(converção, width=20, text='Dia 49: 3660 g', font='arial 10')
                l8.place(x=50,y=400)
                l8.config(bg=color['blac'])
            if W1=='Femea':
                l1=Label(converção, width=20, text='Dia 1: 51 g', font='arial 10')
                l1.place(x=50,y=120)
                l1.config(bg=color['blac'])
                l2=Label(converção, width=20, text='Dia 7: 175 g', font='arial 10')
                l2.place(x=50,y=160)
                l2.config(bg=color['blac'])
                l3=Label(converção, width=20, text='Dia 14: 473 g', font='arial 10')
                l3.place(x=50,y=200)
                l3.config(bg=color['blac'])
                l4=Label(converção, width=20, text='Dia 21: 844 g', font='arial 10')
                l4.place(x=50,y=240)
                l4.config(bg=color['blac'])
                l5=Label(converção, width=20, text='Dia 28: 1341 g', font='arial 10')
                l5.place(x=50,y=280)
                l5.config(bg=color['blac'])
                l6=Label(converção, width=20, text='Dia 35: 1914 g', font='arial 10')
                l6.place(x=50,y=320)
                l6.config(bg=color['blac'])
                l7=Label(converção, width=20, text='Dia 42: 2511 g', font='arial 10')
                l7.place(x=50,y=360)
                l7.config(bg=color['blac'])
                l8=Label(converção, width=20, text='Dia 49: 3084 g', font='arial 10')
                l8.place(x=50,y=400)
                l8.config(bg=color['blac'])
            if W1=='Misto':
                l1=Label(converção, width=20, text='Dia 1: 52 g', font='arial 10')
                l1.place(x=50,y=120)
                l1.config(bg=color['blac'])
                l2=Label(converção, width=20, text='Dia 7: 177 g', font='arial 10')
                l2.place(x=50,y=160)
                l2.config(bg=color['blac'])
                l3=Label(converção, width=20, text='Dia 14: 459 g', font='arial 10')
                l3.place(x=50,y=200)
                l3.config(bg=color['blac'])
                l4=Label(converção, width=20, text='Dia 21: 891 g', font='arial 10')
                l4.place(x=50,y=240)
                l4.config(bg=color['blac'])
                l5=Label(converção, width=20, text='Dia 28: 1436 g', font='arial 10')
                l5.place(x=50,y=280)
                l5.config(bg=color['blac'])
                l6=Label(converção, width=20, text='Dia 35: 2067 g', font='arial 10')
                l6.place(x=50,y=320)
                l6.config(bg=color['blac'])
                l7=Label(converção, width=20, text='Dia 42: 2732 g', font='arial 10')
                l7.place(x=50,y=360)
                l7.config(bg=color['blac'])
                l8=Label(converção, width=20, text='Dia 49: 3369 g', font='arial 10')
                l8.place(x=50,y=400)
                l8.config(bg=color['blac'])
        Metas_de_peso=Button(converção, width='20', text='Metas de peso',font='Arial 10', command=lambda:Listas('listas'))
        Metas_de_peso.place(x=5,y=10)
        Metas_de_peso.config(bg=color['blac'])
        converção.mainloop()



#Menu_Button
    converção_alimentar=Button(menu_window, width='20',text='Converção alimentar',font='Arial 10', command=lambda:converção_alimentar_funcion('Converção_alimentar'))
    converção_alimentar.place(x=15,y=70)
    converção_alimentar.config(bg=color['blac'])

    Peso_medio=Button(menu_window, width='20', text='Peso medio',font='Arial 10', command=lambda:Peso_medio_funcion('Peso_medio'))
    Peso_medio.place(x=195,y=70)
    Peso_medio.config(bg=color['blac'])

    IEP=Button(menu_window, width='20', text='IEP',font='Arial 10', command=lambda:IEP_funcion('IEP'))
    IEP.place(x=15,y=130)
    IEP.config(bg=color['blac'])

    Consumo_de_raçao=Button(menu_window, width='20', text='Consumo de ração',font='Arial 10', command=lambda:Consumo_de_raçao_funcion('Consumo_de_raçao'))
    Consumo_de_raçao.place(x=195,y=130)
    Consumo_de_raçao.config(bg=color['blac'])

    Metas_de_CA=Button(menu_window, width='20', text='Metas de CA',font='Arial 10', command=lambda:Metas_de_CA_funcion('Metas_de_CA'))
    Metas_de_CA.place(x=15,y=190)
    Metas_de_CA.config(bg=color['blac'])

    Metas_de_peso=Button(menu_window, width='20', text='Metas de peso',font='Arial 10', command=lambda:Metas_de_peso_funcion('Metas_de_peso'))
    Metas_de_peso.place(x=195,y=190)
    Metas_de_peso.config(bg=color['blac'])



#Menu_Text
    menu_text_1=Label(menu_window, width='20', text='Menu', font='Arial 30 bold')
    menu_text_1.place(x=-55,y=20)
    menu_text_1.config(bg=color['black'], fg=color['white'])

#End
    menu_window.mainloop()





#Agenda_funcion
def menu10(agenda):
    menu=Tk()
    menu.config(bg=color['black'])
    menu.geometry('205x220')
    menu.title('Agenda menu')
    t4=Label(menu, width=10, text='Agenda',font='arial 20 bold')
    t4.place(x=10,y=1)
    t4.config(bg=color['black'], fg=color['white'])


    def segunda(seg):
        menu1=Tk()
        menu1.config(bg=color['black'])
        menu1.geometry('500x200')
        menu1.title('Agenda menu')
        def x1(X1):
            x=X.get()
            t4=Label(menu1, width=50, text='%s'%(x),font='arial 10')
            t4.config(bg=color['black'], fg=color['white'])
            t4.place(x=1,y=80)
        t4=Label(menu1, width=10, text='Segunda',font='arial 15 bold')
        t4.place(x=200,y=1)
        t4.config(bg=color['black'], fg=color['white'])
        b1=Button(menu1,width=20 ,text='Anotar',command=lambda:x1('X1'))
        b1.place(x=10, y=5)
        b1.config(bg=color['blac'])
        X=Entry(menu1, width=20)
        X.place(x=10, y=40)
        X.config(bg=color['blac'])
        menu1.mainloop()
    def terça(ter):
        menu1=Tk()
        menu1.config(bg=color['black'])
        menu1.geometry('500x100')
        menu1.title('Agenda menu')
        def x1(X1):
            x=X.get()
            t4=Label(menu1, width=80, text='%s'%(x),font='arial 10')
            t4.config(bg=color['black'], fg=color['white'])
            t4.place(x=1,y=80)
        t4=Label(menu1, width=10, text='Terça',font='arial 15 bold')
        t4.place(x=200,y=1)
        t4.config(bg=color['black'], fg=color['white'])
        b1=Button(menu1,width=20 ,text='Anotar',command=lambda:x1('X1'))
        b1.place(x=10, y=5)
        b1.config(bg=color['blac'])
        X=Entry(menu1, width=20)
        X.place(x=10, y=40)
        X.config(bg=color['blac'])
        menu1.mainloop()
    def quarta(qua):
        menu1=Tk()
        menu1.config(bg=color['black'])
        menu1.geometry('500x100')
        menu1.title('Agenda menu')
        def x1(X1):
            x=X.get()
            t4=Label(menu1, width=80, text='%s'%(x),font='arial 10')
            t4.config(bg=color['black'], fg=color['white'])
            t4.place(x=1,y=80)
        t4=Label(menu1, width=10, text='Quarta',font='arial 15 bold')
        t4.place(x=200,y=1)
        t4.config(bg=color['black'], fg=color['white'])
        b1=Button(menu1,width=20 ,text='Anotar',command=lambda:x1('X1'))
        b1.place(x=10, y=5)
        b1.config(bg=color['blac'])
        X=Entry(menu1, width=20)
        X.place(x=10, y=40)
        X.config(bg=color['blac'])
        menu1.mainloop()
    def quinta(qui):
        menu1=Tk()
        menu1.config(bg=color['black'])
        menu1.geometry('500x100')
        menu1.title('Agenda menu')
        def x1(X1):
            x=X.get()
            t4=Label(menu1, width=80, text='%s'%(x),font='arial 10')
            t4.config(bg=color['black'], fg=color['white'])
            t4.place(x=1,y=80)
        t4=Label(menu1, width=10, text='Quinta',font='arial 15 bold')
        t4.place(x=200,y=1)
        t4.config(bg=color['black'], fg=color['white'])
        b1=Button(menu1,width=20 ,text='Anotar',command=lambda:x1('X1'))
        b1.place(x=10, y=5)
        b1.config(bg=color['blac'])
        X=Entry(menu1, width=20)
        X.place(x=10, y=40)
        X.config(bg=color['blac'])
        menu1.mainloop()
    def sexta(sex):
        menu1=Tk()
        menu1.config(bg=color['black'])
        menu1.geometry('500x100')
        menu1.title('Agenda menu')
        def x1(X1):
            x=X.get()
            t4=Label(menu1, width=80, text='%s'%(x),font='arial 10')
            t4.config(bg=color['black'], fg=color['white'])
            t4.place(x=1,y=80)
        t4=Label(menu1, width=10, text='Sexta',font='arial 15 bold')
        t4.place(x=200,y=1)
        t4.config(bg=color['black'], fg=color['white'])
        b1=Button(menu1,width=20 ,text='Anotar',command=lambda:x1('X1'))
        b1.place(x=10, y=5)
        b1.config(bg=color['blac'])
        X=Entry(menu1, width=20)
        X.place(x=10, y=40)
        X.config(bg=color['blac'])
        menu1.mainloop()
    def sabado(sab):
        menu1=Tk()
        menu1.config(bg=color['black'])
        menu1.geometry('500x100')
        menu1.title('Agenda menu')
        def x1(X1):
            x=X.get()
            t4=Label(menu1, width=80, text='%s'%(x),font='arial 10')
            t4.config(bg=color['black'], fg=color['white'])
            t4.place(x=1,y=80)
        t4=Label(menu1, width=10, text='Sabado',font='arial 15 bold')
        t4.place(x=200,y=1)
        t4.config(bg=color['black'], fg=color['white'])
        b1=Button(menu1,width=20 ,text='Anotar',command=lambda:x1('X1'))
        b1.place(x=10, y=5)
        b1.config(bg=color['blac'])
        X=Entry(menu1, width=20)
        X.place(x=10, y=40)
        X.config(bg=color['blac'])
        menu1.mainloop()


    b3=Button(menu, width=10, text='Segunda',command=lambda:segunda('seg'))
    b3.place(x=20,y=100)
    b3.config(bg=color['blac'])
    b2=Button(menu, width=10, text='Terça',command=lambda:terça('ter'))
    b2.place(x=110,y=100)
    b2.config(bg=color['blac'])
    b1=Button(menu, width=10, text='Quarta',command=lambda:quarta('qua'))
    b1.place(x=20,y=140)
    b1.config(bg=color['blac'])
    b4=Button(menu, width=10, text='Quinta',command=lambda:quinta('qui'))
    b4.place(x=110,y=140)
    b4.config(bg=color['blac'])
    b5=Button(menu, width=10, text='Sexta',command=lambda:sexta('sex'))
    b5.place(x=20,y=180)
    b5.config(bg=color['blac'])
    b6=Button(menu, width=10, text='Sabado',command=lambda:sabado('sab'))
    b6.place(x=110,y=180)
    b6.config(bg=color['blac'])
    menu.mainloop()





#Button
b1=Button(window1, width=10, text='Calculadora',command=lambda:Funcion('F'))
b1.place(x=30,y=50)
b1.config(bg=color['blac'])
b2=Button(window1, width=10, text='Avestack 2.0',command=lambda:Funcion1('F1'))
b2.place(x=30,y=80)
b2.config(bg=color['blac'])
b3=Button(window1, width=10, text='Agenda',command=lambda:menu10('agenda'))
b3.place(x=30,y=110)
b3.config(bg=color['blac'])

#Text
t1=Label(window1, width=10, text='Menu do App',font='arial 20 bold')
t1.place(x=10,y=1)
t1.config(bg=color['black'], fg=color['white'])

#End
window1.mainloop()