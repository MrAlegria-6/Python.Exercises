def segundo_mas_grande(lista):
    lista.sort()
    return lista[-2]  

#Aqui podría agregar una verificacion por si solo hay un numero en la lista entonces pero ni modo xd
print(segundo_mas_grande([23, 54, 12, 87, 88, 45, 98, 76]))  # 87
