''' *-* -*- coding: utf-8 -*-
Calculadora do Predo - v1
Autora: Julia Nascimento
Funções: soma, subtração, multiplicação, divisão e exponenciação de números
'''


def main():
    print('\n------------------------------------')
    print('| Bem vindo à Calculadora do Pedro! |')
    print('------------------------------------')

    sair = False
    while sair is False:

        primeiro_numero, segundo_numero = define_numeros()

        if primeiro_numero is not False and segundo_numero is not False:
            escolhe_operacao(primeiro_numero, segundo_numero)

        sair = continua_operadora()

        if sair is False:
            print('\n\n-------------------------------------------------------------')

    print('\n\n----------------------------------')
    print('| Calculadora do Pedro encerrada |')
    print('----------------------------------\n')


def continua_operadora():
    sair = input('Deseja usar a calculadora novamente (s/n)? ')

    if sair == 's':
        return False
    elif sair == 'n':
        return True
    else:
        print('\n--------------------------------------------------------------------------------')
        print('| Você digitou uma opção errada, então vamos encerrar a calculadora! Tchaaauu! |')
        print('--------------------------------------------------------------------------------\n')

        return 'encerrar'


def define_numeros():
    print('\n\nPredo, digita aqui os números que você quer fazer conta:\n')

    primeiro_numero = input('\t--> Primeiro número: ')
    segundo_numero = input('\t--> Segundo número: ')

    try:
        primeiro_numero = int(primeiro_numero)
        segundo_numero = int(segundo_numero)

        return (primeiro_numero, segundo_numero)

    except Exception:
        print('\n\n\tAlgum número seu ta errado ai, parça!\n\n')

        return (False, False)


def escolhe_operacao(primeiro_numero, segundo_numero):
    print('\n\nEscolha a operação que você deseja fazer, Predin:\n')
    print('\t--> Digite 1 para SOMA')
    print('\t--> Digite 2 para SUBTRAÇÃO')
    print('\t--> Digite 3 para MULTIPLICAÇÃO')
    print('\t--> Digite 4 para DIVISÃO')
    print('\t--> Digite 5 para EXPONENCIAÇÃO\n')

    opcao_escolhida = input('\n\t--> Digite aqui a opção desejada: ')

    if opcao_escolhida == '1':
        soma(primeiro_numero, segundo_numero)
    elif opcao_escolhida == '2':
        subtrai(primeiro_numero, segundo_numero)
    elif opcao_escolhida == '3':
        multiplica(primeiro_numero, segundo_numero)
    elif opcao_escolhida == '4':
        divide(primeiro_numero, segundo_numero)
    elif opcao_escolhida == '5':
        exponencia(primeiro_numero, segundo_numero)
    else:
        print('\n\n\tVocê digitou uma opção inválida, mané!\n\n')


def soma(primeiro_numero, segundo_numero):
    print('\n\n\t--> Sua opção escolhida foi SOMA\n')

    resultado = primeiro_numero + segundo_numero

    mostra_resultado('+', primeiro_numero, segundo_numero, resultado)


def subtrai(primeiro_numero, segundo_numero):
    print('\n\n\t--> Sua opção escolhida foi SUBTRAÇÃO\n')

    resultado = primeiro_numero - segundo_numero

    mostra_resultado('-', primeiro_numero, segundo_numero, resultado)


def multiplica(primeiro_numero, segundo_numero):
    print('\n\n\t--> Sua opção escolhida foi MULTIPLICAÇÃO\n')

    resultado = primeiro_numero * segundo_numero

    mostra_resultado('*', primeiro_numero, segundo_numero, resultado)


def divide(primeiro_numero, segundo_numero):
    print('\n\n\t--> Sua opção escolhida foi DIVISÃO\n')

    resultado = primeiro_numero / segundo_numero

    mostra_resultado('/', primeiro_numero, segundo_numero, resultado)


def exponencia(primeiro_numero, segundo_numero):
    print('\n\n\t--> Sua opção escolhida foi EXPONENCIAÇÃO\n')

    resultado = primeiro_numero ** segundo_numero

    mostra_resultado('**', primeiro_numero, segundo_numero, resultado)


def mostra_resultado(operacao, primeiro_numero, segundo_numero, resultado):
    print('\n---------------------------')
    print('| Resultado --> {} {} {} = {} |'.format(primeiro_numero, operacao, segundo_numero, resultado))
    print('---------------------------\n\n')


if __name__ == '__main__':
    main()
else:
    raise 'Deu ruim'
