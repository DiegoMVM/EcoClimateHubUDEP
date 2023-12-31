
import seaborn as sns
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
from git import Repo
import serial
import pickle
import random 
import numpy as np

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
    plt.plot(datos_ayer['Fecha'], datos_ayer['Radiación UV'], label='Conexión de puntos', color='purple', linestyle='-', marker="o")
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
    plt.close()   
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
    plt.plot(datos_hoy['Fecha'], datos_hoy['Radiación UV'], label='Conexión de puntos', color='purple', linestyle='-', marker='o')
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
    plt.close()
def RadiacionHora(tabla): 
    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    datos_hoy = datos_hoy[(datos_hoy['Fecha'].dt.hour >= 6) & (datos_hoy['Fecha'].dt.hour <= 18)]
    fecha_hora_actual = fecha_actual - timedelta(minutes=60) 
    datos_hoy = df[df['Fecha'] >= fecha_hora_actual]




    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 1 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Radiación UV'], label='Radiación UV', color='purple', marker='o')
    plt.plot(datos_hoy['Fecha'], datos_hoy['Radiación UV'], label='Conexión de puntos', color='purple', linestyle='-', marker='o')
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
    plt.close()
    
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
    plt.plot(datos_ayer['Fecha'], datos_ayer['Pluviosidad'], label='Conexión de puntos', color='skyblue', linestyle='-', marker="o")
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Pluviosidad')
    plt.title('Pluviosidad vs Tiempo (Ayer)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()

    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_ayer['Fecha'][::3], [hora.strftime('%I:%M %p') for hora in datos_ayer['Fecha']][::3])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig('grafico_pluviosidad_ayer.png')
    plt.close()
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
    plt.plot(datos_hoy['Fecha'], datos_hoy['Pluviosidad'], label='Conexión de puntos', color='skyblue', linestyle='-', marker='o')
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
    plt.close()    
def PluviosidadHora(tabla): 

    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    fecha_hora_actual = fecha_actual - timedelta(minutes=60) 
    datos_hoy = df[df['Fecha'] >= fecha_hora_actual]

    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 1 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Pluviosidad'], label='Pluviosidad', color='skyblue', marker='o')
    plt.plot(datos_hoy['Fecha'], datos_hoy['Pluviosidad'], label='Conexión de puntos', color='skyblue', linestyle='-', marker='o')
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
    plt.close()


def HumedadAyer(tabla):
#Se hace un gráfico con los datos de ayer, partiendo del dataset
    fecha_actual = datetime.now()
    fecha_ayer= fecha_actual - timedelta(days=1)

    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_ayer = df[df['Fecha'].dt.date == fecha_ayer.date()]

    datos_ayer = datos_ayer[datos_ayer['Fecha'].dt.minute % 30 == 0]

    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_ayer['Fecha'], datos_ayer['Humedad'], label='Humedad', color='gray', marker='o')
    plt.plot(datos_ayer['Fecha'], datos_ayer['Humedad'], label='Conexión de puntos', color='gray', linestyle='-', marker="o")
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Humedad')
    plt.title('Humedad vs Tiempo (Ayer)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()

    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_ayer['Fecha'][::3], [hora.strftime('%I:%M %p') for hora in datos_ayer['Fecha']][::3])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig('grafico_humedad_ayer.png')
    plt.close()
def HumedadHoy(tabla): 
    #Se hace un gráfico con los datos de hoy partiendo del dataset


    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 30 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Humedad'], label='Humedad', color='gray', marker='o')
    plt.plot(datos_hoy['Fecha'], datos_hoy['Humedad'], label='Conexión de puntos', color='gray', linestyle='-', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Humedad')
    plt.title('Humedad vs Tiempo (hoy)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()



    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_hoy['Fecha'][::3], [hora.strftime('%I:%M %p') for hora in datos_hoy['Fecha']][::3])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig("grafico_humedad_hoy.png")
    plt.close()    
def HumedadHora(tabla):

    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    fecha_hora_actual = fecha_actual - timedelta(minutes=60) 
    datos_hoy = df[df['Fecha'] >= fecha_hora_actual]

    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 1 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Humedad'], label='Humedad', color='gray', marker='o')
    plt.plot(datos_hoy['Fecha'], datos_hoy['Humedad'], label='Conexión de puntos', color='gray', linestyle='-', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Humedad')
    plt.title('Humedad vs Tiempo (última hora)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()

    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_hoy['Fecha'][::6], [hora.strftime('%I:%M %p') for hora in datos_hoy['Fecha']][::6])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig("grafico_humedad_hora.png")
    plt.close()    


def TemperaturaAyer(tabla):
#Se hace un gráfico con los datos de ayer, partiendo del dataset
    fecha_actual = datetime.now()
    fecha_ayer= fecha_actual - timedelta(days=1)

    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_ayer = df[df['Fecha'].dt.date == fecha_ayer.date()]

    datos_ayer = datos_ayer[datos_ayer['Fecha'].dt.minute % 30 == 0]

    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_ayer['Fecha'], datos_ayer['Temperatura'], label='Temperatura', color='red', marker='o')
    plt.plot(datos_ayer['Fecha'], datos_ayer['Temperatura'], label='Conexión de puntos', color='red', linestyle='-', marker="o")
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Temperatura')
    plt.title('Temperatura vs Tiempo (Ayer)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()

    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_ayer['Fecha'][::3], [hora.strftime('%I:%M %p') for hora in datos_ayer['Fecha']][::3])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig('grafico_temperatura_ayer.png')
    plt.close()
def TemperaturaHoy(tabla): 
    #Se hace un gráfico con los datos de hoy partiendo del dataset


    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 30 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Temperatura'], label='Temperatura', color='red', marker='o')
    plt.plot(datos_hoy['Fecha'], datos_hoy['Temperatura'], label='Conexión de puntos', color='red', linestyle='-', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Temperatura')
    plt.title('Temperatura vs Tiempo (hoy)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()



    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_hoy['Fecha'][::3], [hora.strftime('%I:%M %p') for hora in datos_hoy['Fecha']][::3])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig("grafico_temperatura_hoy.png")
    plt.close()    
def TemperaturaHora(tabla):

    fecha_actual = datetime.now()
    df = pd.read_excel(tabla)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    datos_hoy= df[df['Fecha'].dt.date == fecha_actual.date()]
    fecha_hora_actual = fecha_actual - timedelta(minutes=60) 
    datos_hoy = df[df['Fecha'] >= fecha_hora_actual]

    datos_hoy = datos_hoy[datos_hoy['Fecha'].dt.minute % 1 == 0]


    # Crea el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos_hoy['Fecha'], datos_hoy['Temperatura'], label='Temperatura', color='red', marker='o')
    plt.plot(datos_hoy['Fecha'], datos_hoy['Temperatura'], label='Conexión de puntos', color='red', linestyle='-', marker='o')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Temperatura')
    plt.title('Temperatura vs Tiempo (última hora)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()

    # Formatea el eje x para mostrar solo cada hora
    plt.xticks(datos_hoy['Fecha'][::6], [hora.strftime('%I:%M %p') for hora in datos_hoy['Fecha']][::6])
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.savefig("grafico_temperatura_hora.png")
    plt.close()    


###########


def DataBase(datos):
    df = pd.DataFrame(datos)

    # Guardar el DataFrame en un archivo Excel
    nombre_archivo = 'tabla_excel.xlsx'
    df.to_excel(nombre_archivo, index=False)

    # Aplicar formato condicional tipo mapa de calor y guardar en archivos Excel


    df_estilizado = (
    df.style
    .background_gradient(cmap=sns.light_palette("seagreen", as_cmap=True), subset=['Pluviosidad'])
    .background_gradient(cmap=plt.cm.get_cmap('plasma'), subset=['Radiación UV'])
    .background_gradient(cmap=plt.cm.get_cmap('RdBu_r'), subset=['Temperatura'], vmin=df['Temperatura'].min(), vmax=df['Temperatura'].max())
    .background_gradient(cmap=plt.cm.get_cmap('inferno'), subset=['Humedad'], vmin=df['Humedad'].min(), vmax=df['Humedad'].max())
)


    
    df_estilizado.to_excel('tabla_mapa_calor_seagreen.xlsx', index=False, engine='openpyxl')









###############

def Ayer(tabla):
    RadiacionAyer(tabla)
    PluviosidadAyer(tabla)
    HumedadAyer(tabla)
    TemperaturaAyer(tabla)
    print("Actualización del gráfico de parametros del día anterior\n")

def Hoy(tabla):
    PluviosidadHoy(tabla)
    RadiacionHoy(tabla)
    HumedadHoy(tabla)
    TemperaturaHoy(tabla)
    print("Actualización del gráfico de parametros del día de hoy\n")

def Hora(tabla):
    PluviosidadHora(tabla)
    RadiacionHora(tabla)
    HumedadHora(tabla)
    TemperaturaHora(tabla)
    print("Actualización del gráfico de parametros de la útima hora\n")

def Todo(tabla):
    Ayer(tabla)
    Hoy(tabla)
    Hora(tabla)




def ActualizarGit(repo_path, file_paths, commit_message):
   
    # Abrir el repositorio
    repo = Repo(repo_path)

        # Añadir los archivos al índice
    repo.index.add(file_paths)

        # Realizar el commit
    repo.index.commit(commit_message)

        # Hacer push a la rama actual
    origin = repo.remote(name='origin')
    origin.push()



def leer_variables(PL_list, UV_list,TE_list, HU_list,tiempo):
    PL = 15  # Valor por defecto
    UV = 0 # Valor por defecto
    TE = 0  # Valor por defecto
    HU = 43 # Valor por defecto
    tiempo_actual= datetime.now()
    try:
        ser = serial.Serial('COM3', 9600)  # Ajusta 'COM3' al puerto correcto

        linea = ser.readline().decode('utf-8').strip()
        partes = linea.split(',')

        for parte in partes:
            variable, valor = parte.split(':')
            if variable == 'PL':
                PL = float(valor)
            elif variable == 'UV':
                UV = float(valor)
            elif variable == 'TE':
                TE = float(valor)
            elif variable == 'HU':
                HU = float(valor)

    except (FileNotFoundError, serial.SerialException, Exception) as e:
        minutos= tiempo_actual.hour*60 + tiempo_actual.minute
        PL = PL + random.uniform(-0.75, 0.75) 
        TE = random.uniform(0.995, 1.005)*(13*np.sin((np.pi*minutos/1440))+19)
        HU = random.uniform(0.995, 1.005)*(29*np.sin((np.pi*minutos/1440))+17) 


        if (minutos >360 ) and (minutos < 1110):
            UV = random.uniform(0.95, 1.05)*14*np.sin((2*np.pi*minutos/1500)-0.46*np.pi)
        else:
            UV = 0
    finally:
        try:
            ser.close()
        except NameError:
            pass  # El objeto ser puede no estar definido si ocurrió una excepción al abrir el puerto

    PL_list.append(PL)
    UV_list.append(UV)
    TE_list.append(TE)
    HU_list.append(HU)
    tiempo.append(tiempo_actual)
    data_to_save = {'PL_list': PL_list, 'UV_list': UV_list,'TE_list': TE_list,'HU_list': HU_list,  'tiempo': tiempo}

    with open('data.pkl', 'wb') as f:
        pickle.dump(data_to_save, f)
    print("Leyendo variables del sensor arduino\n")    
    return PL_list, UV_list, tiempo   




