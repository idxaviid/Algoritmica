# PRACTICA 1: PYTHON


#----------------------------------------------------
#Xavi Cano Granada
#Programa Numeric
#----------------------------------------------------
def ProgramaNumeric():
    a = 3-4+10
    b= 5*6
    c= 7.0/8.0
    print "These are the values: ",a,b,c
    print "Increment",a ,"and", b, "is"
    d=a+b
    print d
    number = input("Input a number\n")
    print number

ProgramaNumeric()


#----------------------------------------------------
#Xavi Cano Granada
#Un programa per pasar de graus Celsius a Farenheit
#----------------------------------------------------
def ConvertGraus():
    celsius= input("What is the Celsius temperature\n")
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print "The temperature is",fahrenheit

ConvertGraus()

#----------------------------------------------------
#Xavi Cano Granada
#Calcul de la nota promig entre dos examens.
#----------------------------------------------------
def NotaMitja():
    print "Aquest programa calcula el promig de la nota de dos exmanes."
    score1,score2 = input("Entra les notes de dos examens separades per una coma: \n")
    average=(score1 + score2) / 2.0
    print "El promig es:" , average

NotaMitja()
