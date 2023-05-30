convidados = []

escolha = "s"

while escolha == "s":
    escolha = input("Você gostaria de convidar alguém? (S/N): ").lower()
    if escolha == "s":
        convite = convidados.append(input('Quem você gostaria de convidar? '))
    else:
        print("Ok, até a próxima!\n")

if len(convidados) > 0:
    print("Seus convidados são:")
    for convidado in convidados:
        print(convidado)
