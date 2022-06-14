import random
from random import randint

def lojaSapato(escolha, lista_Num_Sap):

    preco_sapato = (escolha + 50) // 2

    if escolha in lista_Num_Sap:
        print('Purchased size', escolha, 'shoe for $', preco_sapato)
        lista_Num_Sap.remove(escolha)
        return
    else:
        print('size ', escolha, ' no longer available, so no purchase.')
    
    return preco_sapato

def cliente():
    nome = input('Digite seu nome! \n')
    return nome

numSap = int(input('Número de Sapatos na Loja: '))
if numSap > 0 and numSap < 10**3:
    lista_Num_Sap = [random.randint(2, 20) for x in range(numSap)]
    print('Tamanhos Disponiveis: \n', lista_Num_Sap)

listaSoma = []

laco = int(input('\nGostaria de comprar?\n1 - Para comprar \n2 - Para sair\n'))
if laco == 1:
    escolha = int(input('Qual o tamanho de sapato desejado?\n'))
    Cliente = cliente(), lojaSapato(escolha, lista_Num_Sap)
    listaSoma[len(listaSoma):] = [lojaSapato(escolha, lista_Num_Sap)]
    print(listaSoma)
else:
    print('Fim do programa!')

