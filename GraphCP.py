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

def GenerarGrafo(lista):
    
    G = [[] for _ in range(len(lista))]

    for i in range(len(lista)):
        u = lista[i]
        
        dmax = 100
        
        while(len(G[i])< 2):
            
            for j in range(len(lista)):
                v = lista[j]
                
                d = round(haversine(u[1], u[2], v[1], v[2]), 2)
                
                if d > 0 and d < dmax and not j in G[i]:
                    G[i].append(j)
                    G[j].append(i)
                    
            dmax += 100
    
    return G

def find(ds, a):
    if ds[a] == a:
        return a
    else:
        parent = find(ds, ds[a])
        ds[a] = parent
        return parent
        
def unionQF(ds, a, b):
    pa = find(ds, a)
    pb = find(ds, b)
    
    if pa != pb:
        for i in range(len(ds)):
            if ds[i] == pb:
                ds[i] = pa

def sets(G):
    n = len(G)
    
    ds = [i for i in range(n)]

    for u in range(n):
        for v in G[u]:
            pu = find(ds, u)
            pv = find(ds, v)
            
            unionQF(ds, pu, pv)

    print(ds)
   
    if ds[1:] == ds[:-1]:
        print("Estamos unidos.")
    else:
        print("No estamos unidos :(")

def CP_Regionales():

    CPdoc = oxl.load_workbook("CR_25.xlsx")

    hoja = CPdoc[CPdoc.sheetnames[0]]

    RLista = []

    for fila in hoja.rows:
        if fila[7].value == "1":
            RLista.append([fila[5].value, fila[16].value, fila[15].value])
    
    G = GenerarGrafo(RLista)

#    sets(G)
    
    return G
    
print(CP_Regionales())
    
