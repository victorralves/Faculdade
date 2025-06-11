import random as r  # BIBLIOTECAS IMPORTADAS
import os

coins = 100                                     
possibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pagamento = 0

def sorteio():                           #SORTEADOR DA ROLETA DO TIGRINHO
    x = r.choice(possibilidades)
    y = r.choice(possibilidades)
    z = r.choice(possibilidades)
    return x, y, z

def resultado(ganho = False):            #RESULTADO DO SORTEIO, SE PERDEU OU GANHOU
    print(f'\nA roleta foi: [{x}]   [{y}]   [{z}]')
    if ganho:
        print(f'Você ganhou {pagamento} moedas, seu saldo agora é de {coins} moedas.\n')
    else:
        print(f'Você perdeu {lance} moedas, seu saldo agora é de {coins} moedas.\n')

def sequencia(a, b, c):  #COLOCANDO OS NÚMEROS DA ROLETA ORDENADOS PARA COMPARAÇÃO!
    if a > b:
        t = a
        a = b
        b = t
    if b > c:
        t = b
        b = c
        c = t
    if a > b:
        t = a
        a = b
        b = t
    return a, b, c

def forca():                         #CHAMANDO JOGO DA FORCA
    os.system('cls')
    print('Jogando Forca\n')
    palavra = ""
    revelada = []
    palavra_revelada = []
    matriz = []
    temas = []

    while palavra == "":
        matriz.clear()
        with open("TEMAS.txt","r",encoding="utf-8") as txt:     #UTILIZANDO OUTRO ARQUIVO PARA PEGAR OS TEMAS E AS PALAVRAS
            linhas = txt.readlines()
            for l in linhas:
                lista = l.strip(":").strip("\n").split(":")
                lista[1] = lista[1].split(',')
                matriz.append(lista)
                print(lista[0])      
        escolha = input("\nPra começar o jogo, escolha um dos temas acima: ").upper()
        escolha = int(escolha)
        if escolha < len(matriz):
            palavra = r.choice(matriz[escolha][1])
        else:
            print("\nOpção indisponivel! Escolha novamente!\n")
    
    for x in palavra:
        revelada.append("_")
        palavra_revelada.append(x)
    
    os.system('cls')
    print("Iniciando o jogo!")

    chances = 10
    erradas = []
    print(f"TEMA ESCOLHIDO: {matriz[escolha][0]}")
    print(f"Você agora tem {chances} chances!")
    print(revelada)

    while True:
        letra = input("Entre com a letra desejada: ").upper()
        
        if letra in palavra:
            i = 0
            for x in revelada:
                if letra == palavra[i]:
                    revelada.pop(i)
                    revelada.insert(i, letra)
                    i += 1
                else:
                    i += 1
        else:
            erradas.append(letra)
            chances -= 1
            print("Você errou!")
    
        os.system('cls')
        print(f"TEMA ESCOLHIDO: {matriz[escolha][0]}")
        print(f"Letras tentadas: {erradas}")
        print(f"Você agora tem {chances} chances!")
        print(revelada)
    
        if chances == 0:
            print("DERROTA! Suas chances acabaram!")
            print(f"A palavra era {palavra}.\n")
            break
    
        elif palavra_revelada == revelada:
            print("VITÓRIA! Você acertou a palavra!")
            print(f"A palavra era {palavra}.")
            break

def tigrinho():                               #CHAMANDO JOGO DO TIGRINHO
    global coins, x, y, z, pagamento, lance
    os.system('cls')
    print('Jogando Tigrinho\n')

    while True:
        print('-------------------------------------\n')
        print("PREMIAÇÃO: Se for sorteados 3 números iguais ou em sequência, o valor apostado irá ser pago")
        
        lance_input = input('Digite quanto deseja apostar ou aperte enter/0 para sair: ')

        if lance_input == '' or lance_input == '0':
            print('Saindo do tigrinho...\n')
            break

        lance = int(lance_input)
        if lance >= 1 and lance <= coins:
            check = input('Tem certeza do seu lance? (s/n): ').upper()

            if check == 'S':
                x, y, z = sorteio()
                a, b, c = sequencia(x, y, z)

                if x == y == z:
                    pagamento = lance + x
                    coins += pagamento
                    resultado(True)
                
                elif (a, b, c) == (a, a+1, a+2):
                    pagamento = (x + y + z) / 3 + lance
                    coins += pagamento
                    resultado(True)

                else:
                    coins = coins - lance
                    resultado()
            
            elif check == 'N':
                print('Digite o lance novamente. ')
            
            else:
                print('Opção inválida. ')
        
        else:
            print('Quantidade de moedas inválidas.')

        if coins <= 0:
            print("Saldo zerado, não é possível continuar apostando.")
            break

def menu():  #FUNÇÃO INICIAL DO PROJETO, O MENU VAI DAR AS OPÇÕES DO QUE SE PODE FAZER NO SISTEMA!
    print('------------------------------------------------------------------------')
    print("                           # MENU # ")
    print("                  O que deseja fazer hoje?")
    print('              1 - Forca | 2 - Tigrinho | 3 - Sair\n')
    escolha = input('Digite o número da opção desejada: ').strip()

    if escolha == '1':
        forca()
        menu()

    elif escolha == '2':
        tigrinho()
        menu()

    elif escolha == '3':
        print("Saindo do sistema!")
        return

    else:
        print('Opção inválida\n')
        menu()

menu()