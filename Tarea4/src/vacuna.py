from sys import argv
from Crypto.Util import number
import os

#Función que descifra el archivo .enc
def xx(x):
    r = x.replace('.enc','')
    with open(r,'wb') as z:
        z.write((lambda x:bytes([x[i]^k_final[i%16] for i in range(len(x))]))(open(x,'rb').read()))
    os.remove(x)

#Abrimos el archivo .xyz y dividimos la cadena
file = open('.xyz','rb').read()
c = int.from_bytes(file[0:1],'big')
d = int.from_bytes(file[1:33],'big')
k = int.from_bytes(file[33:],'big')

#Obtenemos la llave
k = (k*number.inverse(d, 1<<c)) % (1<<c)

#convertimos a bytes la llave y eliminamos los ceros que se pusieron de relleno
k_bytes = k.to_bytes(32,'big')
cont = 0
for i in k_bytes:
    if i == 0:
       cont+=1
k_final = k_bytes[cont:]

#Aplicamos la función a cada archivo 
_,_,x = next(os.walk('./'))
x.remove(argv[0])
list(map(xx,x))
