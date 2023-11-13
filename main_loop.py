#Se importan las librerias necesarias, y se inicializan las listas. 
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

tz = pytz.timezone('America/New_York')
def Loop(): 
    fecha_inicio = datetime(2023, 11, 5, 0, 0)
    #Se crean las listas si es que no existen
    # Comprobar si la lista existe
    try:
        x=tiempo
    except NameError:
        tiempo= Crear.CrearTiempo(fecha_inicio)
        
        print("se creo la lista tiempo")

    try:
        x=(PL_list)
    except NameError:
        PL_list= Crear.CrearParametro(tiempo,0,30)
        
        print("se creo la lista Pluviosidad")

    try:
        x=(UV_list)
    except NameError:
        UV_list= Crear.CrearParametro(tiempo,0,14)
        
        print("se creo la lista Radiacion ")


    datos = {
        'Fecha': tiempo,
        'Pluviosidad': PL_list,
        'Radiación UV': UV_list,
    }


    #Actualizamos la base de datos AL COMENZAR.
    import funciones
    funciones.DataBase(datos)

    #Se crean las imagenes. 
    tabla= 'tabla_excel.xlsx'
    funciones.Todo(tabla)

    nuevos_archivos= ['grafico_pluviosidad_ayer.png','grafico_pluviosidad_hoy.png','grafico_pluviosidad_hora.png','grafico_radiacion_hora.png','grafico_radiacion_hoy.png','grafico_radiacion_ayer.png','tabla_excel.xlsx','tabla_mapa_calor_seagreen.xlsx']
    funciones.ActualizarGit(os.getcwd(), nuevos_archivos, "Se actualizaron archivos")


    # Programar las actualizaciones automaticas
    schedule.every().day.at("00:00:03").do(funciones.Todo,tabla)

    # Programar la tarea cada X minutos
    x= 1
    for minuto in range(0, 60, x):
        schedule.every().hour.at(f":{minuto:02}").at.do(funciones.leer_variables,PL_list, UV_list,tiempo)
        schedule.every().hour.at(f":{minuto:02}").do(funciones.DataBase,datos)
        schedule.every().hour.at(f":{minuto:02}").do(funciones.Hora,tabla)
        schedule.every().hour.at(f":{minuto:02}").do(funciones.ActualizarGit,os.getcwd(), nuevos_archivos, "Se actualizaron archivos")
    

    # Programar la tarea cada media hora
    schedule.every().hour.at(":00").do(funciones.Hoy,tabla)
    schedule.every().hour.at(":30").do(funciones.Hoy,tabla)
    while True:
        schedule.run_pending()
        time.sleep(1)
        print("Esperando Actualizaciones...")


Loop()
