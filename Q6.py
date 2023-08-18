anodenascimento=int(input("Digite seu ano de nascimento:"))
anoatual=int(input("Digite o ano atual:"))
idade=(anoatual-anodenascimento)
if idade<16:
    print("Não poderá votar esse ano")
else:
    print("Poderá votar esse ano")

