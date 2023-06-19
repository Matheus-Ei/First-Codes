k=1
x=1
k=float(input("Diga algum valor para o coeficiente elastico do material-"))
x=float(input("Diga algum deslocamento da mola-"))
def elastico(e):
    print("O valor do coeficiente elastico é de %s newtons"%(e))
    
e=k * x

elastico(e)