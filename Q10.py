horas=int(input("Quantas horas você trabalhou no mês:"))
salario=int(input("Quanto você ganha por hora:"))
salarioTotal=horas*salario
salarioBonus=salarioTotal*0.5+salarioTotal
if(horas>40):
    print(salarioBonus)
else:
    print(salarioTotal)


