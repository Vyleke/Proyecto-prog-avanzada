from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

print('********************CALCULADORA********************')

while True:
    print('\nEscriba el símbolo correspondiente a su operación:')
    print('"+" Suma | "-" Resta | "*" Multiplicación | "/" División | "!+" Suma Avanzada | "esc" Salir')
    signo = input("Operación: ")

    if signo == "esc":
        print('Gracias por usar Calculadora patito')
        break

    if signo == "!+":
        print('Ha elegido suma avanzada')
        cantidad = int(input('¿Cuántos números desea sumar?: '))
        numeros = []

        for i in range(cantidad):
            num = float(input(f'Ingrese el número {i+1}: '))
            numeros.append(num)

        resultado = suma_avanzada(numeros)
        print('La suma total es:', resultado)
        continue

    # Operaciones normales (2 números)
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Entrada no válida.")
        continue

    if signo == "+":
        print("Resultado:", sumar(num1, num2))
    elif signo == "-":
        print("Resultado:", restar(num1, num2))
    elif signo == "*":
        print("Resultado:", multiplicar(num1, num2))
    elif signo == "/":
        print("Resultado:", dividir(num1, num2))
    else:
        print("Operación no válida.")