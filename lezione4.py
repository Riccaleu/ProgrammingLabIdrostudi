class CsvFile():
    def __init__(self,name):
         self.name=name
    def get_data(self):
        values=[]
        my_file = open(self.name, 'r')
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            if elements[0] != 'Date':
                date = elements[0]
                value = elements[1]
                values.append([date,value])
        return values
file=CsvFile('shampoo_sales.csv')
print(file.get_data())