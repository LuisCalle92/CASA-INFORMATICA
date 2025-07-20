"""

Escribe un programa que solicite al usuario dos números y muestre su suma, resta, 
multiplicación, división, división entera y residuo (módulo).

"""

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "No se puede dividir entre 0"
division_entera = numero1 // numero2 if numero2 != 0 else "No se puede dividir entre 0"
modulo = numero1 % numero2 if numero2 != 0 else "No se puede dividir entre 0"

print("RESULTADOS")
print(f"La suma total es: {suma}")
print(f"La resta total es: {resta}")
print(f"La multiplicación total es: {multiplicacion}")
print(f"La división total es: {division}")
print(f"La división entera total es: {division_entera}")
print(f"El módulo total es: {modulo}")





