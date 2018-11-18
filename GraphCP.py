# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:07:17 2018

@author: Milagros
"""

# Grafo - Capitales Regionales

import math
import openpyxl as oxl


def haversine(lat1, lon1, lat2, lon2):
    rad = math.pi/180
    dlat = lat2-lat1
    dlon = lon2-lon1
    R = 6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

def generarGrafo(filename):

    CPdoc = oxl.load_workbook(filename)

    hoja = CPdoc[CPdoc.sheetnames[0]]

    RLista = []

    for fila in hoja.rows:
        RLista.append([fila[5].value, fila[16].value, fila[15].value])
    
    G = [[] for _ in range(len(RLista))]

    for i in range(len(RLista)):
        
        u = RLista[i]
        
        dmax = 100
        
        while(len(G[i])< 2):
            
            for j in range(len(RLista)):
                v = RLista[j]
                
                d = round(haversine(u[1], u[2], v[1], v[2]), 2)
                
                if d > 0 and d < dmax and not j in G[i]:
                    G[i].append(j)
                    G[j].append(i)
                    
            dmax += 100
            
    return G
   

print(generarGrafo("CR_25.xlsx")) #segundos
#print(generarGrafo("CP_171.xlsx")) #segundos
#print(generarGrafo("CD_1678.xlsx")) #1 min aprox
#print(generarGrafo("CP_143351.xlsx")) #casi 15 min 

   
