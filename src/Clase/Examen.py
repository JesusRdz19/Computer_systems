#Problema 1 Full name formatter
def normalize_text(text):
    """Normaliza el texto: elimina espacios extra y normaliza mayúsculas."""
    text = ' '.join(text.split())
    text = text.title()

    return text

full_name = input("Ingrese su nombre completo: ")
if not full_name.strip():
    print("Error: El nombre completo no puede estar vacío.")
else:
    full_name = normalize_text(full_name)
    
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Error: Por favor ingrese al menos un nombre y un apellido.")
    else:
        first_name = name_parts[0]
        last_name = name_parts[-1]
        print(f"Nombre: {first_name}")
        print(f"Apellido: {last_name}")
        initials = ''.join([name[0].upper() for name in name_parts])
        print(f"Iniciales: {initials}")