# autor Henrique Kolle Portella
# operações : deposito, saque, extrato
# 3 saques por dia max valo = 500

saques = []
depositos = []
qtde_saques = 0


def saldo():
    soma = sum(depositos) - sum(saques)
    return soma


def verifica_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        print("O valor digitado não é um número.")


def extrato():
    print("###### Extrato da conta ######")

    for x in depositos:
        print(" R$ {:.2f} +".format(x))
    for x in saques:
        print(" R$ {:.2f} -".format(x))

    print("Saldo Atual : R$ {:.2f}".format(saldo()))
    print("###### FIM DO EXTRATO ######")


def sacar():
    valor = input("Quanto deseja sacar? :  ")
    if verifica_numero(valor):
        _valor = float(valor)
        if qtde_saques < 3:
            if _valor <= 500:
                if saldo() >= _valor:
                    saques.append(_valor)
                    print("O valor de R$ {:.2f} foi sacado da sua conta.".format(_valor, ))
                    return True

                else:
                    print("Saldo Insuficiente")
            else:
                print("Limite por saque R$ 500.00")
        else:
            print("Limite de 3 saques diarios")


def depositar():
    valor = input("Qual valor deseja depositar ? : ")

    if verifica_numero(valor):
        _valor = float(valor)
        depositos.append(_valor)
        print(depositos)


while True:
    saldo()
    op = input("""
        Digite a opção :
        [1] - Saque
        [2] - Deposito
        [3] - Extrato
        [4] - Sair
    """)

    if op.isdigit():
        _op = int(op)

        if _op in range(1, 5):

            if _op == 1:
                print("Sacar dinheiro:")
                if sacar():
                    qtde_saques += 1
                    print(qtde_saques)
            elif _op == 2:
                print("Depositar dinheiro:")
                depositar()
            elif _op == 3:
                extrato()
            elif _op == 4:
                break
            else:
                print("Opção invalida!")
        else:
            print("Digite valores entre 1 e 4")

    else:
        print("Digete um valor inteiro entre 1 e 4")
