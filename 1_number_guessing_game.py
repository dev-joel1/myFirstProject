import random
import math

#? Tomando entradas
lower = int(input('Enter lower bound:- '))

upper = int(input('Enter upper bound:- '))

#? Generando numeros aleatorios entre
#? el lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

#? Inicializando el número de conjeturas.
count = 0

#? para el cálculo del número mínimo de
#? las conjeturas dependen del rango

while count < math.log(upper - lower + 1, 2):
    count += 1

    #? tomando como entrada el número de adivinanzas
    guess = int(input("Guess a number:- "))

    #? Prueba de condición
    if x == guess:
        print("Congratulations you did it in ", count, " try")
        
        #? Una vez adivinado, el bucle se romperá.
        break
    elif x > guess:
        print("You guesses too small!")
    elif x < guess:
        print("You guessed too high!")

#? Si las conjeturas son más que las conjeturas requeridas,
#? muestra esta salida.
if count >= math.log(upper -lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")