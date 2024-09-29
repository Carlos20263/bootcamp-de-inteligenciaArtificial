#El primer tipo de dato compuesto que veremos será la lista

lista = ["Carlos Rosero", "tutoriales Carlos Rosero", True, 1.69]
# en el mundo de la programación no contamos del 1 al 10, contamos del 0 al 9
print(lista[1])
lista[0]="Caliche"
print(lista[0])

#la tupla es una lista que no se puede modificar
tupla = ("patacones", "chocalate", "pan", True, 9.00)
print(tupla[2])
#tupla[2] = "pan"
#print(tupla[2])

#Creando un conjunto set
#El conjunto no adminte elementos duplicados 
conjunto = {"Carlos Rosero", "tutoriales Carlos Rosero", True, 1.69, "Carlos Rosero"}
print(conjunto)
#Creando un enunciado
print(f"el conjunto es: {conjunto}")

#Creando un diccionario
diccionario = {
    "nombre": "Carlos",
    "apellidos": "Rosero",
    "estatura": 1.69,
    "está feliz": True,
    "apellido": "Rosero",
    "edad": 30
}
print(diccionario)
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["está feliz"])
print(diccionario["estatura"] + 2) #3.69
print(diccionario["edad"])
