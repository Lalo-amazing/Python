import random


def run():
   
    numero_aleatorio = random.randint(1, 100) #.accedemos a un punto de la función entero
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')



def menu():
    run()
    while (1):
        opcion = int(input("\n¿Desea hacer otro cálculo? (1. Si  2. No): "))
        if (opcion == 1):
            run()
        elif (opcion == 2):
            break


if __name__=="__main__":
   
   menu()