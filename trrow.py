import random
dl=10


tab=[(random.randint(-1000,1000), random.randint(-1000,1000))for _ in range (0,100)]


        


def polet(p, trtab):
    if p in trtab:
        return False
    
    P=0.5*abs((trtab[1][0]-trtab[0][0])*(trtab[2][1]-trtab[0][1])-(trtab[1][1]-trtab[0][1])*(trtab[2][0]-trtab[0][0]))
    P1=0.5*abs((p[0]-trtab[0][0])*(trtab[1][1]-trtab[0][1])-(p[1]-trtab[0][1])*(trtab[1][0]-trtab[0][0]))
    P2=0.5*abs((p[0]-trtab[1][0])*(trtab[2][1]-trtab[1][1])-(p[1]-trtab[1][1])*(trtab[2][0]-trtab[1][0]))
    P3=0.5*abs((p[0]-trtab[0][0])*(trtab[2][1]-trtab[0][1])-(p[1]-trtab[0][1])*(trtab[2][0]-trtab[0][0]))
    if P==P1+P2+P3:
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

                        
print((wyn))
                        
            
                    
                
            
        


