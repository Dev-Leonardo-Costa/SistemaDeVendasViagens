POLTRONA_VAZIA = ''
MEIA = 'MEIA'
INTEIRA = 'INTEIRA'
VENDER_PASSAGEM = 1
VER_POLTRONAS = 2
FINALIZAR_VENDAS = 3
SAIR = 4
OPCAO_JANELA = 'J'
OPCAO_CORREDOR = 'C'
OPCAO_DIREITA = 'D'
OPCAO_ESQUERDA = 'E'
NUMERO_PASSAGENS_DISPONIVEIS = 16
NUMERO_ASSENTOS_POR_FILA = NUMERO_PASSAGENS_DISPONIVEIS // 4
VALOR_PASSAGEM = 100

def menu_passagem():
    print('+-------------------------------------+')
    print('| CONTROL-VIAGENS: VENDA DE PASSAGENS |')
    print('+-------------------------------------+')
    print('[ 1 ] Vender passagem')
    print('[ 2 ] Ver poltronas')
    print('[ 3 ] Finalizar Vendas')
    print('[ 4 ] Sair')
    print('+-------------------------------------+')
    return int(input('Informe sua opção: '))

def poltrona_ja_esta_vendida(poltrona):
    return True if poltrona == 'X' else False

def todas_poltronas_estao_vendidas(poltronas):
    return POLTRONA_VAZIA not in poltronas

def busca_posicoes_livres(poltronas):
    lista_posicoes_livres = []
    for indice, poltrona in enumerate(poltronas, start=1):
        if not poltrona_ja_esta_vendida(poltrona):
            lista_posicoes_livres.append(indice)
    return lista_posicoes_livres

def exibe_posicoes_livres(poltronas_livres):
    posicoes_livres = ' - '.join(str(numero_poltrona) for numero_poltrona in poltronas_livres)
    print(posicoes_livres)

def opcao_vender_passagem(pol_janela_direita, pol_corredor_direita, pol_janela_esquerda, pol_corredor_esquerda, total_vendido):
    while total_vendido <= NUMERO_PASSAGENS_DISPONIVEIS:
        print('Vender passagem')
        idade = obter_idade()
        paga_meia = idade < 5 or idade > 65
        if paga_meia:
            quantidade_vendidos[MEIA] += 1
        else:
            quantidade_vendidos[INTEIRA] += 1

        print('Escolha sua poltrona: ')
        opcao_ver_poltronas()

        opcao_janela_ou_corredor = input('Digite opção Janela [ J ] ou Corredor [ C ]?: ').upper()
        if opcao_janela_ou_corredor == OPCAO_JANELA:

            opcao_direira_ou_esquerda = input('Janela direita [ D ] ou esquerda [ E ]: ').upper()
            if opcao_direira_ou_esquerda == OPCAO_DIREITA:
                vender_uma_passagem(pol_janela_direita, total_vendido)
            elif opcao_direira_ou_esquerda == OPCAO_ESQUERDA:
                vender_uma_passagem(pol_janela_esquerda, total_vendido)
            else:
                print('Opção inválida!')

        elif opcao_janela_ou_corredor == OPCAO_CORREDOR:

            opcao_direira_ou_esquerda = input('Corredor direita [ D ] ou esquerda [ E ]: ').upper()
            if opcao_direira_ou_esquerda == OPCAO_DIREITA:
                vender_uma_passagem(pol_corredor_direita, total_vendido)
            elif opcao_direira_ou_esquerda == OPCAO_ESQUERDA:
                vender_uma_passagem(pol_corredor_esquerda, total_vendido)
            else:
                print('Opção inválida!')

        else:
            print('Opção inválida!')

        if total_vendido == 12:
            print('\n***** Todas as passagens foram vendidas! *****\n')
            break

        comprar_mais = input('Deseja vender outra passagem? [S/N]: ').upper()
        if comprar_mais == 'S':
            continue
        else:
            break

def obter_idade():
    idade_valida = False
    idade = 0
    while not idade_valida:
        idade = int(input('Qual a idade do passageiro?: '))
        if 0 <= idade <= 120:
            idade_valida = True
        else:
            print('Idade inválida, digite novamente!')
    return idade

def vender_uma_passagem(poltronas, total_passagens):
    if todas_poltronas_estao_vendidas(poltronas):
        print('Todos os lugares estão ocupados!')

    print('Posições livres:')
    lista_posicoes_livres = busca_posicoes_livres(poltronas)
    exibe_posicoes_livres(lista_posicoes_livres)

    finalizou_compra = False
    while not finalizou_compra:
        polcompra = int(input('\nDigite o número da poltrona desejada: '))
        if polcompra in lista_posicoes_livres:
            poltronas[polcompra - 1] = 'X'
            total_passagens += 1
            finalizou_compra = True
        else:
            print('Opção invalida! Escolha uma poltrona válida!')
            finalizou_compra = False

    print('\nPassagem vendida com sucesso!\n')

def opcao_ver_poltronas():
    print('Lugares vagos [ ] - Lugares ocupados [X]\n')
    print('   /__ _ ', end='')
    for poltrona in poltronas_janela_direita:
        print('[{}]'.format(poltrona if poltrona else ' '), end='')
    print(' \\  : Janela Direita')

    print('  |   |  ', end='')
    for poltrona in poltronas_corredor_direita:
        print('[{}]'.format(poltrona if poltrona else ' '), end='')
    print('  | : Corredor Direita')

    print('  | __|_ ', end='')
    for poltrona in poltronas_corredor_esquerda:
        print('[{}]'.format(poltrona if poltrona else ' '), end='')
    print('  | : Corredor Esquerda')

    print('   \\     ', end='')
    for poltrona in poltronas_janela_esquerda:
        print('[{}]'.format(poltrona if poltrona else ' '), end='')
    print(' /  : Janela Esquerda')

def opcao_finalizar_vendas():
    valor_meia = (quantidade_vendidos[MEIA] * VALOR_PASSAGEM) / 2
    valor_inteira = quantidade_vendidos[INTEIRA] * VALOR_PASSAGEM
    valor_total = valor_meia + valor_inteira

    if total_vendido >= NUMERO_PASSAGENS_DISPONIVEIS / 2:
        print('O numero minimo de passagens foi atingido! A viagem foi confirmada.')
    else:
        print('O numero minimo de passagens não foi atingido. A viagem esta cancelada!')

    print('O valor total vendido em passagens foi de R$ {}!'.format(valor_total))

if __name__ == '__main__':
    # Declaração de Variáveis
    poltronas_janela_direita = [POLTRONA_VAZIA] * NUMERO_ASSENTOS_POR_FILA
    poltronas_corredor_direita = [POLTRONA_VAZIA] * NUMERO_ASSENTOS_POR_FILA
    poltronas_janela_esquerda = [POLTRONA_VAZIA] * NUMERO_ASSENTOS_POR_FILA
    poltronas_corredor_esquerda = [POLTRONA_VAZIA] * NUMERO_ASSENTOS_POR_FILA
    quantidade_vendidos = {MEIA: 0, INTEIRA: 0}
    total_vendido = 0

    while True:
        opcao_menu = menu_passagem()

        if opcao_menu == VENDER_PASSAGEM:
            opcao_vender_passagem(
                poltronas_janela_direita,
                poltronas_corredor_direita,
                poltronas_janela_esquerda,
                poltronas_corredor_esquerda,
                total_vendido
            )

        elif opcao_menu == VER_POLTRONAS:
            print('Ver poltronas\n')
            opcao_ver_poltronas()

        elif opcao_menu == FINALIZAR_VENDAS:
            opcao_finalizar_vendas()
            break

        elif opcao_menu == SAIR:
            break