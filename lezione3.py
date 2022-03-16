
def sum_list2 (list):
    sum=0
    for element in list:
        sum+= element
    return sum

from lezione2 import sum_list
def sum_csv(file_name):
    values = []
# Apro e leggo il file, linea per linea
    my_file = open(file_name, 'r')
    for line in my_file:
    # Faccio lo split di ogni riga sulla virgola
        elements = line.split(',')
    # Se NON sto processando l’intestazione...
        if elements[0] != 'Date':
    # Setto la data e il valore
            date = elements[0]
            value = elements[1]
# Aggiungo alla lista dei valori questo valore
            values.append(float(value))
    return sum_list(values)

print(sum_csv('shampoo_sales.csv'))