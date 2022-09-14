import re

def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]','',cnpj)
        
def encontrar_valor(cnpj, multiplicadores, valor_maximo):
    aumentador = 0
    multiplicacao_um = 0
    for v in cnpj:
        v = int(v)
        multiplicacao_um += v * multiplicadores[aumentador]
        aumentador += 1
        if aumentador == valor_maximo:
            break
    numero_um = 11 - (multiplicacao_um % 11)
    if numero_um > 9:
        numero_um = 0
    return(numero_um)

    

def primeiro_digito(cnpj):
    cnpj_copia = cnpj[:12]
    multiplicadores = [5,4,3,2,9,8,7,6,5,4,3,2]
    return encontrar_valor(cnpj_copia, multiplicadores, 12)
    
def segundo_digito(cnpj):
    cnpj_copia = cnpj[:13]
    multiplicadores = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    
    return encontrar_valor(cnpj_copia, multiplicadores, 13)
    
def verificacao(cnpj,segundo_digito, primeiro_digito):
    print(cnpj[-2])
    print(primeiro_digito)
    print(cnpj[-1])
    print(segundo_digito)
    if int(cnpj[-2]) == int(primeiro_digito) and int(cnpj[-1]) == int(segundo_digito):
        print('Seu CNPJ é válido')
    else:
        print('Seu CNPJ é inválido')
    

