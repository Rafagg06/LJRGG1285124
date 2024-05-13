# Paso 1: Mostrar el texto inicial
print("Semana No. 10: Ejercicio 1")

# Paso 2: Solicitar al usuario ingresar el número de mes
numero_mes = int(input("Por favor, ingresa el número de mes (1-12): "))

# Paso 3: Validar si el número de mes está dentro del rango válido
if numero_mes < 1 or numero_mes > 12:
    print("Error: El número a ingresar debe estar contenido entre 1 y 12")
else:
    # Paso 4: Determinar el nombre del mes correspondiente al número ingresado
    if numero_mes == 1:
        nombre_mes = "Enero"
    elif numero_mes == 2:
        nombre_mes = "Febrero"
    elif numero_mes == 3:
        nombre_mes = "Marzo"
    elif numero_mes == 4:
        nombre_mes = "Abril"
    elif numero_mes == 5:
        nombre_mes = "Mayo"
    elif numero_mes == 6:
        nombre_mes = "Junio"
    elif numero_mes == 7:
        nombre_mes = "Julio"
    elif numero_mes == 8:
        nombre_mes = "Agosto"
    elif numero_mes == 9:
        nombre_mes = "Septiembre"
    elif numero_mes == 10:
        nombre_mes = "Octubre"
    elif numero_mes == 11:
        nombre_mes = "Noviembre"
    else:
        nombre_mes = "Diciembre"
    
    # Paso 5: Mostrar el resultado en pantalla
    print("MES:", nombre_mes)
