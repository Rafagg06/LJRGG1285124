#Rafael Guevara
#1285124
def metros_to_millas(metros):
    return metros / 1609.34

def metros_to_kilometros(metros):
    return metros / 1000

def metros_to_pies(metros):
    return metros * 3.28084

def metros_to_pulgadas(metros):
    return metros * 39.3701

def main():
    metros = float(input("Ingrese la cantidad en metros: "))

    millas = metros_to_millas(metros)
    kilometros = metros_to_kilometros(metros)
    pies = metros_to_pies(metros)
    pulgadas = metros_to_pulgadas(metros)

    print(f"{metros} metros son:")
    print(f"{millas} millas")
    print(f"{kilometros} kilómetros")
    print(f"{pies} pies")
    print(f"{pulgadas} pulgadas")

if __name__ == "__main__":
    main()

