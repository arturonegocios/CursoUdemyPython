import pandas
from moviepy.editor import *
import datetime
from datetime import time
from lib2to3.fixer_util import String
import os


# df = pandas.read_csv('tiempos_gps2.csv')

# duracion_video = time.fromisoformat("00:07:30")


# nom = geopy.ArcGIS()
 

# def get_address(coordinate):
#     try:
#         street = nom.reverse(coordinate)
#         return str(street)
#     except:
#         return get_address(coordinate)




# for i in range (len(df['Elapsed Time'])):

#     elapsed_time = time.fromisoformat(df['Elapsed Time'][i])
    
    
#     if elapsed_time<duracion_video:
#         with open('Subtitulos.srt', 'a+') as f:
#                 coordinate = (df['Latitude'][i],df['Longitude'][i])
#                 # address = get_address(coordinate)
                
#                 f.writelines(str(i+1)+'\n')
#                 # texto1 = str()
#                 f.writelines(df['Elapsed Time'][i]+' --> '+df['Elapsed Time'][i+1]+'\n')
#     #     #         # # texto2 = str()
#                 f.writelines('<i>'+' coord='+str(coordinate)+'</i>'+'\n')
#                 f.writelines("\n")
#                 print('progreso =', i )
#     else:
#         continue

def setPath(path):
    return path

def listaDeArchivos(dirName,extension):
    lista = []
    for archivo in os.listdir(dirName):
        if archivo.endswith("."+extension):
            lista.append(archivo)
        
    return lista

def tiempoDuracionArchivos(path,listaArchivos):
    lista = []
    try:
        for i in listaArchivos:
            video = VideoFileClip(path + i, audio= False)
            lista.append(video.duration)
        return lista
    except:
        print("problemas leyendo uno de los archivos")

def strToTimeConersion(time):
    #para formato 00:00:00
    timehour = int(time[0:2])
    timeMinute = int(time[3:5])
    timeSecond = int(time[6:8])
    intTime = timehour*3600+timeMinute*60+timeSecond
    return datetime.timedelta(seconds= intTime)

def pegarMultipleGpxCSV(path):
    listaDeDataframes = []
    dfFinal = pandas.DataFrame()
    listaArchivos = listaDeArchivos(path,"csv")
    listaColumnaTiempos = []
    listaColumnaLength = []
    ListaColumnaLatitud = []
    ListaColumnaLongitud = []
    print(listaArchivos)
    
    for i in listaArchivos:
        df = pandas.read_csv(i)
        listaDeDataframes.append(df)
            
    
    for i in range(len(listaDeDataframes)):
        
        listaTimeFirst =  listaDeDataframes[0]['Elapsed Time'].to_list()
        listaLengthFirst = listaDeDataframes[0]['Total Length'].to_list()
        
        if i> 0: 
            previousfilelastRowTime = strToTimeConersion(listaTimeFirst[-1])
            previousfilelastRowLength = listaLengthFirst[-1]
            listaTimescurrent = listaDeDataframes[i]['Elapsed Time'].to_list()
            listaLengthcurrent = listaDeDataframes[i]['Total Length'].to_list()
                                         
            for j in range(len(listaDeDataframes[i])):
                
                currentRowTime = strToTimeConersion(listaTimescurrent[j])
                currentRowLength = listaLengthcurrent[j]
                sumaTimes = currentRowTime + previousfilelastRowTime
                listaTimes.append(sumaTimes)
                sumaLength = currentRowLength + previousfilelastRowLength
                listaLength.append(sumaLength)
                
            
                
                # listaDeDataframes[i]['Elapsed Time'][j] =  sumaTimes
                # listaDeDataframes[i]['Length'][j] = sumaLength
               
                
    
    
    


        

    # dfFinal= dfFinal.append(listaDeDataframes)
    # dfFinal.to_csv("test.csv")






    



path = "C:/Users/arturo/Desktop/Projecto Agricola/OPenCV/"

pegarMultipleGpxCSV(path)

# archivos = listaDeArchivos(path,"mp4")
# print(archivos)
# listadetiempos = tiempoDuracionArchivos(path, archivos)
# print(listadetiempos)





        

        