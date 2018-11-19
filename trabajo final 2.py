
# coding: utf-8

# In[40]:


import math
def floydwarshall_ida(G):
    n = len(G)
    d = [[math.inf]*n for _ in range(n)]
    p = [[-1]*n for _ in range(n)]
          

    for u in range(n):
        d[u][u] = 0
        for v, w in G[u]:
            d[u][v] = w
            p[u][v] = v
          
    for k in range(n):
        for i in range(n):
            for j in range(n):
                f = d[i][k] + d[k][j]
                if d[i][j] > f:
                    d[i][j] = f
                    p[i][j] = k
                    
    return p, d


# In[157]:


import math
def floydwarshall_vuelta(G,r,x,y):
   
    n = len(G)
    d = [[math.inf]*n for _ in range(n)]
    p = [[-1]*n for _ in range(n)]
    
    for u in range(n):
        d[u][u] = 0
        for v, w in G[u]:          
            d[u][v] = w
            p[u][v] = v
    
   
    c=len(r)-2
    for k in range(c):
        t=False
        tt=False
        ttt=False
        a=r[k+1]
        for i in range(n-1):
            for j in range(n):
                if a<=i:
                    t=True
                    d[i][j]=d[i+1][j]
                    p[i][j]=p[i+1][j]
                    if a<y:
                        tt=True
                    if a<x:
                        ttt=True
                    
                        
        for j in range(n-1):
            for i in range(n):
                if a<=j:
                    d[i][j]=d[i][j+1] 
        if t==True :         
            n=n-1   
        if tt==True :         
            y=y-1  
        if ttt==True :         
            x=x-1  
          
   
    for k in range(n):
        for i in range(n):
            for j in range(n):
                f = d[i][k] + d[k][j]
                if d[i][j] > f:
                    d[i][j] = f
                    p[i][j] = k
    ruta(y,x,p,d)               
    return p, d


# In[35]:


import heapq
def r_find(x,y,p,r):
    if(p[x][y]==y): 
        heapq.heappush(r,p[x][y])
        return
    heapq.heappush(r,p[x][y])
    return r_find(p[x][y],y,p,r)


# In[76]:


import heapq
def ruta(x,y,p,d):
    print("la distancia es:")
    print(d[x][y])
    print("El recorrido es:")
    n=len(p)
    r = []
    heapq.heappush(r,x)
    r_find(x,y,p,r)
    print(r)
    return r


# In[141]:



G = [[(1, 4), (2, 8)],
     [(0, 4), (2, 1), (3, 2)],
     [(0, 8), (3, 4),(4,2)],
     [(1, 2), (2, 4),(4,7)],
     [(2, 2),(3,7)]]


# In[158]:


def floyd(G,x,y):
    p, d = floydwarshall_ida(G)
    r=ruta(x,y,p,d)
    p, d = floydwarshall_vuelta(G,r,x,y)
    


# In[159]:


floyd(G,0,4)

