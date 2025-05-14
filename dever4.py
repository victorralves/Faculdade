# 1) 
valor1 = 2
valor2 = 6
print("Quociente = ", valor1/valor2, "e o seu resto é =", valor1%valor2);

# 2)
num = 6
print(num - 1, num, num + 1)

# 3)
valorpago = 20
preçoproduto = 10
troco = valorpago - preçoproduto

print("O troco da compra do produto será ", troco)

# 4)
salario = 3500
reajuste = (salario * 0.35) + salario

print("O salário do trabalhador é 3500, mas com o reajuste de 35% seu salário será de ", reajuste)

# 5)
hora = 6
minutos = (hora * 60)/1
segundos = (minutos * 60)/1

print("Quantos minutos e segundos tem em ", hora, "horas?")
print(" Tem", minutos, "minutos")
print("e", segundos, "segundos")

# 6)
nota1 = 7
nota2 = 9
nota3 = 7
media = (nota1 + nota2 + nota3) /3

print("A média do aluno é ", media)

# 7)
litro_gasolina = 6.5
preço_a_pagar = 50
#coloca R$50 da comum chefe

print("O motorista irá conseguir abastecer",preço_a_pagar-litro_gasolina,"litros de gasolina")

# 8)
nome = "Victor"
ano = 2006

print("O nome da pessoa é", nome, "e essa pessoa nasceu", ano)

# 9)
salario = 3000
vendas = 1250
comissao = 0.01

print("Salário:", salario)
print("Vendas:", vendas)
print("Comissão:", comissao)
print('O salário final do funcionário vai ser de', (comissao * vendas) + salario, "reais")

# 10)
quilo = 12
peso_prato = 100
peso_quilo = peso_prato/1000

print("O valor a ser pago pela pessoa vai ser de", quilo*peso_quilo, "reais")

# 11)
eleitorestotal = 2652
votos_brancos = 750
votos_nulos = 102
votos_válidos = 1800

print("Percentual de cada grupo nas eleições:")
print("Eleitores:", str(100)+'%')
print("Votos brancos:", str(float((votos_brancos*100)/eleitorestotal))+"%")
print("Votos nulos", str(float((votos_nulos*100)/eleitorestotal))+"%")
print("Votos válidos", str(float((votos_válidos*100)/eleitorestotal))+"%")

# 12)
nome = "Victor"
peso = 65
altura = 1.80

print("O IMC(Índice de Massa Corporal) do(a)", nome, "será", peso/(altura*altura))

# 13)
x = 2
y = 6

print("Equação: z = x2+y2/(x-y)2")
print("O valor de z será:", (x**2 + y**2)/((x-y)**2))
