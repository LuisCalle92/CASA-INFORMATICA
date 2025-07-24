"""
Escribe un programa que tome una calificación numérica de un estudiante (entre 0 y 100)
y le asigne una letra según la siguiente tabla:

90-100: A
80-89: B
70-79: C
60-69: D
Menos de 60: F

"""
calificacion = int(input("Ingrese calificación: "))

if calificacion < 0 or calificacion > 100:
    print("Error: solo rango permitido de 0 a 100")
elif calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")


