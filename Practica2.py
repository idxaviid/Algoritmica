# -*- coding: cp1252 -*-
#PRACTICA 2: PYTHON
#---------------------------------------------------------------------------------
#Calcul del valor futur
#Xavi Cano Granada
#---------------------------------------------------------------------------------
from math import * 

def futval():
    print "Aquest programa calcula el valor futur d'una determinada inversio a:\n"
    anys= input("Sisplau, entra el nombre d'anys\n")
    principal=input("Entra la inversio inicial: \n")
    apr= input("Entra l'interes anual: \n")
    for i in range(anys):
        principal= principal * (1 + apr)
    print "La quantitat al cap de",anys,"anys","es:", principal,"\n\n"

futval()
#---------------------------------------------------------------------------------
#Taula conversio de graus Celsius a Fahrenheit
#Xavi Cano Granada
#---------------------------------------------------------------------------------
def convert():
    print "Celsius º"+" ------------- "+"Fahrenheit º\n"
    for celsius in range(0,101,10):
        fahrenheit = 9.0/5.0 * celsius + 32
        print celsius,"       -------------- ",fahrenheit
    print "\n\n"

convert()
#---------------------------------------------------------------------------------
#Calcul de expresions
#Xavi Cano Granada
#---------------------------------------------------------------------------------
def exp():
    a=4.0/10.0+3.5*2
    b=10 % 4 + 6 / 2
    c=abs(4 - 20 / 3) ** 3
    e=3 * 10 / 3 + 10 % 3
    f=3L ** 3

    print "(a)=",a,"\n"
    print "(b)=",b,"\n"
    print "(c)=",c,"\n"
    print "(d)= Python no pot fer una arrel negativa\n" 
    print "(e)=",e,"\n"
    print "(f)=",f,"\n"

exp()
#---------------------------------------------------------------------------------
#Calcul pendent d'una recta
#Xavi Cano Granada
#---------------------------------------------------------------------------------
def punts():
    x1= input("Valor de x1?: \n")
    y1= input("Valor de y1?: \n")
    x2= input("Valor de x2?: \n")
    y2= input("Valor de y2?: \n")

    m=(y2-y1)/(x2-x1)
    print "La pendent de la recta que pasa per els punts","(",x1,",",y1,")"," i ","(",x2,",",y2,")","es:", m

punts()
#---------------------------------------------------------------------------------
#Calcul distancia euclidiana entre dos punts
#Xavi Cano Granada
#---------------------------------------------------------------------------------
def euclid():
    x1,y1 = input("Els valors del primer punt son:\n")
    x2,y2 = input("Els valors del segon punt son:\n")

    d=sqrt(((x2-x1)**2)+((y2-y1)**2))
    print "La distancia entre els punts","(",x1,",",y1,")"," i ","(",x2,",",y2,")","es:", d,"\n\n"

euclid()
#---------------------------------------------------------------------------------
#Calcul distancia euclidiana entre dos punts 2
#Xavi Cano Granada
#---------------------------------------------------------------------------------
def euclid2():
    x1,y1 = input("Els valors del primer punt son:\n")
    x2,y2 = input("Els valors del segon punt son:\n")

    d=sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
    b = d - floor(d)
    if b <0.5 :
        print "El nombre enter que mes s'apropa a la distancia es:",int (b)
    else :
        print "El nombre enter que mes s'apropa a la distancia es:",int (ceil(d))

euclid2()
#---------------------------------------------------------------------------------
#Calcul factorial d'un nombre natural
#Xavi Cano Granada
#---------------------------------------------------------------------------------
def factmenor():                                            
    valor = 1
    valorMax=6204484017332394393600000
    for i in range(1,100):
        valor = valor * i
        if valor <= valorMax:
            print "Valor:",valor,"------------- ","Nº iteracio:",i
        ++i
    
factmenor()

#---------------------------------------------------------------------------------
#Calcul suma nombres naturals
#Xavi Cano Granada
#---------------------------------------------------------------------------------
def suma():
    valor=0
    for i in range(1000):
        if i % 3 == 0 and i % 5 == 0:
            valor=valor + i 
    print "La suma de tots els nombres mes petits que 1000 i multiples de 3 i 5 es: ",valor
    
suma()

#---------------------------------------------------------------------------------
#Calcul divisió nombres naturals mes petits
#Xavi Cano Granada
#---------------------------------------------------------------------------------
def divisible():
    for i in range (1,30240):
        if i%8 == 0 and i%10 == 0 and i%6 == 0 and i%7 == 0 and i%9 == 0:
            print "El nombre natural més petit que és divisible per 2,3,4,5,6,7,8,9 i 10 es:",i
            break
    
divisible()

                  
