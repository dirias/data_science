def examen():
    # Constantes
    PI = int(input("Cual es el valor de PI?: "))
    G = 0
    r = 0
    R = int(input("Cual es el valor der radio?: "))
    h = int(input("Cual es el valor de la altura?: "))

    area = PI * (G * (r * R) + r**2 + R**2)
    Volumen = (PI * h * (R**2 + r**2 + R*r)) / 2 

#variable = input('Ingrese un número: ')


# Variables
string = 'Esto es un string'
interos = 20
decimales = 12.3
booleanos = False


# Calculadora

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
accion = int(input('Ingrese una opcion: \n1- Suma \n2- Resta \n3- Multiplicacion \n4- Division:\n__'))

if accion == 1:
    resultado = num1 + num2
elif accion == 2:
    resultado = num1 - num2
elif accion == 3:
    resultado = num1 * num2
elif accion == 4:
    resultado = num1 / num2
else:
    print('Esa opcion no es valida')

if accion in [1, 2, 3, 4]:
    print('El resultado es: ', resultado)
import pdb; pdb.set_trace()