var ='Ciao'
#var ='3'

try:
    var = float(var)
    print(var)
#except:
    #print('impossibile convertire "var" a numerico')
    #print('uso un valore di default 0.0 per "var" ')

except Exception as e:# mi porto l'exception dentro l'except
    print('impossibile convertire "var" a numerico')
    print('uso un valore di default 0.0 per "var" ')
    print('ho avuto questo errore:"{}"'.format(e))