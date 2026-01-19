subtotal_txt = input("Subtotal (MXN): ")
iva_txt = input("IVA (%) ej. 16: ")
propina_txt = input("Propina (%) ej. 10: ")

try:
    subtotal = float(subtotal_txt)
    iva = float(iva_txt) / 100
    propina = float(propina_txt) / 100
except ValueError:
    print("Entrada inválida, asegúrate de ingresar números.")
    exit()

monto_iva = subtotal * iva
monto_propina = subtotal * propina
total = subtotal + monto_iva + monto_propina

print(f"Subtotal: ${subtotal}")
print(f"IVA: ${monto_iva}")
print(f"Propina: ${monto_propina}")
print(f"Total: ${total}")
