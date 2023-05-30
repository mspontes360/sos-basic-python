from cliente import Cliente
from conta import Conta

# Cadastrar Cliente
novo_cadastro = Cliente('Marcelo', '9876899', 40)

print("NOVO CLIENTE")
print('Nome:',novo_cadastro.nome)
print('CPF:', novo_cadastro.cpf)
print('Idade:', novo_cadastro.idade)

print()
nova_conta = Conta("Marcelo", 0, 1000)
nova_conta.depositar(1500.00)

print("Saldo atual:",nova_conta.saldo)

nova_conta.sacar(730.89)

print("\nSaldo atual:",nova_conta.saldo)
