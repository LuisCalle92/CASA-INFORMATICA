"""
Escribe un programa que solicite al usuario tres números
y determine cuál de ellos es el mayor.

"""
numero1 = int(input("Ingrese primer número: "))
numero2 = int(input("Ingrese segundo número: "))
numero3 = int(input("Ingrese tercer número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} es mayor")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} es mayor")
else:
    print(f"{numero3} es mayor")







