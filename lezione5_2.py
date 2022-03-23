# class CsvFile():
#     def __init__(self,name):
#         self.name=name
#         #try:
#          #    myfile=open(self.name)
#          #    myfile.readline()
#          #except:
#          #    print('Non trovo il cazzo di file....')
#     def get_data(self):
#         leggibile=True

#         try:
#             my_file = open(self.name, 'r')
#         except:
#             print('ERRORE!!: non leggo un cazzo')
#             leggibile=False
#         else:  
#             values=[]
#             my_file = open(self.name, 'r')
#             for line in my_file:
#                 elements = line.split(',')
#                 elements[-1] = elements[-1].strip()
#                 if elements[0] != 'Date':
#                     date = elements[0]
#                     value = elements[1]
#                     values.append([date,value])
#             return values

from lezione4 import CsvFile

class NumericalCsv(CsvFile):
    def get_data(self):
        string=super().get_data()
        number = []
        for row in string:
            number_row=[]
            for i,element in enumerate(row):
                if i==0:
                    number_row.append(element)
                else:
                    try:
                        number_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
            if len(number_row)==len(row):
                number.append(number_row)
        return number                
                

# file=CsvFile('shampoo_sales.csv')
# print(file.get_data())
# #file=NumericalCsv('shampoo_sales.csv')
#print(file.get_data())

        
file=NumericalCsv('shampooo_sales2.csv')
print(file.get_data())


        