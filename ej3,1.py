def verificar_num(num):
    if num == 0:
        return "Cero"
    
    if num % 2 == 0:
        if num > 0:
            return "Par positivo"
        else:
            return "Par negativo"
    else:
        if num > 0:
            return "Impar positivo"
        else:
            return "Impar negativo"
