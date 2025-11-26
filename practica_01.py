#Variables librerias globales
import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
data_path="data.txt"
stop_words=set(stopwords.words("spanish"))
"""
Funciones de limpieza de datos
Seccion 2.2 punto 1
"""
def read_data(data_path:str)->dict[int,str]:
    dicc={}
    with open(data_path,"r",encoding="utf-8") as f:
        for idx,line in enumerate(f):
            dicc[idx]=line
    return dicc
def extraer_alfabeticos(diccionario:dict[int,str])->dict[int,list[str]]:
    diccionario_filtrado={}
    for document in diccionario:
        diccionario_filtrado[document]=re.findall(r'[a-záéíóúñ]+',diccionario[document].lower())
    return diccionario_filtrado
def remover_acentos_string(palabra:str)->str:
    return palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
def quitar_acentos(diccionario:dict[int,list[str]])->dict[int,list[str]]:
    diccionario_sin_acentos={}
    for documento in diccionario:
        diccionario_sin_acentos[documento]=[remover_acentos_string(palabra) for palabra in diccionario[documento]]
    return diccionario_sin_acentos
def remover_palabras_vacias(diccionario:dict[int,list[str]],stop_words:set[str])->dict[int,list[str]]:
    diccionario_filtrado={}
    for documento in diccionario:
        diccionario_filtrado[documento]=[palabra for palabra in diccionario[documento] if palabra not in stop_words and
                                                                                                2<len(palabra)<21]
    return diccionario_filtrado 
def guardar_resultado(diccionario:dict[int,list[str]],nombre:str):
    with open(nombre,"w",encoding="utf-8") as file:
        for elementos in diccionario.values():
            file.write(f"{" ".join(elementos)}\n")
"""
Seccion 2.2 punto 2
"""
######################################
#def frecuencias(topico:str):
#    lista_de_palabras=topico.split(" ")
#    diccionario_frecuencias={}
#    for 
#def palabras_frecuentes(diccionario:[int,str]):
     

"""
Seccion 2.2 punto 1
Llamada de funciones de limpieza de datos
"""
documentos=read_data(data_path)
 
documentos_limpios=extraer_alfabeticos(documentos)
documento_sin_palabras_vacias=remover_palabras_vacias(documentos_limpios,stop_words)
documentos_sin_acentos=quitar_acentos(documento_sin_palabras_vacias)
guardar_resultado(documentos_sin_acentos,"data_processed.txt")
print(" indice\tnorma\tfiltrado")
for idx,valores in enumerate(zip(documentos.values(),documentos_sin_acentos.values())):
    normal=valores[0]
    filtrado=valores[1]
    print(f"{idx}\t|{len(normal)}\t|{len(filtrado)}")
"""
2.2 punto 2
"""
data_processed="data_processed.txt"
diccionario_procesado=read_data(data_processed)

