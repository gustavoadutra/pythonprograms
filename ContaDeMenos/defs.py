def menu():
    print('=='*20)
    print('(1)Ver o saldo\n(2)Depositar\n(3)Retirar')
    print('=='*20)
    

def inicio(local_arquivo):
    menu()
    escolha = int(input('Escolha:'))
    arquivo, arquivo_lista = retirar_valor(local_arquivo)
    if escolha == 1:
        olhar_arquivo(arquivo)
    elif escolha == 2:
        somar_arquivo(arquivo, arquivo_lista, local_arquivo)
    elif escolha == 3:
        diminuir_arquivo(arquivo, arquivo_lista, local_arquivo)


def retirar_valor(local_arquivo):
    arquivo = open(local_arquivo, 'r')
    arquivo_aberto_lista = arquivo.readlines()
    arquivo_final = float((arquivo_aberto_lista[-1]).strip('\n'))
    return arquivo_final, arquivo_aberto_lista


def olhar_arquivo(arquivo = 0):
    print(f'R${arquivo:.2f}')


def somar_arquivo(arquivo, arquivo_aberto_lista, local_arquivo):
    valor_somar = float(str(input('Valor a somar:R$')).replace(',', '.'))
    valor_final = str(arquivo + valor_somar)
    arquivo_aberto_lista.append(valor_final + '\n')
    arquivo_aberto_editar = open(local_arquivo, 'w')
    arquivo_aberto_editar.writelines(arquivo_aberto_lista)
    arquivo_aberto_editar.close()
    print(arquivo_aberto_lista)


def diminuir_arquivo(arquivo, arquivo_aberto_lista, local_arquivo):
    valor_diminuir = float(str(input('Valor a diminuir:R$')).replace(',', '.'))
    valor_final = str(arquivo - valor_diminuir)
    arquivo_aberto_lista.append(valor_final + '\n')
    arquivo_aberto_editar = open(local_arquivo, 'w')
    arquivo_aberto_editar.writelines(arquivo_aberto_lista)
    arquivo_aberto_editar.close()
    print(arquivo_aberto_lista)


