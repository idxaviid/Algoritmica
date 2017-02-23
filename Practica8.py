##########################
#   Xavi Cano Granada    #
#   Practica 8 : Python  #           #NOTA:Les trucades a les funcions estan avall de tot.
##########################
import math
import time
import random
#------------------------------------------------------------------------------------------#
def func1d(x): 
    y = x * math.sin(10*math.pi*(x))+1.0 
    return y
#------------------------------------------------------------------------------------------#
def frange1d(start,end,inc):
    while start<end:
        if start<end:
            yield start		
        start=start+inc
#------------------------------------------------------------------------------------------#
def search1d(start,end,inc):
    t1=time.clock()
    maximo=0
    numAvalu=0
    for i in frange1d(start,end,inc):
        x=func1d(i)
        numAvalu=numAvalu+1
        if maximo<=x:
            maximo=x
            maxFunc=i
    t2=time.clock()
    print "--------------------------------------------------------------------\n"
    print "El valor maxim de la funcio esta al voltant del valor: "+str(maximo)
    print "I es dona per una x al voltant del valor: "+str(maxFunc)
    print "El nombre d'avaluacions de la funcio es: "+str(numAvalu)
    print "El temps que ha trigat en calcular, ha estat : %0.3f ms\n\n" % ((t2-t1))
#------------------------------------------------------------------------------------------#
def func2d(x,y):  
    resul=200-(x**2+y-11)**2-(x+y**2-7)**2 
    return resul
#------------------------------------------------------------------------------------------#
def frange2d(start,end,inc):
    while start<end:
        if start<end:
            yield start		
        start=start+inc
#------------------------------------------------------------------------------------------#
def search2d(start,end,inc):
    t1=time.clock()
    maximo=0
    vector=[]
    numAvalu=0
    cont=0
    longMatriu=0   
    for i in frange2d(start,end,inc):      
        for j in frange2d(start,end,inc):  
            longMatriu=longMatriu+1        
    matriz = [[0 for col in range(2)] for row in range(longMatriu)]
    for i in range(longMatriu):
        matriz[i][0] = 0.0	
    for i in frange2d(start,end,inc):
        for j in frange2d(start,end,inc):
            x=func2d(j,i)
            numAvalu=numAvalu+1
            if maximo<=math.ceil(x):
                maximo=x
                maxFunc="["+str(j)+","+str(i)+"]"
                matriz[cont][0]=maximo
                matriz[cont][1]=maxFunc
                cont=cont+1
                vector.append(maxFunc)
    matriz.sort()
    matriz.reverse()
    print "--------------------------------------------------------------------\n"
    print "Els 4 maxims de la funcio son:"
    for q in range(0,4):
        print matriz[q][1]
    t2=time.clock()
    print "El valor maxim de la funcio esta al voltant del valor: "+str(maximo)
    print "I es dona per una x al voltant del valor: "+str(maxFunc)
    print "El nombre d'avaluacions de la funcio es: "+str(numAvalu)
    print "El temps que ha trigat en calcular, ha estat : %0.3f ms\n\n\n" % ((t2-t1))
#------------------------------------------------------------------------------------------#    
def main1():
    search1d(-1.0,2.0,0.01)
    search1d(-1.0,2.0,0.0001)
    search1d(-1.0,2.0,0.000001)
#------------------------------------------------------------------------------------------#
def main2():
    #Valors de probes
    search2d(-6.0,6.0,0.01)                 #Aquetes valors son de proba per comprobar que l'algoritme funciona be
    search2d(-1.0,0.0,0.001)                #ja que amb els valors que demana l'enunciat el programa triga molt, per
    search2d(0.0,0.001,0.000001)            #aixo he posat intervals mes petits.
    #Valors originals(els de l'enunciat)
    #search2d(-6.0,6.0,0.01)
    #search2d(-6.0,6.0,0.001)
    #search2d(-6.0,6.0,0.000001)
#------------------------------------------------------------------------------------------#
# Definim la funcio d'avaluacio.
def puntx(r):
# Transformem els bits en un valor real x a l'interval [-1,2]
    sum=0.0
    for i in range(len(r)):
        sum = sum + r[i]*(2**i)
    x = -1.0 + sum * (3.0/(2.0**(len(r))-1.0))
    return x
#------------------------------------------------------------------------------------------#
def cost(r):
    # Avaluem el cromosoma x
    x = puntx(r)
    y = x * math.sin(10*math.pi*(x))+1.0
    return y
#------------------------------------------------------------------------------------------#
# Definim el creuament
def creuament(r1,r2):
    i=random.randint(1,len(r1)-2)
    return r1[:i]+r2[i:], r2[:i]+r1[i:]
#------------------------------------------------------------------------------------------#
# Definim la mutació amb probabilitat mutprob per cada bit
def mutacio(r,mutprob):
    for i in range(len(r)):
        if random.random()<mutprob: 
            if r[i]==0: r[i]=1
            else: r[i]=0
    return r
#------------------------------------------------------------------------------------------#
# Creem la població inicial
def initpop(n,long):
    # Generem una poblacio de n cromosomes de longitud long. 
    import random
    pop = [[0] * long for x in range(n)]
    for i in range(n):
        for j in range(long):
            if random.random()>0.5: pop[i][j] += 1 
    return pop
#------------------------------------------------------------------------------------------#
# Definim el proces de seleccio estandard
def seleccio_std(pop,cost,start=0):
    popsize=len(pop)
    # Calculem el valor minim de la funcio d'avaluacio   
    c=[cost(v) for v in pop[start:]]
    minim = min(c)  
    # Normalitzem els valors de manera que el pitjor 
    # individu tingui un valor 0.01
    if minim<0.0: 
        for i in range(len(c)): 
            c[i] = c[i] + abs(minim) + 0.01
    else: 
        for i in range(len(c)): 
            c[i] = c[i] - minim + 0.01
    # Calculem la suma de tots els valors de la funcio d'avaluacio
    sum=0.0
    for i in range(len(c)): sum = sum + c[i]
    # Triem l'individu de forma proporcional al seu valor d'adaptacio 
    ran=random.random()*sum
    i = 0
    sum2=c[0]
    while ran > sum2: 
        i += 1
        sum2=sum2+c[i]
    # Retornem l'individu seleccionat
    return i+start
#------------------------------------------------------------------------------------------#
# Definim l'algorisme genètic 
# Restriccio: popsize ha d'esser un nombre parell
def genetic(cost, cromsize=22, popsize=50, mutprob=0.01, maxiter=150):
    t1=time.clock()
    numAvalu=0
    # Generem la població inicial
    pop=initpop(popsize, cromsize)
    # Iterem fins al nombre de generacions
    for cont in range(maxiter):
        numAvalu=numAvalu+1
        # Avaluem la generacio i l'ordenem
        scores = [(cost(v),v) for v in pop]
        scores.sort(reverse=True)
        ranked=[v for (s,v) in scores]
        # Afegim els dos millors cromosomes a la següent generacío
        newpop=[0]*popsize
        newpop[0],newpop[1]=ranked[0],ranked[1]
        # Seleccionem les parelles 
        for i in range(0,popsize,2):        
            ind1=seleccio_std(ranked,cost,i)
            ranked[i],ranked[ind1]=ranked[ind1],ranked[i]
            ind2=seleccio_std(ranked,cost,i+1)
            ranked[i+1],ranked[ind2]=ranked[ind2],ranked[i+1]
        # Creuem les parelles i generem els fills
        new=[0]*popsize
        for i in range(0,popsize,2):
            new[i],new[i+1] = creuament(ranked[i],ranked[i+1])
        # Mutem
        mut=[0]*popsize
        for i in range(popsize):
            mut[i]=mutacio(new[i],mutprob)
        # Afegim els pares (excepte els dos millors) a la generació
        mut = mut + ranked[2:]
        # Seleccionem la resta d'individus per la següent generació
        for i in range(2,popsize):
            newpop[i]=mut[seleccio_std(mut,cost,i)]
        pop=newpop
    t2=time.clock()
    print "--------------------------------------------------------------------\n"
    print "f(x):", scores[0][0],
    print "x:", puntx(scores[0][1])
    print "El nombre d'avaluacions de la funcio cost es: "+str(numAvalu)
    print "El temps que ha trigat en calcular, ha estat : %0.3f ms\n\n\n" % ((t2-t1))
#---------------------------------- Trucades a les funcions -------------------------------#
main1() #Aquesta funcio correspon a la primera pagina de l'enunciat
main2() #Aquesta funcio correspon a la segona pagina de l'enunciat
genetic(cost) #Aquesta funcio correspon a la tercera pagina de l'enunciat
