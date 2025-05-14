# Exercicio 1
num1 = int(input("Escolha o 1º número: "))
num2 = int(input("Escolha o 2º número: "))

if(num1 > num2):
    print(num1)
else:
    print(num2)

# Exercicio 2
num = int(input("Entre com um número: "))

if(num > 0):
    print("Seu número é maior do que 0!")
else:
    if(num < 0):
        print("Seu número é menor do que 0!")
    else:
        if(num == 0):
            print("Seu número é igual a 0!")

# Execicio 3
num = int(input("Entre com um número: "))

if(num % 2 == 0):
    print("O número escolhido é par!")
else:
    print("O número escolhido é impar!")

# Exercicio 4
num = int(input("Entre com um número: "))

if(num > 80):
    print("Seu número é maior que 80!")
else:
    if(num == 40):
        print("Seu número é igual a 40!")
    else:
        if(num < 25):
            print("Seu número é menor que 25!")

# Exercicio 5
print("You want enter in this system?, so WHAT's THE PASSWORD?")
password = str(input("Enter Password: "))

if(password == "batata frita"):
    print("Acesso Liberado!")
else:
    print("Você não tem acesso ao sistema!")

# Exercicio 6
num1 = int(input("Entre com o 1º número: "))
num2 = int(input("Entre com o 2º número: "))
num3 = int(input("Entre com o 3º número: "))

if(num1 < num2 < num3):
    print(num1, num2, num3)
else:
    if(num1 < num3 < num2):
        print(num1, num3, num2)
    else:
        if(num2 < num1 < num3):
            print(num2, num1, num3)
        else:
            if(num2 < num3 < num1):
                print(num2, num3, num1)
            else:
                if(num3 < num1 < num2):
                        print(num3, num1, num2)
                else:
                        if(num3 < num2 < num1):
                                print(num3, num2, num1)

# Exercicio 7
salariominimo = float(1509.50)
salario = float(input("Qual é o salário do funcionário?" ))

if(salario < 3*salariominimo):
    print("O ajuste salarial do funcionário será de 50%!")
    print("O salário que era", "R$",salario, "foi reajustado para", "R$",(salario*0.5)+salario)
else:
    if(salario < 10*salariominimo):
        print("O ajuste salarial do funcionário será de 20%!")
        print("O salário que era", "R$",salario, "foi reajustado para", "R$",(salario*0.2)+salario)
    else:
        if(salario > 10*salariominimo) and (salario < 20*salariominimo):
            print("O ajuste salarial do funcionário será de 15%!")
            print("O salário que era", "R$",salario, "foi reajustado para", "R$",(salario*0.15)+salario)
        else:
            if(salario > 20*salariominimo):
                print("O ajuste salarial do funcionário será de 10%!")
                print("O salário que era", "R$",salario, "foi reajustado para", "R$",(salario*0.1)+salario)

# Exercicio 8

menor20 = 0.45
maior20 = 0.3
lucro = 0
produto = float(input("Entre com o valor do produto: "))

if(produto <= 20):
    lucro = ((produto*menor20)+produto)
    print("O valor do produto era de R$",produto)
    print("O valor do produto passa a ser R$",lucro)
    print("O lucro que o vendedor terá será de R$",lucro - produto)

if(produto > 20):
    lucro = ((produto*maior20)+produto)
    print("O valor do produto era de R$",produto)
    print("O valor do produto passa a ser R$",lucro)
    print("O lucro que o vendedor terá será de R$",lucro - produto)

# Exercicio 9

valor = float(input("Entre com o valor do veículo: "))
ano = int(input("Entre com o ano do veículo: "))

if(ano <= 2000):
    desconto = valor * 0.12
    valorfinal = valor - desconto
else:
    desconto = valor * 0.07
    valorfinal = valor - desconto

print("O cliente terá um desconto de R$",desconto)
print("E o valor final a ser pago será de R$", valorfinal)

# Exercicio 10

num = float(input("Entre com um número: "))

if(num >= 100) and (num <= 200):
    print("Seu número está entre o intervalo desejado!!")
else:
    print("rapaz..., seu número não está no sistema!")

# Exercicio 11

nome = input("Digite o nome do jogador: ")
salarioatual = float(input("Digite o salário atual do jogador R$: "))

if(salarioatual <= 5000):
    reajuste = salarioatual * 0.20
    salarioreajustado = salarioatual + reajuste
else:
    if(salarioatual <= 15000):
        reajuste = salarioatual * 0.10
        salarioreajustado = salarioatual + reajuste
    else:
        if(salarioatual >= 15000):
        reajuste = 0
        salarioreajustado = salarioatual + reajuste

print("Nome: ", nome)
print("Salário Atual: R$",salarioatual)
print("Salário Reajustado: R$",salarioreajustado)

# Exercicio 12

nome = input("Qual o nome do hóspede? " )
apt = str(input("Qual apartamento o hóspede ficou? " ))
diaria = float(input("Quantas diárias o hóspede ficou? " ))
consumo = float(input("Qual o valor gasto de consumo interno? " ))

match apt:
    case "A":
        valordiaria = 150
        totaldiaria = valordiaria*diaria
    case "B":
        valordiaria = 100
        totaldiaria = valordiaria*diaria
    case "C":
        valordiaria = 75
        totaldiaria = valordiaria*diaria
    case "D":
        valordiaria = 50
        totaldiaria = valordiaria*diaria

subtotal = totaldiaria + consumo
taxaserviço = subtotal * 0.1
total = subtotal + taxaserviço

print("O nome do hóspede é:", nome)
print("O tipo do apartamento do hóspede foi:", apt)
print("O hóspede ficou:", diaria,"dias")
print("A conta das diárias ficou: R$",totaldiaria)
print("O total do consumo interno foi de R$",consumo)
print("O subtotal ficou: R$",subtotal)
print("Lembrando que nós temos uma taxa de serviço de 10%!")
print("Então o total a ser pago é: R$", total)





















