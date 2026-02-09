# Problema 2 conversor de temperatura
c = float (input("Ingrese la temperatura en grados Celsius: "))
f = (c * 9/5) +32
k = c + 273.15
if k < 0:
    ValueError = "Error: La temperatura en Kelvin no puede ser negativa."
    print("Error, la temperatura en Kelvin no puede ser negativa.")
else:
    is_high = c > 30
    print( f"¿La temperatura es alta? {'Si' if is_high else 'No'}")
    print(f"Temperatura en grados Fahrenheit: {f:.2f} °F")
    print(f"Temperatura en grados Kelvin: {k:.2f} K")
ValueError = "Error: Ingresa una temperatura valida en grados Celsius."