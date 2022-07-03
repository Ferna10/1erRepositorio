import sys

if len(sys.argv) != 3:
    print("error, necesito 2 argumentos")
else:
    for elemento in range(int(sys.argv[2])):
        print(sys.argv[1])
