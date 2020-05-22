def __init__(self, key = 0):
    self.__key = key

def cipher(self, content, key):

    assert (isinstance(key,int) and isinstance(content,str))

    key = key or self.__key or 1

    while (key > 255):
        key -= 255

    # Esta lista sera retornada
    ans = []

    for ch in content:
        ans.append(chr(ord(ch) ^ key))

    return ans
    """
    Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
    XOR.
    Parámetro:
       message -- el mensaje a cifrar.
    """
    pass

def decipher(self,content,key):

    assert (isinstance(key,int) and isinstance(content,list))

    key = key or self.__key or 1

    while (key > 255):
        key -= 255

    ans = []

    for ch in content:
        ans.append(chr(ord(ch) ^ key))

    return ans
    """
    Descifra el mensaje recuperando el texto plano siempre y cuando haya
    sido cifrado con XOR.
    Parámetro:
       cryptotext -- el mensaje a descifrar.
    """
    pass
