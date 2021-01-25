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