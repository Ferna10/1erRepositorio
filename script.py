import sys

if len(sys.argv) != 3:
    print("error, necesito 2 argumentos")
else:
    for elemento in range(int(sys.argv[2])):
    # A traves del parametro argv[2] le estamos asignanado el limite mayor de nuestro RANGE,
    # por lo tanto imprimira el parametro argv[1] tantas veces como el numero que indiquemos en argv[2]
        print(sys.argv[1])

