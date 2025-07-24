"""
Contar números pares e impares en un array
Haz un programa que cuente cuántos números pares e 
impares hay en una lista.

"""
numeros = [2,1,7,3,5,11,14,10,22,55,31,13,4]
pares = 0
impares = 0

for i in numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Hay {pares} números pares y {impares} números impares en la lista.")


################################################################


# num = [2,5,8,9,15,10]
# par = []
# impar = []

# for i in num:
#     if i %2 == 0:
#         par.append(i)
#     else:
#         impar.append(i)
# print(f"Los números pares son: {len(par)} {par}")
# print(f"Los números impares son: {len(impar)} {impar}")
