"""
Encontrar el número más grande en un array
Escribe un programa que determine el mayor número en una lista.

"""

numeros = [7,3,100,1,0,10,9,4]

print(f"El número mayor de la lista es: {max(numeros)}")

###################################################
####################################################

numeros = [7,3,100,1,0,10,9,4]
mayor = numeros[0]

for i in numeros:
    if i > mayor:
        mayor = i

print(mayor)

####################################################
####################################################

# num = [5,50,10,100,200,65,1000,0,5000,90]
# mayor = 0

# for i in num:
#     if mayor < i:
#         mayor = i
# print(f"El numero mayor es: {mayor}")



