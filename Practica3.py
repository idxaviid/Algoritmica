#PRACTICA 3: PYTHON
#---------------------------------------------------------------------------------
#Calcul de l'acronim d'una frase
#Xavi Cano Granada
#---------------------------------------------------------------------------------
import string

def acro():
    frase = raw_input("Escriu una frase\n")
    frase_acro = ''
    for i in range(len(frase)):
       if i== 0 and frase[i] != ' ':
           frase_acro = frase_acro + string.upper(frase[i])

       if frase[i] == ' ' and frase[i+1]!=' ' :
            frase_acro = frase_acro + string.upper(frase[i+1])

    print "L'acronim de la vostra frase es:",frase_acro

acro()

#---------------------------------------------------------------------------------
#Calcul contar nombre de paraules en una frase
#Xavi Cano Granada
#---------------------------------------------------------------------------------

def paraules():
    frase= raw_input("Escriu una frase\n")
    paraules= frase.split(' ')
    nombre_paraules=len(paraules)
    print "El nombre de paraules es :",nombre_paraules

paraules()

#---------------------------------------------------------------------------------
#Calcul del xifratge de Cesar
#Xavi Cano Granada
#---------------------------------------------------------------------------------

def cesar():
    clau=input("Sisplau, donam la clau[numero enter]\n")
    frase=raw_input("Escriu una frase\n")
    fraseXifrada=""
    for i in frase:
        numAscii=ord(i)
        fraseXifrada=fraseXifrada + chr(numAscii+clau)

    print "La frase xifrada es:",fraseXifrada
     
cesar()

#---------------------------------------------------------------------------------
#Calcul del xifratge de Cesar 2 
#Xavi Cano Granada
#---------------------------------------------------------------------------------

def lyrics():
    file = open("lletra.txt","r")
    text = file.readlines()
    file.close()
    f = open("lletra_cesar.txt","w")  
    fitxer_nou=""
    salto="\n"

    for line in text:
        for i in line:
                numAscii=ord(i)
                fitxer_nou=fitxer_nou + chr(numAscii+5)
                
        fitxer_nou=fitxer_nou +salto
        
    f.write(fitxer_nou)
    f.close() 

lyrics()

#---------------------------------------------------------------------------------
#Calcul de una sequencia dins d'un fitxer
#Xavi Cano Granada
#---------------------------------------------------------------------------------

def sequencia():

    file = open("lletra_cesar.txt","r")
    text = file.readlines()
    file.close()
    count=0

    for line in text:
        longitud=len(line)
        for i in range(longitud):
            if line[i] == 't' and line[i+1] == 'h':
                count=count+1
    print "A la lletra de la canso anterior,el numero de vegades que hi ha [th] es:",count

sequencia()

#---------------------------------------------------------------------------------
#Calcul de buscar una paraula dins d'un fitxer
#Xavi Cano Granada
#---------------------------------------------------------------------------------

def paraula():

    file = open("lletra.txt","r")
    text = file.readlines()
    file.close()
    paraula= raw_input("Escriu una paraula\n")
    paraula_bona=""+paraula+""
    contador=0
    
    for line in text:
        trobat=line.count(paraula_bona)
        contador+=trobat
        
    print "La paraula buscada esta:",contador,"vegades"

paraula()

                


            


    
    
