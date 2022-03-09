lista=[1,4,67,59]
a=sum(lista)
print('Sum of list: {}'.format(a))

def somma (list):
    Sum=0
    #for i in range(len(list)):
    #    Sum = list[i]+Sum
    for element in list:
        Sum+= element
    return Sum
risult = somma(lista)
print('Sum of list: {}'.format(risult))        