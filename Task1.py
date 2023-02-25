# Importar módulos.  
import pandas as pd 
import sys

# Definir los argumentos.
FIELDS = sys.argv[1].split(',')
FROM = sys.argv[2]()
WHERE = sys.argv[3].split('#')[0]
VALUE = sys.argv[3].split('#')[1]

# Función principal:

def funcion_principal(FROM, WHERE, VALUE, FIELDS):
    records = []  # Crear una lista vacía para guardar los registros de la base de datos 
    with open(FROM) as f:
        record = {}  # Crear un diccionario vacío para almacenar los campos de los registros
        for line in f:
            line = line.strip()
            if line.startswith('ID'):
                if record:  # Iteración para agregar los registros a la lista 
                    records.append(record)
                record = {'id': line.split()[1]}  # Empezar un registro nuevo
            elif line.startswith('//'):
                if record:  # Agregar el último registro a la lista
                    records.append(record)
                record = {}  
            else:
                field = line[:2].strip()  # Extraer el campo (FIELD) 
                value = line[5:].strip()  # Extraer los valores del campo 
                if field in record:
                    record[field] += '\n' + value  # Concatenar múltiples líneas del mismo campo
                else:
                    record[field] = value  # Agregar un nuevo campo

    # Convertir la lista de diccionarios creados en un DataFrame de pandas.
    df = pd.DataFrame.from_records(records)

    # Filtrar los datos por la condición WHERE
    full_record = df[df[WHERE] == VALUE]

    # Agregar al DataFrame una nueva columna con el porcentaje del total de registros que coinciden con el query
    total_records = len(df)
    filtered_records = len(full_record)
    full_record['Percentage'] = round((filtered_records/total_records)*100, 2)

    # Seleccionar los FIELDS deseados
    filtered_record = full_record[FIELDS]

    # Dirigir los resultados a un archivo .fasta en caso de que el campo 'SQ' sea pedido en el query
    if 'sq' in FIELDS:
        with open('result.fasta', 'w') as f:
            for index, row in filtered_record.iterrows():
                f.write('>{}\n{}\n'.format(row['id'], row['sq']))
    else:
        print(filtered_record)

funcion_principal(FROM, WHERE, VALUE, FIELDS)
