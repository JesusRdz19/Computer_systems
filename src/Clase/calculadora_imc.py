weight_txt = input ("Peso (Kg): ")
height_txt = input ("Altura (m): ")

try:
    weight = float(weight_txt)
    height = float(height_txt)
    imc = weight / height**2
    print(f"Tu IMC es {imc}")
    
except (ValueError, ZeroDivisionError):
    print("Datos invalidos. Ej. : Peso 80, Altura 1.80")
    
