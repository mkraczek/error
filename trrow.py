import random


dl=1000000000000000000000000


class Wsp:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def wart(self):
        return (self.x, self.y)

class Wsp1(Wsp):
    def __init__(self, x, y):
        super().__init__(x, y)

tab=[]
for i in range (dl):
    chuj=Wsp1(random.randint(-10,10),random.randint(-10,10))
    tab.append(chuj.wart())


        


def polet(p, trtab):
    if p in trapeztab:
        return False
    P1=0.5*abs((trapeztab[1][0]-trapeztab[0][0])*(p[1]-trapeztab[0][1])-(trapeztab[1][1]-trapeztab[0][1])*(p[0]-trapeztab[0][0]))
    P2=0.5*abs((trapeztab[2][0]-trapeztab[1][0])*(p[1]-trapeztab[1][1])-(trapeztab[2][1]-trapeztab[1][1])*(p[0]-trapeztab[1][0]))
    P3=0.5*abs((trapeztab[3][0]-trapeztab[2][0])*(p[1]-trapeztab[2][1])-(trapeztab[3][1]-trapeztab[2][1])*(p[0]-trapeztab[2][0]))
    P4=0.5*abs((trapeztab[3][0]-trapeztab[0][0])*(p[1]-trapeztab[0][1])-(trapeztab[3][1]-trapeztab[0][1])*(p[0]-trapeztab[0][0]))
    P=0.5*abs((abs(trapeztab[1][0]-trapeztab[0][0])+abs(trapeztab[2][0]-trapeztab[3][0]))*abs(trapeztab[3][1]-trapeztab[0][1]))
    if P==P1+P2+P3+P4:
        return False
    else:
        return True


def rowne(trtab):

    x=((trtab[1][0]-trtab[0][0])**2+(trtab[1][1]-trtab[0][1])**2)
    y=((trtab[2][0]-trtab[1][0])**2+(trtab[2][1]-trtab[1][1])**2)
    z=((trtab[2][0]-trtab[0][0])**2+(trtab[2][1]-trtab[0][1])**2)

    if x==y==z:
        print(x,y,z)
        return True
    else:
        return False

wyn=[]

for i in range (0,dl-2):
    a=tab[i]
    for j in range (i+1,dl-1):
        b=tab[j]
        if a!=b:
            for k in range (j+2,dl-0):
                c=tab[k]
                if a!=c and c!=b:   

                    trtab=[a,b,c]

                    if rowne(trtab):
                        for p in tab:
                            if polet(p,trtab):
                                if trtab not in wyn:
                                    wyn.append(trtab)
                                    break

                                   
def eeee(dl):
    if 123=a:
        return true
                        
print((wyn))
                        
            
                    
                
            
        


