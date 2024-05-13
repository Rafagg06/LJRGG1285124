#Julio Rafael Guevara Gómez. Carné: 1285124

print("Semana no. 11: Ejercicio 2")
N = 0
while N <= 0:
    N = int(input("Ingrese un número mayor que 0: "))
    if N <= 0:
        print("El valor ingresado debe ser mayor a 0: ")
        print()

#el valor N ha sido leido

print("Laboratorio semana 11 ejercicio no.2")
n2 = int(input("Ingrese un número mayor a 0\n"))
a = 0
b = 0 
c = 0
i = 1
if n2 <= 0:
    print("Error, debe ser mayor a 0:")
else:
    while i < n2: 
        # Inciso A
        a = a + 1/i
        i = i + 1
    print("Resultado del Inciso a es:", a)  
    i = 1  
    # Inciso B
    while i < n2:  
        b = b + 1/2**i
        i = i + 1
    print("Resultado del Inciso b es:", b)  

x = int(input("Ingrese un número I\n: "))
a1 = int(input("Ingrese un número II\n: "))
n3 = int(input("Ingrese un número III\n: "))
# Inciso C
for i in range(0, n3 + 1):
    c = c + (x**i) + a1**(n3 - i)
print("Resultado del Inciso c es:", c)