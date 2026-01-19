print("Este programa captura importes")
info = """
        Este programa lleva el control del conteo de cuantos importes 
        ha introducido el usuario.
        
        Va acumulando todos los importes que el usuario ingresa.
        
        Si el usuario desea terminar el pprograma puede escribir cualquier 
        momento la palabra exit, quit, terminar.
        """
    
print(info)
conteo = 0
suma = 0.0
minimo = None
maximo = None

while True:
    user_message = """
    Ingresa tu importe (MXN)
    Si quieres dejar de cargar importes
    puedes escribir exit, quit, terminar
    """
    
    line = input(user_message).lower()
    if line == "exit" or line == "quit" or line == "terminar":
        break
    try:
        value = float(line)
    except ValueError:
        print("Ingresaste valor no valido, intenta de nuevo, Ej. 20.5")
        continue
    
    conteo += 1 #Conteo de valores ingresados
    suma += value #Suma de valores ingresados (Acumulacion)
    if minimo is None or value < minimo:
        minimo = value
    if maximo is None or value > maximo:
        maximo = value
if conteo == 0:
    print("No ingresaste ningun importe")
else:
    print("="*32)
    print("La cantidad de numeros ingresados es:" , f"{conteo}")
    print("La suma de los  numeros es: ", f"{suma}")
    print("El minimo es: ", f"{minimo}")
    print("El maximo es: ", f"{maximo}")
print("Programa finalizado")