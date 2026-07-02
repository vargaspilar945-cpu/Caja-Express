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

