lista = ["Numpy",
         "Pandas",
         "Scitik-learn",
         "Tensorflow",
         "Keras"]
print(lista)
mix = ["uno", 2, 3.14,True,[1,2,4] ]
print(mix)
print (len(mix))
print("primer elemento:", mix[0])
print("primer elemento:", mix[1])
print("ultimo elemento:", mix[-1])
string = "Numpy"
print("primer elemento:", string[0])
print("segundo elemento:", string[1])
print("cuarto elemento:", string[-1])
print (mix[0:2])
print (mix[:2])
print (mix[2:])
print (mix[2:-2])
mix.append (["Romulo", "Nancy"])
mix.insert(0, "Jheyson Galvis")
print(mix)
print (mix.index("Jheyson Galvis"))
numbers =[ 1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))
print("mayor:", max(numbers))
print("menor:", min(numbers))
print (numbers)
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
#print(numbers)