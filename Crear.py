#Crear la lista de datos simuladas. 


from datetime import datetime, timedelta
import random

fecha_inicio = datetime(2023, 11, 5, 0, 0)


def CrearTiempo(fecha_inicio):
    delta_tiempo = timedelta(minutes=5)
    num_iteraciones = (datetime.now() - fecha_inicio) // delta_tiempo
    tiempo = [fecha_inicio + i * delta_tiempo for i in range(num_iteraciones + 1)]
    return tiempo

def CrearParametro(tiempo,limite1,limite2):
    longitud_lista = len(tiempo)

    # Inicializar UV_list con un valor inicial
    list = [random.uniform(limite1, limite2)]

    # Parámetros de variación
    max_variacion = 0.75
    probabilidad_continuar = 0.8  # Probabilidad de que el valor continúe en la misma dirección

    # Generar UV_list
    for i in range(1, longitud_lista):
        # Generar una variación aleatoria
        variacion = random.uniform(-max_variacion, max_variacion)

        # Determinar si el valor continuará en la misma dirección
        if random.random() < probabilidad_continuar:
            nuevo_valor = list[i - 1] + variacion
        else:
            nuevo_valor = list[i - 1] - variacion

        # Asegurar que el valor esté en el rango [0, 14]
        nuevo_valor = max(limite1, min(limite2, nuevo_valor))

        # Agregar el nuevo valor a UV_list
        list.append(nuevo_valor)
    return list

