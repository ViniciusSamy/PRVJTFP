import re #expressoes regulares para ler somente os inteiros
from Classes.Cliente import Cliente


# (Recebe instancia) ->
# Retorna os seguintes parametros:
# (
# nome da instancia,
# numero maximo de veiculos,
# capacidade dos veiculos,
# lista do tipo cliente com os dados do mesmos
# )
#Ex: a,b,c,d,e = lendo_instancia('etc/intancia.txt')
def ler_instancia(instancia_dir):

    try:
        file = open(instancia_dir, 'r')
    except:
        print("Erro ao abrir o arquivo !")
        return [];

    #--------Lendo arquivo-----------#
    nome_instancia = file.readline()
    nome_instancia.rstrip('\n') #Remove quebra de linha do nome caso haja


    # le linha a linha e se a linha tiver elementos numericos adciona a linha na lista numeros
    numeros = []
    for linha in file:
        itens_linha = [int(n) for n in re.findall(r'\d+', linha)]  # seleciona somente os numeros da linha

        if (len(itens_linha) > 0):  # Evita que listas vazias (linhas sem nenhum numero) sejam adicionadas
            numeros.append(itens_linha)


    #print(numeros) #DEBUG


    #Obtendo os dados do cabeçalho (numero de veiculos e capacidade de cada veiculo)
    numero_veiculos = numeros[0][0]
    capacidade_veiculo = numeros[0][1]
    numeros.pop(0) #Uma vez que já foram lidos são apagados da lista


    #print(numeros) #DEBUG


    #Os elementos restantes da lista representam clientes.
    #Os dados de cada cliente(linha ou elemento da lista numeros) são usados para criar um objeto do tipo cliente
    #Cada objeto Cliente é armazenado na lista lista_cliente
    lista_cliente = []
    for cliente in numeros:
        clt = Cliente(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6])
        lista_cliente.append(clt)

    #print(lista_cliente) #DEBUG

    #Retorna todos os itens obtidos da instancia
    return (nome_instancia.rstrip('\n'), numero_veiculos, capacidade_veiculo, lista_cliente)