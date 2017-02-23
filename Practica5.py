#PRACTICA 5: PYTHON
#------------------------------------------------------------------------------------
#Calcul de la sequencia de fibonnaci recursivament
#Xavi Cano Granada
#------------------------------------------------------------------------------------
import time
import math
import random

def fib1():        
    a=0
    b=1
    while 1:
        yield a
        a, b = b, a + b
        
limit=input("Fins a quin numero vols calcular la sequencia de fibonacci?\n")
fibo = fib1() 
t1=time.clock()
for i in range(limit+1):       
    print fibo.next(),         

t2=time.clock()
print "\nEl temps que ha trigat en calular, ha estat: %0.3f ms" % ((t2-t1)*1000)
#------------------------------------------------------------------------------------
#Calcul del mcd utilitzant l'algoritme d'euclides
#Xavi Cano Granada
#------------------------------------------------------------------------------------
def mcd():          
    m = input("\nEcriu un numero:\n")
    n = input("Escriu un altre numero:\n")
    backupm=m
    backupn=n
    while m != 0:
        n, m=m, n%m
    print "El mcd de",backupm,"i",backupn,"es:",n


#------------------------------------------------------------------------------------
#Calcul de la cerca de tots els nombre primers fins a un numero determinat
#Xavi Cano Granada
#------------------------------------------------------------------------------------
def era1():                                     
    n = input("Fins a quin numero vols calcular?:\n")
    llist = range (2,n+1)
    resul = []
    count = 0
    while count < len(llist):
        aux = llist.pop(0)
        resul.append(aux)
        for i in range (len(llist)):
            if aux != 0:
                if llist[i] % aux == 0 and i < len(llist): 
                    llist.insert(i,0)
                    k= llist.pop(i+1)
        count = count +1
    for a in range(len(resul)):
        if resul[a] !=0 :
            print(resul[a]),
    for b in range(len(llist)):
        if llist[b] !=0 :
            print(llist[b]),


#------------------------------------------------------------------------------------
#Calcul del temps que tarda en calcular els nombres primers menors que 10.000.000
#Xavi Cano Granada
#------------------------------------------------------------------------------------
def era2():                                     
    n = 10000000
    llist = range (2,n+1)
    resul = []
    count = 0
    count2 = 0
    t1 = time.clock()
    while count < len(llist):
        aux = llist.pop(0)
        resul.append(aux)
        for i in range (len(llist)):
            if aux != 0:
                if llist[i] % aux == 0 and i < len(llist): 
                    llist.insert(i,0)
                    k= llist.pop(i+1)
        count = count +1
    t2 = time.clock()
    for a in range(len(resul)):
        if resul[a] !=0 :
            print(resul[a]),
            count2 = count2 + 1
    for b in range(len(llist)):
        if llist[b] !=0 :
            print(llist[b]), 
            count2 = count2 +1

    print "\nEl temps que ha trigat en calular, ha estat: %0.3f ms" % ((t2-t1)*1000)
    print "Els numeros primers que hi han son:",count2


#------------------------------------------------------------------------------------
#Calcul per saber si un nombre es primer mitjançant la tècnica de la factorització
#Xavi Cano Granada
#------------------------------------------------------------------------------------
def factorp():
    num=input("Escriu un numero\n")
    numbackup=num
    n = 1000
    llist = range (2,n+1)
    resul = []
    sortida=""
    count = 0
    llistaFinal=[]
    t1 = time.clock()
    while count < len(llist):
        aux = llist.pop(0)
        resul.append(aux)
        for i in range (len(llist)):
            if aux != 0:
                if llist[i] % aux == 0 and i < len(llist): 
                    llist.insert(i,0)
                    k= llist.pop(i+1)
        count = count +1
    for a in range(len(resul)):
        if resul[a] !=0 :
            llistaFinal.append(resul[a])
    for b in range(len(llist)):
        if llist[b] !=0 :
            llistaFinal.append(llist[b])
    t1 = time.clock()
    for k in range(len(llistaFinal)):
        if num % llistaFinal[k] == 0:   
            num=num/llistaFinal[k]
            k=0
        k=0
    t2 = time.clock()
    if num == 1:
        print "El numero",numbackup,":  Es primer"
    else:
        print "El numero",numbackup,":  No es primer"
    print "\nEl temps que ha trigat en calular, ha estat: %0.3f ms" % ((t2-t1)*1000)    
       


#------------------------------------------------------------------------------------
#Calcul per saber si un nombre es primer mitjançant la tècnica de fermat
#Xavi Cano Granada
#------------------------------------------------------------------------------------
def fermatp():
    n=input("Escriu un numero\n")
    a=[2,3,5]
    
    for i in range(len(a)):
        if pow(a[i],n-1) % n != 1:
            sortida=False            
    sortida=True

    print sortida
    


#Trucades a les funcions:---------------------------------------------------

#mcd()
#era1()
#era2()
#factorp()
#fermatp()

#----------------------------------------------------------------------------
