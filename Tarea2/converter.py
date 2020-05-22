#-*- coding: utf-8 -*-
import base64

#	Leemos el archivo
in_file = open("cinta_aleatoria.txt", "r") # opening for [r]eading as [b]inary
data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

cadena = ''
for x in data:
	cadena += x

message_bytes = base64.b64decode(cadena)
llave_bytes = bytearray(message_bytes)
lon = len(llave_bytes)
print ("Longitud de la llave: ",lon)
################################## imagen.png
#	Leemos el archivo
in_file = open("imagen.png", "rb") 
data = in_file.read() 
in_file.close()

data_bytes = bytearray(data)
lon2 = len(data_bytes)
print ("Longitud de m: ",lon2)
#######################Aqui hacemos el xor byte a byte
i = 0
while i < len(data_bytes):
	data_bytes[i] = (data_bytes[i]^llave_bytes[i])
	i += 1

# Imprimimos los primeros 10 bytes
for x in range(10):
	print(data_bytes[x])


#	Escribimos el arreglo de bytes en un archivo de salida
out_file = open("imagenCifrada.png", "wb") # open for [w]riting as [b]inary
out_file.write(data_bytes)
out_file.close()
