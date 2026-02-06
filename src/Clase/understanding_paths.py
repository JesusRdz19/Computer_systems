from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
print(BASE)

raw = BASE / "data" / "raw"
clean = BASE / "data" / "clean"
#Crear carpetas
raw.mkdir(parents=True, exist_ok=True)
clean.mkdir(parents=True, exist_ok=True)

#Escribir a txt

txt_patth = raw/ "notas.txt"
txt_patth.write_text("Notas chuy\n commo andan \n ya es viernes", encoding="utf-8")

contenido = txt_patth.read_text(encoding="utf-8")
print(contenido)