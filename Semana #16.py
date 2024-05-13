import random

# Actividad 1
print("Semana No. 16: Ejercicio 1")
A = []
for i in range(10):
    r = random.randint(1, 100)
    A.append(r)
print("Los números ingresados son:", A)
promedio = sum(A) / len(A)
print("El promedio es:", promedio)
print("La longitud del arreglo es:", len(A))
sumapar = sum(A[::2])
sumaimpar = sum(A[1::2])
print("La suma de posiciones pares es:", sumapar)
print("La suma de posiciones impares es:", sumaimpar)

# Actividad 2
print("\nSemana No. 16: Ejercicio 2")
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

B = []
for i in range(filas):
    temporal = []
    for j in range(columnas):
        r = random.randint(0, 1000)
        temporal.append(r)
    B.append(temporal)
print("La matriz generada es:")
for fila in B:
    print(fila)
numeros_pares = sum(1 for fila in B for num in fila if num % 2 == 0)
numeros_impares = sum(1 for fila in B for num in fila if num % 2 != 0)
numero_mayor = max(max(fila) for fila in B)
numero_menor = min(min(fila) for fila in B)

print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)
print("Número mayor:", numero_mayor)
print("Número menor:", numero_menor)
