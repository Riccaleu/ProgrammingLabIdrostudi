class CsvFile():
    def __init__(self,name):
        self.name=name
        #try:
         #    myfile=open(self.name)
         #    myfile.readline()
         #except:
         #    print('Non trovo il cazzo di file....')
    def get_data(self):
        leggibile=True

        try:
            my_file = open(self.name, 'r')
        except:
            print('ERRORE!!: non leggo un cazzo')
            leggibile=False
        else:  
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
file=CsvFile('shampoo_sales_2.csv')
print(file.get_data())