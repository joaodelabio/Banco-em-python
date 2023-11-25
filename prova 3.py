from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, registro, saldo, limite, cliente):
        self.registro = registro
        self.saldo = saldo
        self.limite = limite
        self.cliente = cliente
        self.historico = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f"{datetime.now()} - Depósito de R$ {valor:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(f"{datetime.now()} - Saque de R$ {valor:.2f}")
        else:
            print("Saldo insuficiente.")

def cadastro(contas):
    cliente = Cliente(input("Informe o nome do cliente: "), input("Informe o CPF do cliente: "))
    conta = Conta(int(input("Informe o registro da conta: ")), float(input("Informe o saldo da conta: ")), float(input("Informe o limite da conta: ")), cliente)
    contas.append(conta)

def informacoes(conta):
    print("Nome: ", conta.cliente.nome)
    print("Registro da conta: ", conta.registro)
    print("CPF: ", conta.cliente.cpf)
    print("Saldo: ", conta.saldo)
    print("Limite: ", conta.limite)
    print("Histórico:")
    for operacao in conta.historico:
        print(operacao)

contas = []

while True:
    print("===========================")
    print("1 - Cadastrar nova conta. ")
    print("2 - Depositar um valor.    ")
    print("3 - Sacar um valor.        ")
    print("4 - Informações da conta. ")
    print("---------------------------")
    print("5 - Sair.                 ")
    print("===========================")

    opcao = input("Insira a opção desejada: ")

    if opcao == "1":
        cadastro(contas)
        print("Cadastro realizado.")

    elif opcao == "2" and contas:
        while True:
            registro_conta = int(input("Informe o registro da conta: "))
            conta = next((c for c in contas if c.registro == registro_conta), None)
            if conta:
                valor = float(input("Informe o valor a ser depositado: "))
                conta.depositar(valor)
                break
            else:
                print("Conta inexistente.")

    elif opcao == "3":
        registro_conta = int(input("Informe o registro da conta: "))
        valor = float(input("Informe o valor a ser sacado: "))
        conta = next((c for c in contas if c.registro == registro_conta), None)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta inexistente.")

    elif opcao == "4":
        registro_conta = int(input("Informe o registro da conta. "))
        conta = next((c for c in contas if c.registro == registro_conta), None)
        if conta:
            informacoes(conta)
        else:
            print("Conta inexistente.")

    elif opcao == "5":
        print("Saindo.")
        break
