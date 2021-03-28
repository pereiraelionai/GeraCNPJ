from random import randint

def CNPJ():
    def criaDigito(soma):
        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0
            return digito
        else:
            return digito


    def logica(fator, cnpj):
        soma_lista = []
        for teste in cnpj:
            soma = int(teste) * fator
            soma_lista.append(soma)
            if fator == 2:
                fator = 9
            else:
                fator -= 1
        return sum(soma_lista)


    cnpj = randint(00000000, 99999999)
    cnpj = str(cnpj) + '0001'

    soma_1 = logica(5, cnpj)
    digito_1 = criaDigito(soma_1)

    cnpj = cnpj + str(digito_1)

    soma_2 = logica(6, cnpj)
    digito_2 = criaDigito(soma_2)

    cnpj = cnpj + str(digito_2)

    return cnpj
