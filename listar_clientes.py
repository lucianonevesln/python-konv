# bibliotecas necessarias para que essa parte do programa funcione
import csv


# funcao que lista todos os clientes cadastrados
def listar_clientes():
    with open('banco_de_dados_clientes.csv', mode='r') as clientes_cadastrados:
        leitura = csv.reader(clientes_cadastrados, delimiter=',')
        contador = 0
        for cliente in leitura:
            if contador == 0:
                print('\n---------- Lista de Clientes ----------\n')
                print(f'Cabecalho: {" ".join(cliente)}')
                contador += 1
            else:
                print(f'Cliente: {" ".join(cliente)}')
                contador += 1