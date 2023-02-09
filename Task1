# Importar módulos.

import sys

# Definir la función de búsqueda.

def busqueda(file, string, query, fields):
  hits=0
  hits_analizados=0
  record=[]
  
  while True:
    line=file.readline()  
    if line.startswith("ID"):
      hits_analizados +=1
      record.clear()
      record=[line[:-1]]
    elif line.startswith("//"):
      
      for i in record:   
        if string in i.startswith(query):
          hits += 1     
    else:
      record.append(line[:-1])
    return hits_analizados, hits

hits_analizados, hits = busqueda(file, string, query, fields)
file.close()

file = open(uniprot_sprot.dat)
print("Hits obtenidos", hits)
print("Hits analizados ", hits_analizados)