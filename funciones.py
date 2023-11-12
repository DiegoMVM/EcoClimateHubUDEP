
import seaborn as sns
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import requests
import base64 




def subir_archivo_github(nombre_archivo):
    url = f'https://api.github.com/repos/DiegoMVM/EcoClimateHubUDEP/contents/{nombre_archivo}'
    with open(nombre_archivo, 'rb') as file:
        contenido_base64 = base64.b64encode(file.read()).decode('utf-8')

    headers = {
        'Authorization': f'Bearer {"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"}',
        'Content-Type': 'application/json',
    }

    # Verificar si el archivo ya existe
    respuesta = requests.get(url, headers=headers)
    if respuesta.status_code == 200:
        sha = respuesta.json()['sha']
        mensaje = 'Actualizar archivo'
    elif respuesta.status_code == 404:
        sha = None
        mensaje = 'Añadir archivo'
    else:
        print(f'Error al obtener información del archivo: {respuesta.status_code}')
        return







    data = {
        'message': mensaje,
        'content': contenido_base64,
        'sha': sha,
    }

    respuesta = requests.put(url, headers=headers, json=data)

    if respuesta.status_code == 200 or respuesta.status_code == 201:
        print(f'Archivo subido exitosamente: {respuesta.json()["content"]["html_url"]}')
    else:
        print(f'Error al subir el archivo: {respuesta.status_code}')

################################################################

def RadiacionAyer(tabla):
    #Se hace un gráfico con los datos de ayer, partiendo del dataset
    fecha_actual = datetime.now()
    fecha_ayer= fecha_actual - timedelta(days=1)

    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_ayer = df[df['Fecha'].dt.date == fecha_ayer.date()]
    datos_ayer = datos_ayer[(datos_ayer['Fecha'].dt.hour >= 6) & (datos_ayer['Fecha'].dt.hour <= 18)]
    datos_ayer = datos_ayer[datos_ayer['Fecha'].dt.minute % 30 == 0]

    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_ayer['Fecha'], datos_ayer['Radiación UV'], label='Radiación UV', color='purple', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Radiación UV')
    plt.title('Radiación UV vs Tiempo (Ayer)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()



    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_ayer['Fecha'][::6], [hora.strftime('%I:%M %p') for hora in datos_ayer['Fecha']][::6])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig('grafico_radiacion_ayer.png')
    subir_archivo_github('grafico_radiacion_ayer.png')
def RadiacionHoy(tabla):

    #Se hace un gráfico con los datos de hoy partiendo del dataset
    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    datos_hoy = datos_hoy[(datos_hoy['Fecha'].dt.hour >= 6) & (datos_hoy['Fecha'].dt.hour <= 18)]
    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 30 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Radiación UV'], label='Radiación UV', color='purple', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Radiación UV')
    plt.title('Radiación UV vs Tiempo (hoy)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()



    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_hoy['Fecha'][::6], [hora.strftime('%I:%M %p') for hora in datos_hoy['Fecha']][::6])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig('grafico_radiacion_hoy.png')
    subir_archivo_github('grafico_radiacion_hoy.png')

def RadiacionHora(tabla): 
    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    datos_hoy = datos_hoy[(datos_hoy['Fecha'].dt.hour >= 6) & (datos_hoy['Fecha'].dt.hour <= 18)]
    fecha_hora_actual = fecha_actual - timedelta(minutes=60) 
    datos_hoy = df[df['Fecha'] >= fecha_hora_actual]




    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 5 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Radiación UV'], label='Radiación UV', color='purple', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Radiación UV')
    plt.title('Radiación UV vs Tiempo (última hora)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()



    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_hoy['Fecha'][::6], [hora.strftime('%I:%M %p') for hora in datos_hoy['Fecha']][::6])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig('grafico_radiacion_hora.png')
    subir_archivo_github('grafico_radiacion_hora.png')
def PluviosidadAyer(tabla):
#Se hace un gráfico con los datos de ayer, partiendo del dataset
    fecha_actual = datetime.now()
    fecha_ayer= fecha_actual - timedelta(days=1)

    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_ayer = df[df['Fecha'].dt.date == fecha_ayer.date()]

    datos_ayer = datos_ayer[datos_ayer['Fecha'].dt.minute % 30 == 0]

    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_ayer['Fecha'], datos_ayer['Pluviosidad'], label='Pluviosidad', color='skyblue', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Pluviosidad')
    plt.title('Pluviosidad UV vs Tiempo (Ayer)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()



    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_ayer['Fecha'][::3], [hora.strftime('%I:%M %p') for hora in datos_ayer['Fecha']][::3])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig('grafico_pluviosidad_ayer.png')
    subir_archivo_github('grafico_pluviosidad_ayer.png')

def PluviosidadHoy(tabla): 
    #Se hace un gráfico con los datos de hoy partiendo del dataset


    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 30 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Pluviosidad'], label='Pluviosidad', color='skyblue', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Pluviosidad')
    plt.title('Pluviosidad vs Tiempo (hoy)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()



    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_hoy['Fecha'][::3], [hora.strftime('%I:%M %p') for hora in datos_hoy['Fecha']][::3])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig("grafico_pluviosidad_hoy.png")
    subir_archivo_github("grafico_pluviosidad_hoy.png")
def PluviosidadHora(tabla): 

    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    fecha_hora_actual = fecha_actual - timedelta(minutes=60) 
    datos_hoy = df[df['Fecha'] >= fecha_hora_actual]

    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 5 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Pluviosidad'], label='Pluviosidad', color='skyblue', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Pluviosidad')
    plt.title('Pluviosidad vs Tiempo (última hora)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()



    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_hoy['Fecha'][::6], [hora.strftime('%I:%M %p') for hora in datos_hoy['Fecha']][::6])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig("grafico_pluviosidad_hora.png")
    subir_archivo_github("grafico_pluviosidad_hora.png")
###########


def DataBase(datos):
    df = pd.DataFrame(datos)

    # Guardar el DataFrame en un archivo Excel
    nombre_archivo = 'tabla_excel.xlsx'
    df.to_excel(nombre_archivo, index=False)
    archivos = ['tabla_mapa_calor_seagreen.xlsx']
    mapas_colores = {'seagreen': sns.light_palette("seagreen", as_cmap=True)}

    # Aplicar formato condicional tipo mapa de calor y guardar en archivos Excel
    for nombre_archivo, mapa_color in zip(archivos, mapas_colores.values()):
        df_estilizado = df.style.background_gradient(cmap=mapa_color, subset=['Pluviosidad', 'Radiación UV'])
        df_estilizado.to_excel(nombre_archivo, index=False, engine='openpyxl')
    subir_archivo_github('tabla_excel.xlsx')
    subir_archivo_github('tabla_mapa_calor_seagreen.xlsx')


###############

def Ayer(tabla):
    RadiacionAyer(tabla)
    PluviosidadAyer(tabla)

def Hoy(tabla):
    PluviosidadHoy(tabla)
    RadiacionHoy(tabla)

def Hora(tabla):
    PluviosidadHora(tabla)
    RadiacionHora(tabla)


def Todo(tabla):
    Ayer(tabla)
    Hoy(tabla)
    Hora(tabla)






