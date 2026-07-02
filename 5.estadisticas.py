Módulo de ESTADÍSTICAS - Sistema de Pedidos de Comida
--------------------------------------------------------
Responsable: Brisa Alanis Rodriguez

# ---------- FUNCIONES DE CÁLCULO ----------
 
def cantidad_pedidos(pedidos):
    """Devuelve cuántos pedidos se registraron."""
    return len(pedidos)

def calcular_total_vendido(pedidos):
    """Suma el total de todos los pedidos usando un acumulador y un while."""
    total = 0
    contador = 0
    while contador < len(pedidos):
        total += pedidos[contador]["total"]
        contador += 1
    return total

def comida_mas_vendida(pedidos):
    """
    Recorre todos los pedidos y cuenta cuántas unidades se vendieron
    de cada producto. Devuelve una tupla (producto, cantidad).
    Si no hay pedidos, devuelve (None, 0).
    """
    conteo = {}
 
    i = 0
    while i < len(pedidos):
        items = pedidos[i]["items"]
 
        j = 0
        while j < len(items):
            producto = items[j]["producto"]
            cantidad = items[j]["cantidad"]
 
            if producto in conteo:
                conteo[producto] += cantidad
            else:
                conteo[producto] = cantidad
 
            j += 1
        i += 1
 
    if len(conteo) == 0:
        return None, 0
 
    producto_top = None
    cantidad_top = 0
    for producto, cantidad in conteo.items():
        if cantidad > cantidad_top:
            cantidad_top = cantidad
            producto_top = producto
 
    return producto_top, cantidad_top
