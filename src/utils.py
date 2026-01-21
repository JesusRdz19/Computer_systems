def normalize_name(txt):
    """Esta funcion normaliza strings.
    Lo que hace es quitar espacios en blanco al inicio y final
    del string, los espacios en blanco los elimina.
    Y el nombre en titulo.
    
    Ej:
    cArlos AnToNiO  -> Carlos Antonio
    :params (str) : texto de entrada
    :return (str) : texto normalizado
    """
    
    return "".join(txt.strip().title().split())

def to_mxn(valor, tasa: float = 1.0):
    """Docstring for to_mxn
    Convierte valor numerico a MXN multiplicado por la tasa
    
    :param valor: Descripcion
    :param tasa: Descripcion
    :type tasa: float
    """
    
    return float(valor) * float (tasa)

