m=1
v=1
r=1
def ma(c):
    print("o valor da força centripeta é de %s Newtons"%(c))

m=float(input("Diga alguma massa-"))
v=float(input("Diga alguma velocidade-"))
r=float(input("Diga algum raio-"))

n=(v * v)
d=(m * n)
c=d/r

ma(c)