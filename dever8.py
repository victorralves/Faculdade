# # EXERCICIO 1

# def exercicio1(x,y):
#     if(x>y):
#         print(f{x}'é maior que'{y})
#     elif(y>x):
#         print(f{y}'é maior que'{x})
#     elif(x == y):
#         print('Os números são iguais!')

# exercicio1(3,4)

# # EXERCICIO 2

# def exercicio2(n):
#     if(n/2 == 0):
#         print('O número é par!')
#     else:
#         print('O número é ímpar!')

# exercicio2(7)

# # EXERCICIO 3

# def exercicio3(n):
#     if(n < 0):
#         n = n * -1
#         print(n)
#     else:
#         print(n)

# exercicio3(-2)

# # EXERCICIO 4

# def exercicio4(ano):
#     if (ano % 4 == 0):
#         return True
#     else:
#         return False

# print(exercicio4(1984))

# # EXERCICIO 5

# def exercicio5(a,b,c):
#     if(a + b > c):
#         return True
#     else:
#         return False
    
# print(exercicio5(5,2,5))

# # EXERCICIO 6

# def exercicio6(n):
#     i = 0
#     while n > i:
#         if(n % 3 == 0) and (n % 5 == 0):
#             print("FizzBuzz")
#         elif(n % 3 == 0): 
#             print("Fizz")
#         elif (n % 5 == 0):
#             print("Buzz")
#         else:
#             print(n)
#         if(n == 0):
#             break
#         else:
#             n -= 1
#             continue
    

# exercicio6(15)

# # EXERCICIO 7

# list = [1,2,3,4]
# def exercicio7(n):
#     i = len(list)
#     while i >= n:
#         if i == n:
#             return i + 1
#         else:
#             i -= 1
#     if i < n:
#        return -1
        

# print(exercicio7(6))


# # EXERCICIO 8

# def exercicio8(n):
#     list = []
#     list2 = []
#     while True:
#         divisão = int(n/2)
#         resto = int(n % 2)
#         list.append(resto)
#         if divisão > 1:
#             n = divisão
#         if divisão == 1:
#             list.append(divisão)
#             for i in range(len(list)-1, -1, -1):
#                 list2.append(list[i])
#             return list2
        
# print(exercicio8(6))

# # EXERCICIO 9

# def exercicio9():
#     while True:
#         n = int(input('Escolha um número: '))
#         escolha = int(input('Agora escolha uma das opções a Seguir:\n' 
#         '1 - Imprimir a representação binária desse número\n' 
#         '2 - Imprimir a representação hexadecimal desse número\n' 
#         'Resposta: '))
        
#         if escolha == 1:
#             list = []
#             list2 = []
#             while True:
#                 divisão = int(n/2)
#                 resto = int(n % 2)
#                 list.append(resto)
#                 if divisão > 1:
#                     n = divisão
#                 if divisão == 1:
#                     list.append(divisão)
#                     for i in range(len(list)-1, -1, -1):
#                         list2.append(list[i])
#                     return list2
        
#         if escolha == 2:
#             list = []
#             list2 = []
#             while True:
#                 divisão = int(n/16)
#                 resto = int(n % 16)
#                 if (resto == 10):
#                     list.append('A')
#                 elif (resto == 11):
#                     list.append('B')
#                 elif (resto == 12):
#                     list.append('C')
#                 elif (resto == 13):
#                     list.append('D')
#                 elif (resto == 14):
#                     list.append('E')
#                 elif (resto == 15):
#                     list.append('F')
#                 else:
#                     list.append(str(resto))

#                 if divisão < 16:
#                     if (divisão == 10):
#                         list.append('A')
#                     elif (divisão == 11):
#                         list.append('B')
#                     elif (divisão == 12):
#                         list.append('C')
#                     elif (divisão == 13):
#                         list.append('D')
#                     elif (divisão == 14):
#                         list.append('E')
#                     elif (divisão == 15):
#                         list.append('F')
#                     else:
#                         list.append(str(divisão))

#                     for i in range(len(list)-1, -1, -1):
#                         list2.append(list[i])
#                     return list2
#                 else:
#                     n = divisão

#         if (escolha > 2) and (escolha == '') and (escolha < 1):
#             break
        
# print(exercicio9())

# # EXERCICIO 10

# def exercicio10():
#     import math
#     while True:
#         a = int(input('Entre com o 1º número: '))
#         if a == 0:
#             return "Não é uma equação do segundo grau."
#         else:
#             b = int(input('Entre com o 2º número: '))
#             c = int(input('Entre com o 3º número: '))
#         print('Equação:',f'{a}x^2+{b}x+{c}= 0')
#         delta = float((b*b) - (4*a*c))
#         if (delta < 0):
#             return "Não existem raízes reais."
#         elif (delta == 0):
#             x = float((-b + math.sqrt(delta))/(2*a))
#             return (f"Raiz única: x = {x}")
#         if(delta > 0):
#             x1 = float((-b + (math.sqrt(delta)))/(2*a))
#             x2 = float((-b - (math.sqrt(delta)))/(2*a))
#             return (f"Duas raízes reais: x1 = {x1}, x2 = {x2}")
        
# print(exercicio10())

# # EXERCICIO 11

# def exercicio11():
#     listaCandidatos = ['Maria','José','João']
#     listaVotos = [0,0,0]
#     count = 0
#     nome_novo = ""

#     print("Antes de começar a votação, você quer:")
#     print("1 - Colocar um nome na candidatura")
#     print("2 - Remover um nome da candidatura")
#     print("3 - Ir direto pra votação")

#     while True:
#         resposta_inicio = int(input("Responda aqui com uma das alternativas: "))
#         if (resposta_inicio == 1):
#             nome_novo = input("Adicione o nome do candidato: ")
#             listaCandidatos.append(listaCandidatos)
#         elif (resposta_inicio == 2):
#             remover_nome = input("Digite o nome do candidato a ser retirado da votação: ")
#             if(remover_nome in listaCandidatos):
#                 remover_nome.remove(listaCandidatos)
#         if(resposta_inicio == 3):
#             print("ELEIÇÕES 2025")
#             print("Escolha um candidato:")
#             while count < len(listaCandidatos):
#                 print(f"{count+1} - {listaCandidatos[count]}")
#                 count += 1 
#             processo = input('Escolha seu candidato: ')
#             if (processo.upper() == listaCandidatos[0].upper()) or (processo == 1):
#                 listaVotos[0] += 1
#             else:
#                 if (processo.upper() == listaCandidatos[1].upper()) or (processo == 2):
#                     listaVotos[1] += 1
#                 else:
#                     if (processo.upper() == listaCandidatos[2].upper()) or (processo == 3):
#                         listaVotos[2] += 1
#                     else:
#                         break

#     print("RESULTADOS DA VOTAÇÃO:")
#     print("1:Maria ->", listaVotos[0])
#     print("2:José ->", listaVotos[1])
#     print("3:João ->", listaVotos[2])
#     if listaCandidatos == nome_novo:
#         print(listaCandidatos)

#     if (listaVotos[0] > listaVotos[1] and listaVotos[0] > listaVotos[2]):
#         print('O vencedor é:', listaCandidatos[0],"com",listaVotos[0],"votos")
#     else:
#         if (listaVotos[1] > listaVotos[0] and listaVotos[1] > listaVotos[2]):
#             print('O vencedor é:', listaCandidatos[1],"com",listaVotos[1],"votos")
#         else:
#             if (listaVotos[2] > listaVotos[0] and listaVotos[2] > listaVotos[1]):
#                 print('O vencedor é:', listaCandidatos[2],"com",listaVotos[2],"votos")

# print(exercicio11())