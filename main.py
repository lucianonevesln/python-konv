# chamadas de funcoes necessarias para que o programa principal funcione
from cadastrar_cliente import cadastrar_cliente
from listar_clientes import listar_clientes
from depositar import depositar
from sacar import sacar
from consultar_extrato_saldo import consultar_extrato_saldo


# funcao que apresenta opcoes para usuario interagir com o sistema
def menu():
    print('\n---------- Menu de Opcoes ----------\n')
    print('Digite 1 para: Cadastrar um novo cliente')
    print('Digite 2 para: Listar Clientes Existentes')
    print('Digite 3 para: Realizar Depósito')
    print('Digite 4 para: Realizar Saque')
    print('Digite 5 para: Consultar Extrato/Saldo')
    print('Digite 6 para: Sair do Sistema')
    print('\n---------- Fim Menu ----------\n')
    opcao = int(input("Digite a opcao escolhida: "))
    if opcao == 1:
        cadastrar_cliente()
        menu()
    elif opcao == 2:
        listar_clientes()
        menu()
    elif opcao == 3:
        depositar()
        menu()
    elif opcao == 4:
        sacar()
        menu()
    elif opcao == 5:
        consultar_extrato_saldo()
        menu()
    elif opcao == 6:
        print('\n---------- Saindo do sistema... ----------\n')
    else:
        print('\n---------- Escolha uma opcao valida. ----------\n')
        menu()


# chamada para execucao do programa principal
menu()