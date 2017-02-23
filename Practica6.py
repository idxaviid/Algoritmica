#----------------------------------------------------#
#PRACTICA 6: PYTHON                                  #
#----------------------------------------------------#
#Calcul de buscar el cromosoma mes similar en un Adn #
#Xavi Cano Granada                                   #
#----------------------------------------------------#

import time


#-------------------------------------------- LECTURA DEL FITXER ----------------------------------------------
def llegirTxt():
    file = open("HUMAN-DNA.txt","r")
    text = file.readlines() #Llegeixo el text per linies y ho guardo en text
    file.close()
    return text #Retorno el text a la funcio que "hem cridi", en aquet cas sera a la funcio "Main".







#------------------------------------------ LEVENSTHEIN + CALCULS -------------------------------------------
def levens(first,second):
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length):
        distance_matrix[i][0] = i
    for j in range(second_length):
        distance_matrix[0][j] = 0 #Inicialitzo la primera fila a ceros, tal i com diu a l'enunciat de la practica.
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 2 #Cambio el cost,tal i com diu a l'enunciat de la practica
            insertion = distance_matrix[i][j-1] + 2 #Cambio el cost,tal i com diu a l'enunciat de la practica
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion,deletion, substitution)
    guardoVector=[1000,0]
    cromosoma=""
    for i in range(second_length):
        if distance_matrix[first_length-1][i] <= guardoVector[0]:
            guardoVector[0]=distance_matrix[first_length-1][i] #Distancia de edicio
            guardoVector[1]=i #Posicio
            cromosoma=second[(guardoVector[1]-first_length)+1:guardoVector[1]]#Cromosoma
    guardoVector[1]=guardoVector[1]-first_length+1
    llistaCompleta=[str(guardoVector[0]),str(guardoVector[1]-1),cromosoma]#Creo i guardo en un vector  3 coses,DistanciaEdicio,Posicio,Cromosoma.Els str() son per despres poder retornar correctament la llista, d'aquesta manera tot son strings.
    return llistaCompleta #Retorno el text a la funcio que "hem cridi", en aquet cas sera a la funcio "Main".







#--------------------------------------------------- MAIN ----------------------------------------------
#----------------------------------------- Calcul de primer patro --------------------------------------
def main():
    text=llegirTxt() #Truco a la funcio llegirTxt i el que hem retorni ho guardo en texto.
    longitud=len(text)
    distEdMin=-1
    t1=time.clock()
    patro1="AGATACATTAGACAATAGAGATGTGGTC" #Primer patro
    numlinea=""
    posicio=""
    distEd=""
    cromoSimilar=""
    for i in range(longitud):
        linea=text[i]
        vector2=levens(linea,patro1) #Truco a la funcio Levens i l'hi vaig pasan les linies del text , i tambe el pimer patro.
        if int(vector2[0])<=distEdMin or distEdMin==-1: #Vaig comparant la DistanciaEdicio i hem vaig guardan la minima en la variable minima.
            distEdMin=int(vector2[0])
            numlinea=str(i)
            posicio=vector2[1]
            distEd=vector2[0]
            cromoSimilar=vector2[2]
    print "El patro",patro1,"es troba a la linia",numlinea,", posicio",posicio,"del cromosoma 2 huma, i la seva distancia d'edicio es",distEd
    print "El substring del cromosoma huma mes semblant es",cromoSimilar
    t2=time.clock()
    print "El temps de calcul ha estat: ",str((t2-t1)*1000),"ms"
    print "\n\n"
#----------------------------------------- Calcul de segon patro --------------------------------------
    distEdMin=-1
    t1=time.clock()
    patro2="GTCAGTCTGGCCTTGCCATTGGTGCCACCA" #Segon patro
    numlinea=""
    posicio=""
    distEd=""
    cromoSimilar=""
    for i in range(longitud):
        linea=text[i]
        vector2=levens(linea,patro2) #Truco a la funcio Levens i l'hi vaig pasan les linies del text , i tambe el segon patro.
        if int(vector2[0])<=distEdMin or distEdMin==-1: #Vaig comparant la DistanciaEdicio i hem vaig guardan la minima en la variable minima.
            distEdMin=int(vector2[0])
            numlinea=str(i)
            posicio=vector2[1]
            distEd=vector2[0]
            cromoSimilar=vector2[2]
    print "El patro",patro2,"es troba a la linia",numlinea,", posicio",posicio,"del cromosoma 2 huma, i la seva distancia d'edicio es",distEd
    print "El substring del cromosoma huma mes semblant es",cromoSimilar
    t2=time.clock()
    print "El temps de calcul ha estat: ",str((t2-t1)*1000),"ms"
    print "\n\n"
#----------------------------------------- Calcul de tercer patro --------------------------------------
    distEdMin=-1
    t1=time.clock()
    patro3="TACCGAGAAGCTGGATTACAGCATGTACCATCAT" #Tercer patro
    numlinea=""
    posicio=""
    distEd=""
    cromoSimilar=""
    for i in range(longitud):
        linea=text[i]
        vector2=levens(linea,patro3) #Truco a la funcio Levens i l'hi vaig pasan les linies del text , i tambe el tercer patro.
        if int(vector2[0])<=distEdMin or distEdMin==-1: #Vaig comparant la DistanciaEdicio i hem vaig guardan la minima en la variable minima.
            distEdMin=int(vector2[0])
            numlinea=str(i)
            posicio=vector2[1]
            distEd=vector2[0]
            cromoSimilar=vector2[2]
    print "El patro",patro3,"es troba a la linia",numlinea,", posicio",posicio,"del cromosoma 2 huma, i la seva distancia d'edicio es",distEd
    print "El substring del cromosoma huma mes semblant es",cromoSimilar
    t2=time.clock()
    print "El temps de calcul ha estat: ",str((t2-t1)*1000),"ms"
    print "\n\n"


#-------------------------------------------- TRUCADES A LES FUNCIONS ---------------------------------

main()#En aquet cas nomes fa falta trucar al main, ja que el mateix ja s'encarregara de trucar a la resta.