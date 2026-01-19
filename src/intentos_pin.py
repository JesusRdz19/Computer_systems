"""
    (1) Este programa va a pedir al  usuario un pin de acceso, si el pin es 
    correcto el programa debe decir "Autenticacion exitosa, acceso concedido".
    (2) Si el pin es incorrecto, entonces el programa debe decir "Pin incorrecto" 
    y cantidad de intentos restantes 
    (3) Si el usuario supera el numero de intentos permitidos el programa debera 
    decir "Numero de intentos superado" y el  programa se bloquearia.
"""
PIN_CORRECTO = "1234"
INTENTOS_MAX = 3
intentos = 0

while intentos < INTENTOS_MAX:
    entrada = input("Ingresa tu pin (4 digitos): ")
    if entrada == PIN_CORRECTO:
        print("Autenticacion exitosa, acceso concedido")
        break
    else:
        intentos += 1
        restantes = INTENTOS_MAX - intentos
        if restantes > 0:
            print(f"Pin incorrecto. Quedan {restantes} intentos.")
        else:
            print("Numero de intentos superado. CUENTA BLOQUEADA.")