# EXERCICIO 1

cliente = ['Duda', 'Samuel', 'Victor']

while True:
    print('----MENU----')
    print('1 - Cadastrar')
    print('2 - Alterar')
    print('3 - Excluir')
    print('4 - Listar')
    print('5 -Sair')
    menu = input('Insira o número da opção desejada: ')
    if (menu == ''):
        print("Essa opção não está nas opções presentes no sistema!")
        continue
    else:
        menu = int(menu)
        if(menu > 5) or (menu == 0):
            print("Essa opção não está nas opções presentes no sistema!")
            continue
    break    

match menu:
    case 1:
        print('Você escolheu cadastrar um cliente!')
        novo_cliente = input("Entre com o nome do novo cliente: ").title()
        cliente.append(novo_cliente)
        
    case 2:
        print('Você escolheu alterar um nome na lista de clientes!')
        print('Essa é a lista de clientes ->', cliente)
        while True:
            alteraçao = input('Entre com o nome do cliente que deseja alterar: ').title()
            if (alteraçao in cliente):
                cliente.remove(alteraçao)
                nova_alteração = input('Entre com o novo nome: ').title()
                cliente.append(nova_alteração)
                print(cliente)
                break
            else:
                print('Escolha não contida nas opções!')
                continue

    case 3:
        print('Você escolheu excluir um cliente da lista!')
        while True:
            print('Essa é a lista de clientes ->', cliente)
            nome_excluido = input('Entre com o nome do cliente a ser removido: ').title()
            if(nome_excluido in cliente):
                cliente.remove(nome_excluido)
                print('A lista ficou assim ->', cliente)
                break
            else:
                print('Escolha não contida nas opções!')
                continue
    
    case 4:
        print('Você escolheu listar os cliente da lista!')
        print('Essa é a lista de clientes ->', cliente)
    
    case 5:
        print('Você escolheu sair do sistema!')
        print('Até outra hora!')

# EXERCICIO 2

cadastro_pessoas = []
quest = [0,0,0,0,0]

cadastro = input('Para começar, cadastre a pessoa que irá responder o questionário: ')
cadastro_pessoas.append(cadastro)

print('Vamos começar o questionário sobre o crime') 
print('cometido na noite de 30/02/2025!')
print('Responda as perguntas com Sim ou Não!')

count = 0
q1 = (input('1º pergunta: Telefonou para a vítima?').lower())
if(q1 == 'sim'):
    count += 1
    quest[0] += 1

q2 = input('2º pergunta: Esteve no local do crime?').lower()
if(q2 == 'sim'):
    count += 1
    quest[1] += 1

q3 = input('3º pergunta: Mora perto da vítima?').lower()
if(q3 == 'sim'):
    count += 1
    quest[2] += 1

q4 = input('4º pergunta: Devia para a vítima?').lower()
if(q4 == 'sim'):
    count += 1
    quest[3] += 1

q5 = input('5º pergunta: Já trabalhou com a vítima?').lower()
if(q5 == 'sim'):
    count += 1
    quest[4] += 1

print('Resultado do questionário:')
print(quest)
if(count == 0):
    print('O(a)', cadastro,'foi considerado como "Inocente"')

if (count == 2):
    print('O(a)', cadastro,'foi considerado como "Suspeita"')
elif (count == 3) or (count == 4):
    print('O(a)', cadastro,'foi considerado como "Cúmplice"')
elif (count == 5):
    print('O(a)', cadastro,'foi considerado como "Assassino"')


# EXERCICIO 3

print('QUALIFICAÇÕES PARA APOSENTADORIA')
funcionarios = []
idade = []
tempo_trabalho = []
func_qualificados = []
func_naoqualificados = []
mediat_qualificados = []

while True:
    ID = input('Entre com o ID do funcionário: ')
    if(ID == ''):
        break
    funcionarios.append(ID)
    ano_nascimento = int(input('Entre com o ano do nascimento do funcionário: '))
    if(ano_nascimento == ''):
        break
    ano_ingresso = int(input('Entre com o ano de ingresso na companha: '))
    if(ano_ingresso == ''):
        break

    ano_aposentadoria = 2025 - ano_nascimento
    idade.append(ano_aposentadoria)
    anos_trabalhados = 2025 - ano_ingresso
    tempo_trabalho.append(anos_trabalhados)
    if(ano_aposentadoria >= 65) or (anos_trabalhados >= 30):
        func_qualificados.append(ID)
        mediat_qualificados.append(ano_ingresso)
    else:
        func_naoqualificados.append(ID)
    
    if(ano_aposentadoria >= 60) and (anos_trabalhados >= 25):
        func_qualificados.append(ID)
        mediat_qualificados.append(ano_ingresso)

i = 0
while i < len(funcionarios):
    print('NOME:',funcionarios[i])
    print('IDADE:', idade[i])
    print('TEMPO DE TRABALHO:', tempo_trabalho[i])
    i += 1
    continue
print('Os funcionários que podem requerer aposentadoria são: ',func_qualificados)  
media = int(sum(mediat_qualificados)/len(mediat_qualificados))
print('A média de trabalho dos funcionários é: ',media,'anos')

# EXERCICIO 4
# NAO FIZ



    













    

        

