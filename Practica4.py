#PRACTICA 4: PYTHON
#---------------------------------------------------------------------------------------------------
#Calcul de la suma de els n primer nombres
#Xavi Cano Granada
#---------------------------------------------------------------------------------------------------
def mentre():

    numero = input("Sisplau, escriu un numero menor que 999\n")
    suma1=0
    suma2=0
    numVeg=0
    numero2=numero
    numInici=numero
    sumaTots=0

    while numero2 % 2 == 0:
        numVeg=numVeg+1
        numero2=numero2/2

    while numero != 999:
        sumaTots=sumaTots+numero
        for i in range(numero+1):
            suma1=suma1+i
            if i % 2 != 0:
                suma2=suma2+i

        numero = input("Escriu un altre numero per continuar o si vols finalitzar escriu 999\n")

    print "La suma dels",numInici,"primers nombres sencers es:",suma1
    print "La suma dels",numInici,"primers nombres senars es:",suma2
    print "La suma tots els nombres es:",sumaTots
    print "El nombre de vegades que es pot dividir per 2 el numero",numInici,"es:",numVeg

#mentre()

#---------------------------------------------------------------------------------------------------
#Calcul de temps que tarda en doblar un valor
#Xavi Cano Granada
#---------------------------------------------------------------------------------------------------

def inversio():
    interesAnu = input("Introdueix l'interes anual, Ex:[0.75]\n")
    valor = input("Introdueix un valor fix, Ex:[1000]\n")

    doble=valor*2
    cnt = 0

    while valor < doble:
        valor = valor * (1 + interesAnu)
        cnt = cnt +1

    print "El nombre d'anys que tarda en doblarse el valor es:",cnt

#inversio()

#---------------------------------------------------------------------------------------------------
#Calcul de temps que tarda en doblar un valor
#Xavi Cano Granada
#---------------------------------------------------------------------------------------------------

def nota():

    notaa = input("Introdueix una nota:")

    coleccio=["Suspens","Aprobat","Notable","Excelent","Matricula"]
    sortida=""

    if notaa < 5:
        sortida=coleccio[0]
    elif notaa >= 5 and notaa < 7:
        sortida=coleccio[1]
    elif notaa >= 7 and notaa < 9:
        sortida=coleccio[2]
    elif notaa>=9 and notaa < 10:
        sortida=coleccio[3]
    elif notaa == 10:
        sortida=coleccio[4]

    print "La qualificació quantitativa de", notaa,"es: "+sortida

#nota()

#---------------------------------------------------------------------------------------------------
#Calcul de la lletra del dni
#Xavi Cano Granada
#---------------------------------------------------------------------------------------------------

def dni():
    
    numDni = input("Introdueix un numero de dni\n")
    coleccio=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    lletra=0
    sortida=0

    if len(str(numDni)) < 8:
        print "El dni que has introduit es incorrecte"
    else:
        lletra= numDni % 23
        sortida=coleccio[lletra]

        print "La lletra del dni:",numDni,"es:",sortida

#dni()

#---------------------------------------------------------------------------------------------------
#Calcul de una coleccio aleatoria
#Xavi Cano Granada
#---------------------------------------------------------------------------------------------------

import random 

def llista():

    paraula = raw_input("Introdueix una paraula\n")
    llista=[]
    sortir="S"

    while paraula != sortir:

        llista.append(paraula)
        paraula = raw_input("Introdueix una altre paraula o 'S' per sortir\n")

    print "La llista de paraules ordenada de forma normal es:\n",llista    
    random.shuffle(llista,random.random)                                                       
    print "\nLa llista de paraules ordenada de forma aleatoria es:\n",llista
    
#llista()

#---------------------------------------------------------------------------------------------------
#Calcul de conversio string a alfabet fonetic OTAN
#Xavi Cano Granada
#---------------------------------------------------------------------------------------------------

def otan():
    diccionari = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo",
                  "F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliet",
                  "K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar",
                  "P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango",
                  "U":"Uniform","V":"Victor","W":"Whiskey","X":"Xray","Y":"Yankee",
                  "Z":"Zulu"}
    
    paraula = raw_input("Escriu una paraula en mayuscules:\n")
    valorsDicci=""
    
    for i in range(len(paraula)):
        valorsDicci=valorsDicci+diccionari[paraula[i]]+" "
        
    print paraula,"=",valorsDicci

#otan()
