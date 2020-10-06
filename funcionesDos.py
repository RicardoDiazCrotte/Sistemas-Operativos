
# Funcion para dividir dos enteros
def sumar(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def dividir(num1,num2):
    return num1/num2
# Funcion principal
def main():
    print("-- Programa para Mostrar funciones ---")
    # solicitar numero por el teclado
    num1 = int(input("Ingresa el valor del primer numero:"))
    num2 = int(input("Ingresa el valor del segundo numero:"))

    print("La suma es: ", sumar(num1,num2))
    print("La resta es: ", resta(num1,num2))
    print("La multiplicacion es: ", multiplicacion(num1,num2))
    print("La divicion es: ", dividir(num1,num2))

if __name__ == "__main__":
    main()
