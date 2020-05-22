#-*- coding: utf-8 -*-

m = 256	# Modulo del longitud del alfabeto

coprimos = []

# define la función del maximo comun divisor
def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a
#Se saca el modulo inverso de a y m
def modInverso(a, m):
    	a = a % m
    	for x in range (1, m):
    		if (a*x) % m == 1:
    			return x
    	return 1

#	Encontramos todos los numeros coprimos con 'm'
for posible_coprimo in xrange(0, m):
	if mcd(posible_coprimo, m) == 1:	#	Calculamos el Máximo Común Divisor
		coprimos.append(posible_coprimo)



llaves = []
#	Dados los coprimos de 'm', buscamos un número 'b' 
# 	que satisfaga la ecuación
#	E(x) = (ax + b) mod m
for a in coprimos:
	for b in xrange(0, m):
		#	En particular queremos que satisfaga estas dos igualdades
		#	a*ff + b = f2 y a*fb + b = be
		if (a*255 + b) % m == 242 and (a*251 + b) % m == 190:	
			llaves.append([a, b])

print "LLAVES (a, b)"
print(llaves)


llaves_ainversa = []
#	Obtenemos el inverso multiplicativo modular de 'a' para cada llave
for llave in llaves:
	a_inversa = modInverso(llave[0], m)
	llaves_ainversa.append([a_inversa, llave[1]])
	
print "LLAVES (a^-1, b)"
print(llaves_ainversa)




#	Leemos el archivo
in_file = open("audio.enc", "rb") # opening for [r]eading as [b]inary
data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

 #	Guardamos los datos en un arreglo de bytes mutables
data_bytes = bytearray(data)

#	Desencriptamos el arreglo de bytes
# 	con la función 
#	D(x) = a^(-1)(x - b) mod m

i = 0
while i < len(data_bytes):
	data_bytes[i] = (197*(data_bytes[i] - 255)) % m
	i += 1

#	Escribimos el arreglo de bytes en un archivo de salida
out_file = open("audio_dec", "wb") # open for [w]riting as [b]inary
out_file.write(data_bytes)
out_file.close()
