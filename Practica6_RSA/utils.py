def prime_relative(a, b):
    if(b == 0):
        return a == 1
    else:
        return prime_relative(b, a%b)
"""
contador = 0
for numero in range(0,n):
	if(prime_relative(numero,n)== 1):
		contador+=1
print("phi: ",contador)
"""


