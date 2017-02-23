#-----------------------------------#
#       PRACTICA 7: PYTHON          #
#-----------------------------------#
#       Xavi Cano Granada           #
#-----------------------------------#
import random
import math
#--------------- Funcio Exponent ----------------#
def exponent(a,n):
    if n > 1:
        return exponent(a,math.floor(n/2.0))*exponent(a,math.ceil(n/2.0))        #Aixo va fent divideix i venceras amb la formula que ens dona l'enunciat.Les funcions ceil() i floor() son per arrodonir el resultat al enter mes gran i mes petit.
    else:
        return a
        
#--------------- Funcio reverse -----------------#
def reverse(string):
    if len(string) < 2:                                                          #Si la longitud del string que hem pasan es menor a 2,
        return string                                                            #retorno el string tal y com esta.
    else:
        meitat = len(string)/2                                                   #Parteixo l'string per la meitat
        esquerra = reverse(string[:meitat])                                      #Hem guardo el que hi ha a l'string desde la posicio 0 fins a la meitad.
        dreta = reverse(string[meitat:])                                         #Hem guardo el que hi ha a l'string desde la meitat fins l'ultima posicio.
        return dreta + esquerra                                                  #Retorno les dues particions(esquerra,dreta) pero amb l'orde intercanviat.
    
#--------------- Funcio negatius -----------------#

def negatius(list):
    if list == []: 
        return []
    else:
        pivot = list[0]
        menors = negatius([x for x in list[1:] if x < pivot])                    #Hem guardo els numeros menors que el pivot, es a dir tots els negatius.
        menorsIzq = negatius([x for x in menors[0:1] if x < pivot])              #Parteixo de nou els numeros menors
        menorsDer = negatius([x for x in menors[1:] if x != menorsIzq])          #Parteixo de nou els numeros menors
        majors = negatius([x for x in list[1:] if x >= pivot])                   #Hem guardo els numeros majors que el pivot, es a dir tots els positius.
        majorsIzq = negatius([x for x in majors[0:1] if x > pivot])              #Parteixo de nou els numeros majors
        majorsDer = negatius([x for x in majors[1:] if x != majorsIzq])          #Parteixo de nou els numeros majors
        return menorsDer + menorsIzq + [pivot] + majorsDer + majorsIzq           #Intercanvio l'ordre dels menors i dels majors, d'aquesta manera sempre estaran desordenats i a la vegada ordenats de negatius a positius.
#                    Negatius             1             Positius


#----------- Trucades a les funcions --------------#
#print exponent(3,5)
#print reverse("hola, com estas?")
#print negatius([1,-2,3,-4,-3,5,6])
