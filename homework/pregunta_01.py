"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import pandas as pd
import re
# pylint: disable=import-outside-toplevel

def pregunta_01():
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        

        head = []
        for line in lines[:2]:
            line = re.split(r"\s{2,}", line.strip())
            head.append(line)
        head[0][1] = head[0][1] + " " + head[1][0]
        head[0][2] = head[0][2] + " " + head[1][1]
        head = head[:-1]
        columns = [i.lower().replace(" ", "_") for i in head[0]]
        

        data = "".join(lines[4:])
        data = re.split(r"\n\s*\n", data)
        data = data[:-1]

        table = []

        for entry in data:
            entry = entry.replace("\n", " ")  
            entry = re.sub(r"\s{4,}", "|", entry.strip())
            parts = entry.split("|", 3)

            cluster = int(parts[0])
            cantidad = int(parts[1])
            porcentaje = float(parts[2].replace(",", ".").replace(" %", ""))
            clave = parts[3]
            clave = clave.replace("|", " ")
            clave = re.sub(r"\s{2,}", " ", clave)
            clave = re.sub(r"\s*,\s*", ", ", clave).strip().rstrip(".")

            table.append([cluster, cantidad, porcentaje, clave])

    df = pd.DataFrame(table, columns=columns)
    return df


    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
if __name__ == "__main__":
    print(pregunta_01())