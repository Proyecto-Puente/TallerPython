# Ejercicio 6
# Taller: introducción a python
# Día 9

# Consigna:
#   Elabore una función que obtenga la ruta de un archivo csv y xlsx, e
#   inserte las filas del csv en la hoja de cálculo.


def csv_xlsx(ruta_archivo_csv, ruta_archivo_xlsx):
    import csv
    from openpyxl import load_workbook

    # Leer los archivos csv y guardarlos en una lista
    data = []
    with open(ruta_archivo_csv, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    # Escribir la lista en el archivo xlsx
    libro = load_workbook(ruta_archivo_xlsx)
    writer = libro.active
    for fila in data:
        writer.append(fila)
    libro.save(ruta_archivo_xlsx)

if __name__ == "__main__":
    csv_xlsx("ejemplo.csv", "ejemplo.xlsx")