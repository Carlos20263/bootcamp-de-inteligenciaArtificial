#Operadores numericos 

a = 10
b = 3
print("suma:", a > b)
print("resta:", a < b)
print("multiplicación:", a * b)
print("division:", a / b)

#En python se utiliza el signo % para obtener el residuo de la división 

print("modulo:", a % b)

#En python como en matemáticas dividir entre 0 es un error 

#Division entera
print("division entera:", a // b)

#Potenciación
print("potencia:", a ** b)

#Para sumarle n valor a la variable A se podria poner a= a+n o mejor:

a += 2
print(a)

#PEMDAS 
operacion_1 = 2 + 3 * 4 
operacion_2 = 2 + (3 * 4)
operacion_3 = (2 + 3) * (4 ** 2) / 8 - 1

print(operacion_1)
print(operacion_2)
print(operacion_3)

#Comparaciones 
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)