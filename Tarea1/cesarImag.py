#-*- coding: utf-8 -*-
m = 256	# Modulo del longitud del alfabeto

#dec= c-b (mod m)

llave = []
#	Buscamos la llave b tal que restada al cifrado, nos da el resultado
#	D(E(x)) = (E(x) - b) mod m
for b in xrange(0, m):
	# Suponemos que es el formato jpeg y empieza en 64 hexadecimal,
	# que en entero seria el 100 que usaremos abajo y ff = 255 que es como empieza un jpeg. 
	if (100- b) % m ==  255:
		llave.append([b])

print "LLAVE (b)"
print(llave)



#	Leemos el archivo
in_file = open("imagen.enc", "rb") # opening for [r]eading as [b]inary
data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

#	Guardamos los datos en un arreglo de bytes mutables
data_bytes = bytearray(data)

#	Tomando a 101 = b la llave que cumplió la igualdad 
i = 0
while i < len(data_bytes):
	data_bytes[i] = (data_bytes[i] - 101) % m
	i += 1

#	Escribimos el arreglo de bytes en un archivo de salida
out_file = open("imagenNew", "wb") # open for [w]riting as [b]inary
out_file.write(data_bytes)
out_file.close()

