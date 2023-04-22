# programa que lee un numero N y da el total de numero pares e impares
# El programa termina cuando ingrese el cero (0)

num = int(input("ingrese la cantidad de numeros a leer: "))
pares = 0
impares = 0

for i in range(num):
    num2 = int(input("Ingrese un número para determinar si es par o impar: "))
    if num2 % 2 == 0:
        pares = pares+1
    else:
        impares = impares+1

print("La cantidad de números pares es:", pares)
print("La cantidad de números impares es:", impares)