import numpy as np

#Calculo el porcentaje de hombres y mujeres.
def porcentaje(i,j):
    male = round((i * 100)/(i+j))
    female = round((j * 100)/(i+j))
    return (male, female)


#En las edades quiero que coja sólo dos valores.
import re
import statistics
import numpy 
def ages(i):
    try:
        pattern = r'(\d{2})'
        busca = re.findall(pattern, i)
        return int(busca[0])

    except:
        return np.nan

#Agrupo las actividades por las que más ataques tienen.
def activity(x):
    if x == "Surfing": 
        return "Surfing"
    elif x == "Swimming": 
        return "Swimming"
    elif x == "Wading": 
        return "Wading"
    elif x == "Standing": 
        return "Standing"
    elif x == "Fishing": 
        return "Fishing"
    else:
        return "Other"
        
#Agrupo los nombres y los que no son.
def name(x):
    if x == "male": 
        return "NoName"
    elif x == "female": 
        return "NoName"
    elif x == "girl": 
        return "NoName"
    else:
        return x