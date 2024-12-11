def area_cuadrado(longitud):
    if not isinstance(longitud, (int, float)) or longitud < 1:
        raise TypeError("Los valores deben ser enteros positivos")
    return longitud * longitud
#Calcular area de un cuadrado