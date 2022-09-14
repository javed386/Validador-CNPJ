import cnpj

while True:
    try:
        cnpj_usuario = input('digite seu cnpj: ')
        cnpj_usuario = cnpj.remover_caracteres(cnpj_usuario)
        if len(cnpj_usuario) < 14:
            print('digite um valor válido')
        else:   
            cnpj.verificacao(cnpj_usuario, cnpj.segundo_digito(cnpj_usuario), cnpj.primeiro_digito(cnpj_usuario))    
    except:
        print('digite um valor válido')
    
    
    

    