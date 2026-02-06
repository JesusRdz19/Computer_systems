names = []
print(names)

#Metodo append para agregar elementos al final de la lista.

names.append("Chuy")
names.append("Charly")
names.append("Martin")
names.append("Daniel")
names.append("Mancilla")


print(names)
print(type(names))
print(len(names))

#Metodo insert para agregar elementos en una posicion especifica.

names.insert(0, "Viktor")
print(names)

#Metodo pop() sin indice para eliminar el ultimo elemento de la lista.
names.pop()
print(names)

#Metodo pop() con indice para eliminar un elemento en una posicion especifica.
names.pop(2)
print(names)