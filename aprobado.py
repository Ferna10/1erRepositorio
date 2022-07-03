import sys

if len(sys.argv) == 3:
    nota1 = int(sys.argv[1])
    nota2 = int(sys.argv[2])
    
    if (nota1 or nota2) > 10:
        print("Error, ingresa 2 notas del 0 al 10")
    elif nota1>= 7 and nota2>= 7:
        print("PROMOCIONADO")
    elif nota1>= 4 and nota2>=4:
        print("APROBADO, debe rendir final")
    elif nota1<4 and nota2 >=4:
        print( "DESAPROBADO debes recuperar primer parcial")
    elif nota1 >= 4 and nota2 <4:
        print("DESAPROBADO, debes recuperar el segundo parcial")
    elif (nota1 and nota2) < 4:
        print("DESAPROBADO, DEBERA RECURSAR")
else:
    print("ERROR, DEBE INGRESAR DOS NOTAS")