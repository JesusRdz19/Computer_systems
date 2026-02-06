name = "Hola mundo"
print(name)
    
#Built- in method type 1
user_name = input ("Cual es tu nombre? ")
edad_txt = input ("Cual es tu edad? ")

print ("Hola " + user_name)
print (type(edad_txt ))
    
try:
        edad = int(edad_txt)
        print(edad)
        print(type(edad))
    
except ValueError:
        print("Error: la conversion no se puede realizar.")
        print("Debes ingresar un numero entero para la edad.")
        
print ("Fin del programa")
