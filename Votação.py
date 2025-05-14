listaCandidatos = ['Maria','José','João']
listaVotos = [0,0,0]
count = 0
nome_novo = ""

print("Antes de começar a votação, você quer:")
print("1 - Colocar um nome na candidatura")
print("2 - Remover um nome da candidatura")
print("3 - Ir direto pra votação")

while True:
    resposta_inicio = int(input("Responda aqui com uma das alternativas: "))
    if (resposta_inicio == 1):
        nome_novo = input("Adicione o nome do candidato: ")
        listaCandidatos.append(listaCandidatos)
    elif (resposta_inicio == 2):
        remover_nome = input("Digite o nome do candidato a ser retirado da votação: ")
        if(remover_nome in listaCandidatos):
            remover_nome.remove(listaCandidatos)
    if(resposta_inicio == 3):
        print("ELEIÇÕES 2025")
        print("Escolha um candidato:")
        while count < len(listaCandidatos):
            print(f"{count+1} - {listaCandidatos[count]}")
            count += 1 
        processo = input('Escolha seu candidato: ')
        if (processo.upper() == listaCandidatos[0].upper()) or (processo == 1):
            listaVotos[0] += 1
        else:
            if (processo.upper() == listaCandidatos[1].upper()) or (processo == 2):
                listaVotos[1] += 1
            else:
                if (processo.upper() == listaCandidatos[2].upper()) or (processo == 3):
                    listaVotos[2] += 1
                else:
                    break

print("RESULTADOS DA VOTAÇÃO:")
print("1:Maria ->", listaVotos[0])
print("2:José ->", listaVotos[1])
print("3:João ->", listaVotos[2])
if listaCandidatos == nome_novo:
    print(listaCandidatos)

if (listaVotos[0] > listaVotos[1] and listaVotos[0] > listaVotos[2]):
    print('O vencedor é:', listaCandidatos[0],"com",listaVotos[0],"votos")
else:
    if (listaVotos[1] > listaVotos[0] and listaVotos[1] > listaVotos[2]):
        print('O vencedor é:', listaCandidatos[1],"com",listaVotos[1],"votos")
    else:
        if (listaVotos[2] > listaVotos[0] and listaVotos[2] > listaVotos[1]):
            print('O vencedor é:', listaCandidatos[2],"com",listaVotos[2],"votos")


