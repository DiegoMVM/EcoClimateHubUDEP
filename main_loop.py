#Se importan las librerias necesarias 
import subprocess

# Instalar todos los requerimientos
print("Comprobando e instalando requerimientos\n")
subprocess.run(f'pip install -r requirements.txt', shell=True)

#Se importan el resto de librerias
import seaborn as sns
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import time
import Crear
import funciones 
import schedule 
import pytz 
import os
from git import Repo
import serial
import pickle
print("Requerimientos instalados e importados\n")

#Se establece la zona horaria.
tz = pytz.timezone('America/New_York')
print("Zona horaria establecida como GMT-5\n")

#Se define el loop
def Loop(): 
    #Se carga la data anterior en caso exista. 
    try:
        with open('data.pkl', 'rb') as f:
            saved_data = pickle.load(f)
        PL_list = saved_data.get('PL_list', [])
        UV_list = saved_data.get('UV_list', [])
        TE_list = saved_data.get('TE_list', [])
        HU_list= saved_data.get('UV_list', [])
        tiempo = saved_data.get('tiempo', [])
        print("Obteniendo data almacenada anteriormente\n")

    except FileNotFoundError:
        PL_list = []
        UV_list = []
        TE_list=  []
        HU_list=  []
        tiempo = []
        print("Listas creadas\n")

    listas= [tiempo,
    PL_list,
    UV_list,
        TE_list,
        HU_list]
        
    large = []
    for lista in listas:
            large.append(len(lista))
    new_large= min(large)
    for lista in listas:
        lista= lista[:new_large]

    print(new_large)

    tiempo=tiempo[0:new_large]
    PL_list=PL_list[0:new_large]
    UV_list=UV_list[0:new_large]
    TE_list=TE_list[0:new_large]
    HU_list=HU_list[0:new_large]



    

    datos = {
        'Fecha': tiempo,
        'Pluviosidad': PL_list,
        'Radiación UV': UV_list,
        "Temperatura": TE_list,
        "Humedad": HU_list
    }

    #Se crea o inicializa la base de datos.
    import funciones
    funciones.DataBase(datos)
    print("Base de datos inicializada\n")

    #Se crean los gráficos. 
    tabla= 'tabla_excel.xlsx'
    funciones.Todo(tabla)
    print("Obteniendo gráficos\n")

    nuevos_archivos= ['grafico_pluviosidad_ayer.png','grafico_pluviosidad_hoy.png','grafico_pluviosidad_hora.png','grafico_radiacion_hora.png','grafico_radiacion_hoy.png','grafico_radiacion_ayer.png', 'grafico_temperatura_hora.png','grafico_temperatura_hoy.png','grafico_temperatura_ayer.png','grafico_humedad_hora.png','grafico_humedad_hoy.png','grafico_humedad_ayer.png','tabla_excel.xlsx','tabla_mapa_calor_seagreen.xlsx', "data.pkl"]
    
    funciones.ActualizarGit(os.getcwd(), nuevos_archivos, "Se actualizaron archivos")
    print("Subiendo gráficos al repositorio de GitHub\n")

    #Programar la actualizacion del grafico AYER
    schedule.every().day.at("00:00:03").do(funciones.Todo,tabla)


    # Programar la a tarea cada X minutos
    x= 1
    for minuto in range(0, 60, x):      
        schedule.every().hour.at(f":{minuto:02}").do(funciones.leer_variables,PL_list, UV_list,TE_list, HU_list,tiempo)
        schedule.every().hour.at(f":{minuto:02}").do(funciones.DataBase,datos)
        schedule.every().hour.at(f":{minuto:02}").do(funciones.Hora,tabla)
        schedule.every().hour.at(f":{minuto:02}").do(funciones.ActualizarGit,os.getcwd(), nuevos_archivos, "Se actualizaron archivos")
    

    # Programar la tarea cada media hora
    schedule.every().hour.at(":00").do(funciones.Hoy,tabla)
    schedule.every().hour.at(":30").do(funciones.Hoy,tabla)
    while True:
        schedule.run_pending()
        time.sleep(1)
        print("Esperando Actualizaciones de los sensores...\n")



Loop()
