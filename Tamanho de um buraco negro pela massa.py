c=299792458
m=1
g=6.674184*0.00000000001

def ma(r):
    print("O raio do buraco negro com esta massa é de %s"%(r))

C=(c * c)
m=(float(input("Diga alguma massa para um buraco negro-")))
G=(2*g*m)
R=G/C
r=R/1000

ma(r)