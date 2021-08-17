import random
import numpy as np
from Classes.Cliente import Cliente

class Problema:

    __numero_max_veiculos = 0  # [int] numero de veiculos
    __capacidade_veiculo = 0 # [int] capacidade de cada veiculo (frota homogenea)
    __velocidade_veiculo = 0.0  # [float] Respresenta uma velocidade constante para os veiculos
    __custo_tranporte_unidade_distancia = 0.0  # [float] Custo de transporte por unidade de distencia associado a cada veiculo
    __custo_veiculo = 0.0  # [float] Repesenta o custo fixo do veiculo
    __tempo_servico = 0 # [int] Tempo de serviço de cada cliente

    __numero_clientes = 0 # [int] numero total de cosumidores(clientes)
    __dados_cliente = [] # [list of list] lista que armazena os dados de cada cliente i como vetor e j um atributo desse cliente

    __qualidade_produto = 0.0 # [float] valor associado a qualidade do produto [beta] possui intervalo entre 0 e 1
    __ciclo_de_vida_produto = 0.0 # [float] Decaimento da qualidade do produto por unidade de tempo

    __w1 = 0 # [int] Coeficiente de ..
    __w2 = 0 # [int] Coeficiente de ..
    __w3 = 0 # [int] Coeficiente de ..


    #-----------CONSTRUTOR------------#


    #-----------SETTERS-----------#

    def set_numero_max_veiculos(self, numero_max_veiculos):
        # verifica tipo
        if (type(numero_max_veiculos) is int):
            self.__numero_max_veiculos = numero_max_veiculos
            return True
        else:
            return False

    def set_capacidade_veiculo(self, capacidade_veiculo):
        # verifica tipo
        if (type(capacidade_veiculo) is int):
            self.__capacidade_veiculo = capacidade_veiculo
            return True
        else:
            return False

    def set_velocidade_veiculo (self, velocidade_veiculo ):
        # verifica tipo
        if (type(velocidade_veiculo) is float):
            self.__velocidade_veiculo  = velocidade_veiculo
            return True
        else:
            return False

    def set_custo_tranporte_unidade_distancia (self, custo_tranporte_unidade_distancia ):
        #verifica tipo
        if (type(custo_tranporte_unidade_distancia ) is float ):
            self.__custo_tranporte_unidade_distancia  = custo_tranporte_unidade_distancia
            return True
        else:
            return False

    def set_custo_veiculo(self, custo_veiculo):
        # verifica tipo
        if (type(custo_veiculo) is float):
            self.__custo_veiculo = custo_veiculo
            return True
        else:
            return False

    def set_tempo_servico(self, tempo_servico):
        # verifica tipo
        if (type(tempo_servico) is int):
            self.__tempo_servico = tempo_servico
            return True
        else:
            return False

    def set_numero_clientes(self, numero_clientes):
        # verifica tipo
        if (type(numero_clientes) is int):
            self.__numero_clientes = numero_clientes
            return True
        else:
            return False

    def set_dados_cliente(self, dados_cliente):
        # verifica tipo
        if (type(dados_cliente) is list):
            self.__dados_cliente = dados_cliente
            return True
        else:
            return False

    def set_qualidade_produto(self, qualidade_produto):
        # verifica tipo
        if (type(qualidade_produto) is float):
            self.__qualidade_produto = qualidade_produto
            return True
        else:
            return False

    def set_ciclo_de_vida_produto(self, ciclo_de_vida_produto):
        # verifica tipo
        if (type(ciclo_de_vida_produto) is float):
            self.__ciclo_de_vida_produto = ciclo_de_vida_produto
            return True
        else:
            return False

    def set_w1(self, w1):
        # verifica tipo
        if (type(w1) is int):
            self.__w1 = w1
            return True
        else:
            return False

    def set_w2(self, w2):
        # verifica tipo
        if (type(w2) is int):
            self.__w2 = w2
            return True
        else:
            return False

    def set_w3(self, w3):
        # verifica tipo
        if (type(w3) is int):
            self.__w3 = w3
            return True
        else:
            return False

    # Uma vez que se setamos o tempo de servico temos que atualizar eles nos dados dos clientes
    def att_tempo_servico(self):
        clientes = self.get_dados_cliente()
        tempo_de_servico = self.get_tempo_servico()

        for cliente in clientes:
            t_servico = tempo_de_servico if cliente.get_tempo_de_servico() > 0 else 0  # Manter a origem sem tempo de servico
            cliente.set_tempo_de_servico(t_servico)

    def att_janelas_de_tempo(self, operador):
        for cliente in self.__dados_cliente:
            janela_inicio = cliente.get_janela_inicio()
            janela_inicio = janela_inicio * operador
            cliente.set_janela_inicio(janela_inicio)

            janela_fim = cliente.get_janela_fim()
            janela_fim = janela_fim * operador
            cliente.set_janela_fim(janela_fim)

            tempo_servico = cliente.get_tempo_de_servico()
            tempo_servico = tempo_servico * operador
            cliente.set_tempo_de_servico(tempo_servico)

    #------------GETTERS-----------#

    def get_custo_tranporte_unidade_distancia(self):
        return self.__custo_tranporte_unidade_distancia

    def get_numero_max_veiculos(self):
        return self.__numero_max_veiculos

    def get_capacidade_veiculo(self):
        return self.__capacidade_veiculo

    def get_velocidade_veiculo(self):
        return self.__velocidade_veiculo

    def get_custo_veiculo(self):
        return self.__custo_veiculo

    def get_tempo_servico(self):
        return self.__tempo_servico

    def get_numero_clientes(self):
        return self.__numero_clientes

    def get_dados_cliente(self):
        return list(self.__dados_cliente)

    def get_qualidade_produto(self):
        return self.__qualidade_produto

    def get_ciclo_de_vida_produto(self):
        return self.__ciclo_de_vida_produto

    def get_w1(self):
        return self.__w1

    def get_w2(self):
        return self.__w2

    def get_w3(self):
        return self.__w3

    def get_demanda_total(self):
        demanda_total =0

        for cliente in self.__dados_cliente:
            demanda_total += cliente.get_demanda()

        return  demanda_total






    #------------CRIAÇÃO-DE-SOLUÇÕES-----------#

    #--------->ALEATORIA
    #Criando Solução Aleatoria respeitando as Demandas
    def criando_solucao_aleatoria(self):
        ##!!!!!!NÂO CONSIDERA DISTÂNCIAS NA GERAÇÃO
        ##!!!!!!!NÃO CONSIDERA JANELAS DE TEMPO NA GERAÇÃO

        clientes_nao_atendidos = list(self.get_dados_cliente()) #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos

        cliente_origem = clientes_nao_atendidos.pop(0) #Retira o primeiro cliente(origem de destribuição) da lista de clientes nao atendidos

        random.shuffle(clientes_nao_atendidos) #Embaralha todos os clientes atendidos para criar ordem aleatoria de adição

        solucao = [] #armazena a solucao

        capacidade_veiculo = self.get_capacidade_veiculo() #capacidade do veiculo(frota homogenea)

        #-------------Enquanto houver clientes a serem atendidos------------#
        while(len(clientes_nao_atendidos) > 0):

            rota = [] #Rota atribuida ao veiculo. A cada iteração o veiculo muda e rota começa vazia
            demanda_rota = 0 #Calcula demanda da rota

            #Toda rota começa da origem
            rota.append(cliente_origem)
            demanda_rota += cliente_origem.get_demanda() #Origem não possui demanda então continua em 0

            # print(clientes_nao_atendidos) #DEBUG
            # print(capacidade_veiculo) #DEGUG
            # print(cliente_origem) #DEBUG


            #percorre todos os cliente nao atendidos enquanto a demanda da rota não for atendida
            i = 0
            while( i < len(clientes_nao_atendidos) ):

                cliente = clientes_nao_atendidos[i] #Varivel que recebe o cliente da iteração
                demanda_cliente = cliente.get_demanda() #Demanda do cliente da iteração

                #verifica se a adição do cliente da iteração irá exceder a capacidade maxima do veiculo
                if(demanda_rota + demanda_cliente <= capacidade_veiculo):

                    #adiciona o cliente a rota do veiculo
                    rota.append(cliente)
                    demanda_rota += demanda_cliente

                    #remove o cliente adicionado a rota da lista de clientes nao atendidos
                    clientes_nao_atendidos.remove(cliente)
                    #Decrementa o iterador toda vez que um cliente é retirado da lista (evita que algum cliente seja pulado)
                    i -= 1

                #Se a demanda da rota ja atingiu a capacidade maxima do veiculo sai do loop
                if(demanda_rota == capacidade_veiculo):
                    break


                i += 1 # incrementa o iterador


            rota.append(cliente_origem) #A rota termina na origem

            solucao.append(rota) #Adiciona a rota a solução


            #print('append na solucao') #DEBUG
            #print(rota) #DEBUG

        return solucao


    #--------->CLUSTERIZADO
    #criando solucao a partir dos clusters (KMEANS)
    def criando_solucao_clusterizada(self, clusters, matriz_distancias):
        dados_clientes = self.__dados_cliente
        capacidade_veiculo = self.get_capacidade_veiculo()

        #Copiando clusters (para não alterar fora da função)
        clusters = list(clusters)
        for i in range(len(clusters)):
            clusters[i] = list(clusters[i])

        #Solução (conjunto de rotas
        solucao = []

        #Rota do veiculo e demanda acumulada desse veiculo
        rota = []
        rota.append(dados_clientes[0])
        demanda_atual = 0

        #Continua enquanto houverem elementos no clusters (precisam ser adicionados
        while len(clusters) > 0:

            #Lista com os clusters já percorridos por uma rota
            clusters_percorridos = []

            #Indice cluster a ser adicionado a solução (começa pelo primeiro)
            indice_cluster = 0

            #Variavel que armazena o ultimo cliente adicionado a rota
            ultimo_cliente = 0 #começa pela origem



            # Indica que o cluster já foi visitado
            clusters_percorridos.append(indice_cluster)
            # Copia o cluster da iteração somente para avaliar os clientes
            cluster_iteracao = list(clusters[indice_cluster])
            while True:


                #print(f"CLUSTER itr = {cluster_iteracao}") #DEBUG


                #Busca o cliente mais próximo ao ultimo cliente adicionado dentro do cluster da iteração
                indice_cliente = self.mais_proximo_cluster(ultimo_cliente, cluster_iteracao, matriz_distancias)
                cliente = cluster_iteracao.pop(indice_cliente)

                # Verifica se atende a demanda e caso atenda é adiconado a rota do veiculo
                if (dados_clientes[cliente].get_demanda() + demanda_atual <= capacidade_veiculo):

                    #Adiciona a rota e atualiza demanda do veiculo
                    rota.append(dados_clientes[cliente])
                    demanda_atual += dados_clientes[cliente].get_demanda()

                    #Retira o elemento dos clusters (o original e não o cluster da iteração)
                    clusters[indice_cluster].remove(cliente)

                    #Define o ultimo cliente adicionado
                    ultimo_cliente = cliente


                #Verifica se o cluster atual ainda possui elementos, caso não haja passa para o mais próximo do ultimo cliente ( que ainda nao foi percorrido)
                if (len(cluster_iteracao) <= 0):
                    indice_cluster = self.cluster_mais_proximo(ultimo_cliente, clusters, clusters_percorridos, matriz_distancias)
                    # Indica que o cluster já foi visitado
                    clusters_percorridos.append(indice_cluster)
                    # Copia o cluster da iteração somente para avaliar os clientes
                    cluster_iteracao = list(clusters[indice_cluster])
                    #print (f"indice Cluster {indice_cluster}") #DEBUG




                #CONDICAO DE PARADA DO WHILE
                if( len(clusters_percorridos) >= len(clusters) ):
                    #Adiciona a rota a solucao
                    solucao.append(rota)
                    rota.append(dados_clientes[0])
                    #print(f"ROTA{rota}") #DEBUG
                    #Definindo um nova rota
                    demanda_atual = 0
                    rota = []
                    rota.append(dados_clientes[0])


                    break

            #Remove os clusters que não possuem mais nenhum cliente(vazios)
            self.retirar_clusters_vazios(clusters)








        return solucao

    #Procura o cliente mais proximo ao ultimo clientente adicionado em um certo cluster
    def mais_proximo_cluster(self, i ,cluster, matriz_distancias):
        min_distancia = float("inf")
        indice_min = 0
        indice = 0

        for j in cluster:
            # print(f"[{j}]->{matriz_distancias[i][j]} < {min_distancia} = {matriz_distancias[i][j] < min_distancia}") #DEBUG
            if(matriz_distancias[i][j] < min_distancia):

                min_distancia = matriz_distancias[i][j]
                indice_min = indice


            indice += 1

        return indice_min

    def retirar_clusters_vazios(self, clusters):
        #clusters_vazios = []
        i = 0
        while( i < len(clusters) ):

            if(len(clusters[i]) <= 0 ):
                clusters.pop(i)
                i -= 1 #Retrocede o iterador (numero de clusters diminui)

            i += 1



        #clusters.pop(clusters_vazios)
        #for i in clusters_vazios:
         #  clusters.pop(i)

    #Verifica qual o cluster ainda não visitado mais proximo do ultimo cliente adicionado
    def cluster_mais_proximo(self, indice_cliente, clusters, clusters_percorridos, matriz_distancias):
        min_distancia = float("inf")

        indice_cluster_min = -1
        for i in range(len(clusters)):

            #Se ainda não foi percorrido
            if( i not in clusters_percorridos):

                for j in clusters[i]:

                    if(matriz_distancias[indice_cliente][j] < min_distancia):
                        min_distancia = matriz_distancias[indice_cliente][j]
                        indice_cluster_min = i


        return indice_cluster_min





    #------------OBJETIVOS-----------#

    #Calcula a função objetivo 1 para uma dada solução ( utiliza-se de seus instantes de entrega )
    def func_obj1(self, solucao, instantes):
        solucao_cpy =  list(solucao) # copia da solução


        T = self.get_ciclo_de_vida_produto()

        t1=0
        t2=0
        t3=0


        #-------Soma do custo por unidade percorrida do veiculo-------#
        sum_1 = 0.0 #custo dos veiculos dados os km
        custo_por_unidade = self.get_custo_tranporte_unidade_distancia()  # Custo por unidade percorrida do veiculo
        for i in range(len(solucao_cpy)):
            rota = solucao[i]
            for j in range(len(rota) - 1):
                cliente_atual = rota[j]
                cliente_proximo = rota[j+1]

                sum_1 += cliente_atual.calcula_distancia_clientes(cliente_proximo) * custo_por_unidade
        #print(f"Soma Custo transporte: {sum_1}") #DEBUG



        # -------Soma do custo pelo numero de veiculos alocados-------#
        sum_2 = 0.0 #custo dado o numero de veiculos da solucao
        n_veiculos = len(solucao)
        custo_por_veiculo = self.get_custo_veiculo()
        sum_2 = n_veiculos * custo_por_veiculo
        #print(f"Soma numero veiculos: {sum_2}")  # DEBUG


        # -------Soma do custo pelo adiantamento e ultrapassagem das janelas-------#
        sum_3 = 0.0 #Soma referente ao adiantamento das janelas
        w1 = self.get_w1() #Coeficiente de adiantamento

        sum_4 = 0.0  # Soma referente a ultrapassagem das janelas
        w2 = self.get_w2()  # Coeficiente de ultrapassagem

        #Percorre clientes da solução
        for i in range(len(solucao_cpy)):
            rota = solucao_cpy[i]
            for j in range(len(rota) - 1): #Não considera a janela de tempo quando o veiculo volta a origem
                cliente = rota[j]
                cliente_janela_inicio = cliente.get_janela_inicio()
                cliente_janela_fim = cliente.get_janela_fim()
                cliente_instante_entrega = instantes[i][j]

                sum_3 += 0.0 if (cliente_instante_entrega >= cliente_janela_inicio) else cliente_janela_inicio - cliente_instante_entrega #Só adiciona se houver um adiantamento
                sum_4 += 0.0 if (cliente_janela_fim >= cliente_instante_entrega) else cliente_instante_entrega - cliente_janela_fim  # Só adiciona se houver uma ultrapassagem

                t1 += 0.0 if (cliente_instante_entrega >= cliente_janela_inicio) else 1

                t2 += 0.0 if (cliente_janela_fim >= cliente_instante_entrega) else 1



        #aplicando coeficientes
        sum_3 = sum_3 * w1
        sum_4 = sum_4 * w2
        #print(f"Soma Adianto(W1): {sum_3}")  # DEBUG
        #print(f"Soma Atraso(W2): {sum_4}")  # DEBUG
        #print(f"t1: {t1}")
        #print(f"t2: {t2}")


        # -------Soma do custo pelos danos aos produtos no instante de entrega-------#
        sum_5 = 0 #Armazena a soma de danos ao produto
        w3 = self.get_w3()  # Coeficiente dos danos

        # Percorre clientes da solução
        for i in range(len(solucao_cpy)):
            rota = solucao_cpy[i]
            for j in range(len(rota) - 1):
                cliente = rota[j]
                cliente_demanda = cliente.get_demanda()
                cliente_instante_entrega = max(instantes[i][j],cliente.get_janela_inicio())

                sum_5 += self.phi(cliente_instante_entrega,T)*cliente_demanda

        sum_5 = sum_5*w3
        #print(f"Soma danos(W3):  {sum_5}")  # DEBUG

        return sum_1+sum_2+sum_3+sum_4+sum_5







        ###################OBJ2

    # Calcula a função objetivo 1 para uma dada solução ( utiliza-se de seus instantes de entrega )
    def func_obj2(self, solucao, instantes  ):

        T = self.get_ciclo_de_vida_produto()

        numerador = 0.0
        denominador = 0.0

        for i in range(len(solucao)):
            rota = solucao[i]
            rota_instantes = instantes[i]

            for j in range(len(rota)):
                cliente = rota[j]
                cliente_ti = max(rota_instantes[j],cliente.get_janela_inicio())

                numerador += self.beta(cliente_ti,T) * cliente.get_demanda()
                denominador += cliente.get_demanda()


        obj2 = numerador/denominador
        return obj2

    def phi(self, instante, T):
        return np.exp(((np.log(2) / T) * instante)) - 1

    def beta(self, instante, T):
        beta = 1 - (self.phi(instante, T))
        beta = 0.0 if ( beta < 0) else beta #se beta negativo

        return beta






    # ----------FUNÇÕES DE TRATAMENTO DE SOLUÇÕES(USO EXTERNO)---------#
    def objs(self, array_solucao):

        solucao = self.converte_array_solucao(array_solucao)

        instantes = self.calcula_instantes_de_entrega(solucao)

        obj1 = self.func_obj1(solucao, instantes)
        obj2 = self.func_obj2(solucao, instantes)

        return obj1, obj2

    # Conversão padrão
    def converte_array_solucao(self, array_solucao):

        clientes = list(self.get_dados_cliente())
        capacidade_veiculo = self.get_capacidade_veiculo()

        solucao = []
        rota = []
        demanda_rota = 0





        rota.append(clientes[0])

        for k in array_solucao:
            cliente = clientes[k]

            if (demanda_rota + cliente.get_demanda() <= capacidade_veiculo):
                rota.append(cliente)
                demanda_rota += cliente.get_demanda()

            else:
                rota.append(clientes[0])
                solucao.append(rota)

                rota = []
                demanda_rota = 0
                tempo_acumulado = 0
                rota.append(clientes[0])

                rota.append(cliente)
                demanda_rota += cliente.get_demanda()

        rota.append(clientes[0])
        solucao.append(rota)
        return solucao

    # Conversao considerando uma qualidade minima
    def converte_array_solucao_Qmin(self, array_solucao):

        clientes = list(self.get_dados_cliente())
        capacidade_veiculo = self.get_capacidade_veiculo()
        velocidade = self.__velocidade_veiculo
        qualidade_min = self.__qualidade_produto
        T = self.__ciclo_de_vida_produto

        solucao = []
        rota = []
        demanda_rota = 0


        rota.append(clientes[0])
        istRota = [0]

        for k in array_solucao:

            cliente = clientes[k]
            tempo_entre_cli = rota[-1].calcula_distancia_clientes(cliente) / velocidade
            ult_instante = istRota[-1]
            ts_anterior = rota[-1].get_tempo_de_servico()
            istpart_anterior = max(ult_instante, rota[-1].get_janela_inicio() ) + ts_anterior
            istChegada = istpart_anterior + tempo_entre_cli
            istAtendimento = max(istChegada, cliente.get_janela_inicio())

            print(f"[{k}] -> {self.beta(istAtendimento,T)} >= {qualidade_min} ({istChegada})", end="")
            if demanda_rota + cliente.get_demanda() <= capacidade_veiculo and self.beta(istAtendimento,T) >= qualidade_min :
                rota.append(cliente)
                demanda_rota += cliente.get_demanda()
                istRota.append(istChegada)
                print(" IN")

            else:
                print(" NOT IN")
                rota.append(clientes[0])
                solucao.append(rota)

                rota = []
                demanda_rota = 0
                rota.append(clientes[0])
                istRota = [0]

                rota.append(cliente)
                demanda_rota += cliente.get_demanda()

        rota.append(clientes[0])
        solucao.append(rota)
        return solucao


    def converte_solucao_array(self, solucao):
        list_temp = []
        for i in range(len(solucao)):
            for j in range(len(solucao[i])):
                index_i = solucao[i][j].get_indice()
                list_temp.append(index_i)

        return np.array(list_temp)

        # Retorna uma lista de lista com os instantes em que os clientes foram atendidos em um dada solucao



    # Retorna uma lista de lista com os instantes em que os clientes foram atendidos em um dada solucao
    # Uma mesma posição(i,j) tanto nos instantes quanto na solução correspondem aos dados de um mesmo cliente
    def calcula_instantes_de_entrega(self, solucao):
        # !!!!!!! PRIMEIRO INSTANTE DA ROTA É IGUAL A JANELA DE TEMPO DO PRIMEIRO CLIENTE

        solucao_copia = list(solucao) #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos




        instantes_entregas_solucao = [] #armazena os instantes de entrega de toda a solução


        #i_rota = 0 #Armazena a rota(veiculo) da iteração

        for i_rota in range(len(solucao)) :
            rota_clientes_nao_calculados = list(solucao[i_rota])

            instantes_entregas_rota = []  # armazena os intantes de entrega de toda a rota

            tempo_acumulado = 0  # tempo acumulado até o momento

            tempo_espera = 0 #Caso um veiculo chege antes do inicio da janela de tempo de um cliente sua janela de tempo é cosiderada no atendimento do seus sucessor


            #Estabelecendo os primeiro clientes da rota a tere instantes acumulados
            cliente_anterior = rota_clientes_nao_calculados.pop(0)  # pegando primeiro cliente(origem) da rota da iteração e remove ele
            cliente_anterior_t_servico = cliente_anterior.get_tempo_de_servico()  # tempo de serviço do cliente da iteração

            cliente_atual = rota_clientes_nao_calculados.pop(0)  # pegando primeiro cliente(id:1) da rota da iteração e remove ele

            distancia_clientes = cliente_atual.calcula_distancia_clientes(cliente_anterior) #calcula a distancia entre os clientes

            velocidade_veiculo = self.get_velocidade_veiculo()


            ##Calcula os instantes de atendimeto de cada cliente da rota
            for i_cliente in range( len(rota_clientes_nao_calculados) ):


                # Adiciona o instante de entrega do cliente anterior
                instantes_entregas_rota.append(tempo_acumulado)

                # Calcula tempo entre cliente anterior e o atual
                tempo_entre_clientes = distancia_clientes / (velocidade_veiculo)

                #Calcula o tempo de espera que houve no cliente anterior se houver
                janela_inicio_cliente_anterior = cliente_anterior.get_janela_inicio()
                tempo_espera = 0 if( tempo_acumulado >= janela_inicio_cliente_anterior ) else janela_inicio_cliente_anterior - tempo_acumulado

                # Calcula o tempo acumulado entre o cliente atual e o anterior
                tempo_acumulado = tempo_acumulado + cliente_anterior_t_servico + tempo_entre_clientes + tempo_espera

                #Atualiza o cliente anterior e o proximo
                cliente_anterior = cliente_atual #Cliente atual passa a ser o anterior

                cliente_anterior_t_servico = cliente_anterior.get_tempo_de_servico() #Atualiza o temp ode serviço do cliente anterior

                cliente_atual = rota_clientes_nao_calculados.pop(0) #Cliente atual é agora o proximo cliente (primeiro da list de rota)

                distancia_clientes = cliente_atual.calcula_distancia_clientes(cliente_anterior) # Atualiza a distancia entre esses clientes




            instantes_entregas_rota.append(tempo_acumulado) #adiciona o instante de entreg do ultimo cliente da rota


            ##Calcula e adiciona instante do ultimo cliente (origem)
            tempo_entre_clientes = distancia_clientes / velocidade_veiculo  # Calcula tempo entre cliente anterior e o atual

            tempo_acumulado = tempo_acumulado + cliente_anterior_t_servico + tempo_entre_clientes  # Calcula o tempo acumulado entre o cliente atual e o anterior

            instantes_entregas_rota.append(tempo_acumulado)  # adiciona o instante de entreg do ultimo cliente da rota



            # print(instantes_entregas_rota) #DEBUG
            instantes_entregas_solucao.append(instantes_entregas_rota) #Adiciona os instantes da rota aos instantes da solução


        # print(instantes_entregas_solucao); #DEBUG

        return instantes_entregas_solucao

    def calcula_instante_de_entrega_sucinto(self, solucao):
        #Cria uma copia da solucao
        solucao = list(solucao)

        #Estrtura que irá armazenar os intantes da solução
        instantes_solucao = []

        #Velocidade veiculo
        velocidade = self.__velocidade_veiculo

        #Percorre rotas
        for i in range(len(solucao)):
            rota = solucao[i]
            instantes_rota = [0]


            # Percorre clientes da rota
            for j in range(len(rota)-1):
                # Cliente Anterior
                cliente_anterior = rota[j]
                #Cliente Atual
                cliente_atual = rota[j+1]

                #Distancia entre os clientes
                distancia = cliente_atual.calcula_distancia_clientes(cliente_anterior)

                #Tempo entre clientes
                tempo = distancia/velocidade

                #Ultimo instante adicionado
                ult_instante = instantes_rota[-1]

                #Tempo de servico cliente anterior
                ts_anterior = cliente_anterior.get_tempo_de_servico()

                #Instante de partida do cliente anterior
                Ipart_anterior = max(ult_instante, cliente_anterior.get_janela_inicio()) + ts_anterior

                #Instante de chegada ao cliente atual
                Ichegada = Ipart_anterior + tempo

                #Adiciona o instante de chegada
                instantes_rota.append(Ichegada)

            instantes_solucao.append(instantes_rota)


        return instantes_solucao










    #Calcula o valor objetivos de rotas externas[clientes representados como ints]
    def func_objs(self, solucao_ints):

        solucao = self.repara_rota(solucao_ints)

        instantes = self.calcula_instantes_de_entrega(solucao)

        obj1 = self.func_obj1(solucao, instantes)
        obj2 = self.func_obj2(solucao, instantes)

        return obj1, obj2

    #Repara as rotas caso a origem ou algum outro cliente esteja represendo por um inteiros
    def repara_rota(self, solucao):

        clientes = list(self.get_dados_cliente())

        for i in range(len(solucao)):

            for j in range(len(solucao[i])):
                if type(solucao[i][j]) is int:
                    index = solucao[i][j]
                    solucao[i][j] = clientes[index]



        return solucao



    #-----------PRINT-----------#
    def print(self):
        print(f"\nnumero_veiculo = {self.get_numero_max_veiculos()}"
            f"\ncapacidade_veiculo = {self.get_capacidade_veiculo()}"
            f"\nvelocidade_veiculo = {self.get_velocidade_veiculo()}"
            f"\ncusto_tranporte_unidade_distancia = {self.get_custo_tranporte_unidade_distancia()}"
            f"\ncusto_veiculo = {self.get_custo_veiculo()}"
            f"\ntempo_servico = {self.get_tempo_servico()}"
            f"\nnumero_clientes = {self.get_numero_clientes()}"
            f"\ndados_cliente = {self.get_dados_cliente()}"
            f"\nqualidade_produto = {self.get_qualidade_produto()}"
            f"\nciclo_de_vida_produto = {self.get_ciclo_de_vida_produto()}"
            f"\nw1 = {self.get_w1()}"
            f"\nw2 = {self.get_w2()}"
            f"\nw3 = {self.get_w3()}"
        )














    ##############################------------FUNCOES PARA TESTE ------------#######################
    def criando_solucao_aleatoria_2(self):
        ##!!!!!!!!!!!PROBLEMA: Não Considerao numero maximo de veiculos
        ##!!!!!!!!!!!PROBLEMA: Não Cosidera a qualidade minima
        ##!!!!!!!!!!!PROBLEMA: Não considera as Janelas de Tempo

        clientes_nao_atendidos = list(self.get_dados_cliente()) #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos

        cliente_origem = clientes_nao_atendidos.pop(0) #Retira o primeiro cliente(origem de destribuição) da lista de lcientes nao atendidos

        random.shuffle(clientes_nao_atendidos) #Embaralha todos os clientes atendidos para criar ordem aleatoria de adição

        solucao = [] #armazena a solucao

        capacidade_veiculo = self.get_capacidade_veiculo() #capacidade do veiculo(frota homogenea)

        #-------------Equanto houver clientesa serem atendidos------------#
        while(len(clientes_nao_atendidos) > 0):

            rota = [] #Rota atribuida ao veiculo. A cada iteração o veiculo muda e rota começa vazia
            demanda_rota = 0 #Calcula demanda da rota
            tempo_acumulado = 0 #Tempo acumulado da rota

            #Toda rota começa da origem
            rota.append(cliente_origem)
            demanda_rota += cliente_origem.get_demanda()

            # print(clientes_nao_atendidos) #DEBUG
            # print(capacidade_veiculo) #DEGUG
            # print(cliente_origem) #DEBUG


            #percorre todos os cliente nao atendidos
            i = 0
            while( i < len(clientes_nao_atendidos) ):

                cliente = clientes_nao_atendidos[i] #Varivel que recebe o cliente da iteração
                demanda_cliente = cliente.get_demanda() #Demanda do cliente da iteração
                cliente_janela_inicio = cliente.get_janela_inicio()
                cliente_janela_fim = cliente.get_janela_fim()
                ultimo_cliente_rota = rota[-1]

                #verifica se a adição do cliente da iteração irá exceder a capacidade maxima do veiculo
                a = ultimo_cliente_rota.get_tempo_de_servico()
                b = cliente.calcula_distancia_clientes(ultimo_cliente_rota)
                c = self.get_velocidade_veiculo()
                tempo_teste = ultimo_cliente_rota.get_tempo_de_servico() + (cliente.calcula_distancia_clientes(ultimo_cliente_rota) * (1/self.get_velocidade_veiculo()))

                if(demanda_rota + demanda_cliente <= capacidade_veiculo and (tempo_teste+tempo_acumulado >= cliente_janela_inicio and cliente_janela_fim >= tempo_teste+tempo_acumulado)):

                    #adiciona o cliente a rota do veiculo
                    tempo_acumulado += tempo_teste
                    rota.append(cliente)
                    demanda_rota += demanda_cliente

                    #remove o cliente adicionado a rota da lista de clientes nao atendidos
                    clientes_nao_atendidos.remove(cliente)

                    #O iterador é reniciado toda vez que uma solução é adicionado.
                        #Permite que elementos que não passaram nas iterações anteriores sejam reanalisados, uma vez que o tempo muda eles tem a possibilidade de serem aceitos
                    i = 0

                #Se a demanda da rota ja atingiu a capacidade maxima do veiculo sai do loop
                if(demanda_rota == capacidade_veiculo):
                    break


                i += 1 # incrementa o iterador



            solucao.append(rota)


            #print('append na solucao') #DEBUG
            #print(rota) #DEBUG

        return solucao

    def criando_solucao_aleatoria_3(self, clientes):
        ##!!!!!!!!!!!PROBLEMA: Não Considerao numero maximo de veiculos
        ##!!!!!!!!!!!PROBLEMA: Não Cosidera a qualidade minima
        ##!!!!!!!!!!!PROBLEMA: Não considera as Janelas de Tempo

        clientes_nao_atendidos = list(clientes) #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos

        cliente_origem = clientes_nao_atendidos.pop(0) #Retira o primeiro cliente(origem de destribuição) da lista de lcientes nao atendidos

        random.shuffle(clientes_nao_atendidos) #Embaralha todos os clientes atendidos para criar ordem aleatoria de adição

        solucao = [] #armazena a solucao

        capacidade_veiculo = self.get_capacidade_veiculo() #capacidade do veiculo(frota homogenea)

        #-------------Equanto houver clientesa serem atendidos------------#
        while(len(clientes_nao_atendidos) > 0):



            rota = [] #Rota atribuida ao veiculo. A cada iteração o veiculo muda e rota começa vazia
            demanda_rota = 0 #Calcula demanda da rota

            #Toda rota começa da origem
            rota.append(cliente_origem)
            demanda_rota += cliente_origem.get_demanda()

            #Tempo corrente da rota
            tempo_acumulado = 0

            #velocidade veiculo
            velocidade_veiculo = self.get_velocidade_veiculo()

            #Ultimo cliente adicionado a rota
            ultimo_cliente_rota = rota[-1]

            # ordena clientes_nao atendidos pela janela de tempo (se um cliente é adicionado a rota a ordeção é feita a partit do mesmo)
            # (Prioridade: 1-Obedece uma janela, 2-Obedece somente inicio, 3-Obedece somente fim, 4-Soma das distancia entre as janelas)
            print(clientes_nao_atendidos)
            clientes_nao_atendidos = self.ordena_por_janela_tempo(ultimo_cliente_rota, tempo_acumulado, clientes_nao_atendidos, velocidade_veiculo)
            print(clientes_nao_atendidos)
            print()


            # print(clientes_nao_atendidos) #DEBUG
            # print(capacidade_veiculo) #DEGUG
            # print(cliente_origem) #DEBUG


            #percorre todos os cliente nao atendidos
            i = 0
            while( i < len(clientes_nao_atendidos) ):

                cliente = clientes_nao_atendidos[i] #Varivel que recebe o cliente da iteração
                demanda_cliente = cliente.get_demanda() #Demanda do cliente da iteração

                #verifica se a adição do cliente da iteração irá exceder a capacidade maxima do veiculo
                if(demanda_rota + demanda_cliente <= capacidade_veiculo):

                    #adiciona o cliente a rota do veiculo
                    rota.append(cliente)
                    demanda_rota += demanda_cliente

                    #atualiza o tempo acumulado
                    tempo_acumulado += ultimo_cliente_rota.get_tempo_de_servico() + (cliente.calcula_distancia_clientes(ultimo_cliente_rota) * (1/self.get_velocidade_veiculo()))

                    #remove o cliente adicionado a rota da lista de clientes nao atendidos
                    clientes_nao_atendidos.remove(cliente)

                    # ordena clientes_nao atendidos pela janela de tempo (se um cliente é adicionado a rota a ordeção é feita a partit do mesmo)
                    # (Prioridade: 1-Obedece uma janela, 2-Obedece somente inicio, 3-Obedece somente fim, 4-Soma das distancia entre as janelas)
                    # print(clientes_nao_atendidos) #DEBUG
                    clientes_nao_atendidos = self.ordena_por_janela_tempo(rota[-1], tempo_acumulado, clientes_nao_atendidos, velocidade_veiculo)
                    # print(clientes_nao_atendidos) #DEBUG

                    #Toda vez que um cliente é escolhido o iterador reinicia uma vez que a cliente_nao_atendidos é reordenado
                    i = -1

                #Se a demanda da rota ja atingiu a capacidade maxima do veiculo sai do loop
                if(demanda_rota == capacidade_veiculo):
                    break


                i += 1 # incrementa o iterador



            solucao.append(rota)


            #print('append na solucao') #DEBUG
            #print(rota) #DEBUG

        return solucao

    def ordena_por_janela_tempo(self, ultimo_cliente_rota, tempo_acumulado, clientes_nao_atendidos, velocidade_veiculo ):

        ###EQUACAO PARA CALCULAR SE HA FOLGA NO INICIO DA JANELA
        # C_i(folga_inicio) = C_i(janela_inicio) - ( tempo_acumulado + C_ultimo(tempo_servico) + ( dist( C_i, C_ultimo)/velocidade_veiculo ) )
        # C_i(folga_inicio) < 0 -> Tempo ultrapassa o inicio da janela (Respeita janela)
        # C_i(folga_inicio) = 0 -> Tempo igual ao inicio da janela (Respeita Janela)
        # C_i(folga_inicio) > 0 -> Tempo abaixo do inicio da janela (Não respeita janela)

        ###EQUACAO PARA CALCULAR SE HA FOLGA NO FIM DA JANELA
        # C_i(folga_fim) = ( tempo_acumulado + C_ultimo(tempo_servico) + ( dist( C_i, C_ultimo)/velocidade_veiculo ) ) - C_i(janela_fim)
        # C_i(folga_fim) < 0 -> Tempo abaixo do fim da janela (Respeita janela)
        # C_i(folga_fim) = 0 -> Tempo igual ao fim da janela (Respeita Janela)
        # C_i(folga_fim) > 0 -> Tempo ultrapassa o fim da janela (Não respeita janela)

        ###VARIAVEIS
        # C_i = i-ésimo cliente pertencente aos clientes nao atendidos
        # C_ultimo = Ultimo cliente atendido pela rota ( a partir dele que sera feiro a ordenação das janelas)
        # tempo_acumulado = Tempo acumulado pela rota; Tempo corrente
        # velocidade_veiculo = velocidade do veiculo por unidade de distancia

        #ultimo cliente
        C_ultimo = ultimo_cliente_rota

        #Listas auxiliares para ordenação
        L_1 = []
        L_2 = []
        L_3 = []
        L_4 = []


        for C_i in clientes_nao_atendidos:

            #Obtendo janela de inicio de fim dos clientes
            janela_inicio = C_i.get_janela_inicio()
            janela_fim = C_i.get_janela_fim()

            #Calculo das folgas
            folga_inicio = janela_inicio - (  tempo_acumulado + C_ultimo.get_tempo_de_servico() + (C_i.calcula_distancia_clientes(C_ultimo)/velocidade_veiculo)  )
            folga_fim = (  tempo_acumulado + C_ultimo.get_tempo_de_servico() + (C_i.calcula_distancia_clientes(C_ultimo)/velocidade_veiculo)  ) - janela_fim


            #itens são armazenados nas lista como tuplas (Cleinte, folga_inicio, folga_fim)
            if( folga_inicio <= 0 and folga_fim <=0):# C_i respeita as duas janelas
                tupla = (C_i, folga_inicio, folga_fim)
                L_1.append(tupla)

            elif (folga_inicio <= 0): #C_i respeita somente a janela de inicio
                tupla = (C_i, folga_inicio, folga_fim)
                L_2.append(tupla)

            elif (folga_fim <= 0): #C_i respeita somente a janela de termino
                tupla = (C_i, folga_inicio, folga_fim)
                L_3.append(tupla)

            else: #C_i não respeita nenhuma janela
                tupla = (C_i, folga_inicio, folga_fim)
                L_4.append(tupla)



        #ordenado listas onde os primeiros elementos das listas serao os mais proximos das janelas
        #L_1 não é ordenado pois obedecem as janelas
        L_2.sort(key=lambda x: x[1]) #ordena a lista pela folga_inicio
        L_3.sort(key=lambda x: x[2]) #ordena a lista pela folga_fim
        L_4.sort(key=lambda x: x[1]+x[2]) #ordena a lis pela folga_inicio + folga_fim

        #adicionando na lista final respeitando a ordem
        L= []
        L_1 = [ tupla[0] for tupla in L_1 ] #Criando um nova lista removendo a tupla e mantendo só os clientes
        L.extend(L_1)
        L_2 = [ tupla[0] for tupla in L_2 ]  # Criando um nova lista removendo a tupla e mantendo só os clientes
        L.extend(L_2)
        L_3 = [ tupla[0] for tupla in L_3 ]  # Criando um nova lista removendo a tupla e mantendo só os clientes
        L.extend(L_3)
        L_4 = [ tupla[0] for tupla in L_4 ]  # Criando um nova lista removendo a tupla e mantendo só os clientes
        return L

    def criando_solucao_fixa(self):

        clientes_nao_atendidos = list(self.get_dados_cliente()) #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos

        cliente_origem = clientes_nao_atendidos.pop(0) #Retira o primeiro cliente(origem de destribuição) da lista de clientes nao atendidos

        #random.shuffle(clientes_nao_atendidos) #Embaralha todos os clientes atendidos para criar ordem aleatoria de adição

        solucao = [] #armazena a solucao

        capacidade_veiculo = self.get_capacidade_veiculo() #capacidade do veiculo(frota homogenea)

        #-------------Enquanto houver clientes a serem atendidos------------#
        while(len(clientes_nao_atendidos) > 0):

            rota = [] #Rota atribuida ao veiculo. A cada iteração o veiculo muda e rota começa vazia
            demanda_rota = 0 #Calcula demanda da rota

            #Toda rota começa da origem
            rota.append(cliente_origem)
            demanda_rota += cliente_origem.get_demanda() #Origem não possui demanda então continua em 0

            # print(clientes_nao_atendidos) #DEBUG
            # print(capacidade_veiculo) #DEGUG
            # print(cliente_origem) #DEBUG


            #percorre todos os cliente nao atendidos enquanto a demanda da rota não for atendida
            i = 0
            while( i < len(clientes_nao_atendidos) ):

                cliente = clientes_nao_atendidos[i] #Varivel que recebe o cliente da iteração
                demanda_cliente = cliente.get_demanda() #Demanda do cliente da iteração

                #verifica se a adição do cliente da iteração irá exceder a capacidade maxima do veiculo
                if(demanda_rota + demanda_cliente <= capacidade_veiculo):

                    #adiciona o cliente a rota do veiculo
                    rota.append(cliente)
                    demanda_rota += demanda_cliente

                    #remove o cliente adicionado a rota da lista de clientes nao atendidos
                    clientes_nao_atendidos.remove(cliente)
                    #Decrementa o iterador toda vez que um cliente é retirado da lista (evita que algum cliente seja pulado)
                    i -= 1
                else:
                    break

                #Se a demanda da rota ja atingiu a capacidade maxima do veiculo sai do loop
                if(demanda_rota == capacidade_veiculo):
                    break


                i += 1 # incrementa o iterador


            rota.append(cliente_origem) #A rota termina na origem

            solucao.append(rota) #Adiciona a rota a solução


            #print('append na solucao') #DEBUG
            #print(rota) #DEBUG

        return solucao


    #[PADRÃO]
    def calcula_instantes_de_entrega_1(self, solucao):

        solucao_copia = list(solucao) #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos
        instantes_entregas_solucao = [] #armazena os instantes de entrega de toda a solução


        i_rota = 0 #Armazena a rota(veiculo) da iteração

        for i_rota in range(len(solucao)) :
            rota_clientes_nao_calculados = list(solucao[i_rota])

            instantes_entregas_rota = []  # armazena os intantes de entrega de toda a rota

            tempo_acumulado = 0  # tempo acumulado até o momento


            #Estabelecendo os primeiro clientes da rota a terem instantes acumulados
            cliente_anterior = rota_clientes_nao_calculados.pop(0)  # pegando primeiro cliente(origem) da rota da iteração e remove ele
            cliente_anterior_t_servico = cliente_anterior.get_tempo_de_servico()  # tempo de serviço do cliente da iteração
            cliente_atual = rota_clientes_nao_calculados.pop(0)  # pegando primeiro cliente(id:1) da rota da iteração e remove ele
            distancia_clientes = cliente_atual.calcula_distancia_clientes(cliente_anterior) #calcula a distancia entre os clientes

            velocidade_veiculo = self.get_velocidade_veiculo()


            ##Calcula os instantes de atendimeto de cada cliente da rota
            for i_cliente in range( len(rota_clientes_nao_calculados) ):

                # Adiciona o instante de entrega do cliente anterior
                instantes_entregas_rota.append(tempo_acumulado)

                # Calcula tempo entre cliente anterior e o atual
                tempo_entre_clientes = distancia_clientes / velocidade_veiculo

                #Calcula o tempo de espera que houve no cliente anterior se houver
                janela_inicio_cliente_anterior = cliente_anterior.get_janela_inicio()
                tempo_espera = 0 if( tempo_acumulado >= janela_inicio_cliente_anterior ) else janela_inicio_cliente_anterior - tempo_acumulado

                # Calcula o tempo acumulado entre o cliente atual e o anterior
                tempo_acumulado = tempo_acumulado + cliente_anterior_t_servico + tempo_entre_clientes + tempo_espera

                #Atualiza o cliente anterior e o proximo
                cliente_anterior = cliente_atual #Cliente atual passa a ser o anterior

                cliente_anterior_t_servico = cliente_anterior.get_tempo_de_servico() #Atualiza o temp ode serviço do cliente anterior

                cliente_atual = rota_clientes_nao_calculados.pop(0) #Cliente atual é agora o proximo cliente (primeiro da list de rota)

                distancia_clientes = cliente_atual.calcula_distancia_clientes(cliente_anterior) # Atualiza a distancia entre esses clientes




            instantes_entregas_rota.append(tempo_acumulado) #adiciona o instante de entreg do ultimo cliente da rota


            ##Calcula e adiciona instante do ultimo cliente (origem)
            tempo_entre_clientes = distancia_clientes / velocidade_veiculo

            # Calcula o tempo de espera que houve no cliente anterior se houver
            janela_inicio_cliente_anterior = cliente_anterior.get_janela_inicio()
            tempo_espera = 0 if (
                        tempo_acumulado >= janela_inicio_cliente_anterior) else janela_inicio_cliente_anterior - tempo_acumulado

            # Calcula o tempo acumulado entre o cliente atual e o anterior
            tempo_acumulado = tempo_acumulado + cliente_anterior_t_servico + tempo_entre_clientes + tempo_espera

            instantes_entregas_rota.append(tempo_acumulado)  # adiciona o instante de entreg do ultimo cliente da rota



            # print(instantes_entregas_rota) #DEBUG
            instantes_entregas_solucao.append(instantes_entregas_rota) #Adiciona os instantes da rota aos instantes da solução



        return instantes_entregas_solucao

    #Se o veiculo chega antes da janela de tempo de um cliente ele espera ate o inicio
    #e para os demais clientes ele ignora as janelas e atende no momento da chegada
    def calcula_instantes_de_entrega_2(self, solucao):
        # !!!!!!! PRIMEIRO INSTATE DA ROTA É IGUAL A JANELA DE TEMPO DO PRIMEIRO CLIENTE

        solucao_copia = list(solucao) #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos




        instantes_entregas_solucao = [] #armazena os instantes de entrega de toda a solução


        #i_rota = 0 #Armazena a rota(veiculo) da iteração

        for i_rota in range(len(solucao)) :
            rota_clientes_nao_calculados = list(solucao[i_rota])

            instantes_entregas_rota = []  # armazena os intantes de entrega de toda a rota

            tempo_acumulado = 0  # tempo acumulado até o momento

            tempo_espera = 0 #Caso um veiculo chege antes do inicio da janela de tempo de um cliente sua janela de tempo é cosiderada no atendimento do seus sucessor


            #Estabelecendo os primeiro clientes da rota a tere instantes acumulados
            cliente_anterior = rota_clientes_nao_calculados.pop(0)  # pegando primeiro cliente(origem) da rota da iteração e remove ele
            cliente_anterior_t_servico = cliente_anterior.get_tempo_de_servico()  # tempo de serviço do cliente da iteração

            cliente_atual = rota_clientes_nao_calculados.pop(0)  # pegando primeiro cliente(id:1) da rota da iteração e remove ele

            distancia_clientes = cliente_atual.calcula_distancia_clientes(cliente_anterior) #calcula a distancia entre os clientes

            velocidade_veiculo = self.get_velocidade_veiculo()



            ##Calcula os instantes de atendimeto de cada cliente da rota
            for i_cliente in range( len(rota_clientes_nao_calculados) ):


                # Adiciona o instante de entrega do cliente anterior
                instantes_entregas_rota.append(tempo_acumulado)

                # Calcula tempo entre cliente anterior e o atual (CONVERTE VELOCIDADE DE KM/H PARA M/S)
                tempo_entre_clientes = distancia_clientes / (velocidade_veiculo)

                #Calcula o tempo de espera que houve no cliente anterior se houver
                janela_inicio_cliente_anterior = cliente_anterior.get_janela_inicio()
                tempo_espera = 0 if( tempo_acumulado >= janela_inicio_cliente_anterior ) else janela_inicio_cliente_anterior - tempo_acumulado

                if(cliente_anterior.get_indice() == 0):
                    tempo_acumulado += cliente_atual.get_janela_inicio()
                else:
                    # Calcula o tempo acumulado entre o cliente atual e o anterior
                    tempo_acumulado = tempo_acumulado + cliente_anterior_t_servico + tempo_entre_clientes


                #Atualiza o cliente anterior e o proximo
                cliente_anterior = cliente_atual #Cliente atual passa a ser o anterior

                cliente_anterior_t_servico = cliente_anterior.get_tempo_de_servico() #Atualiza o temp ode serviço do cliente anterior

                cliente_atual = rota_clientes_nao_calculados.pop(0) #Cliente atual é agora o proximo cliente (primeiro da list de rota)

                distancia_clientes = cliente_atual.calcula_distancia_clientes(cliente_anterior) # Atualiza a distancia entre esses clientes




            instantes_entregas_rota.append(tempo_acumulado) #adiciona o instante de entreg do ultimo cliente da rota


            ##Calcula e adiciona instante do ultimo cliente (origem)
            tempo_entre_clientes = distancia_clientes / velocidade_veiculo  # Calcula tempo entre cliente anterior e o atual

            tempo_acumulado = tempo_acumulado + cliente_anterior_t_servico + tempo_entre_clientes  # Calcula o tempo acumulado entre o cliente atual e o anterior

            instantes_entregas_rota.append(tempo_acumulado)  # adiciona o instante de entreg do ultimo cliente da rota



            # print(instantes_entregas_rota) #DEBUG
            instantes_entregas_solucao.append(instantes_entregas_rota) #Adiciona os instantes da rota aos instantes da solução


        # print(instantes_entregas_solucao); #DEBUG

        return instantes_entregas_solucao








        #print(clientes_rota);

    #Se um veiculo chega antes ele pode atender o cliente imediatamente
    def calcula_instantes_de_entrega_3(self, solucao):
        # !!!!!!! PRIMEIRO INSTANTE DA ROTA É IGUAL A JANELA DE TEMPO DO PRIMEIRO CLIENTE

        solucao_copia = list(solucao) #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos




        instantes_entregas_solucao = [] #armazena os instantes de entrega de toda a solução


        #i_rota = 0 #Armazena a rota(veiculo) da iteração

        for i_rota in range(len(solucao)) :
            rota_clientes_nao_calculados = list(solucao[i_rota])

            instantes_entregas_rota = []  # armazena os intantes de entrega de toda a rota

            tempo_acumulado = 0  # tempo acumulado até o momento

            tempo_espera = 0 #Caso um veiculo chege antes do inicio da janela de tempo de um cliente sua janela de tempo é cosiderada no atendimento do seus sucessor


            #Estabelecendo os primeiro clientes da rota a tere instantes acumulados
            cliente_anterior = rota_clientes_nao_calculados.pop(0)  # pegando primeiro cliente(origem) da rota da iteração e remove ele
            cliente_anterior_t_servico = cliente_anterior.get_tempo_de_servico()  # tempo de serviço do cliente da iteração

            cliente_atual = rota_clientes_nao_calculados.pop(0)  # pegando primeiro cliente(id:1) da rota da iteração e remove ele

            distancia_clientes = cliente_atual.calcula_distancia_clientes(cliente_anterior) #calcula a distancia entre os clientes

            velocidade_veiculo = self.get_velocidade_veiculo()


            ##Calcula os instantes de atendimeto de cada cliente da rota
            for i_cliente in range( len(rota_clientes_nao_calculados) ):


                # Adiciona o instante de entrega do cliente anterior
                instantes_entregas_rota.append(tempo_acumulado)

                # Calcula tempo entre cliente anterior e o atual (CONVERTE VELOCIDADE DE KM/H PARA M/S)
                tempo_entre_clientes = distancia_clientes / (velocidade_veiculo)

                #Calcula o tempo de espera que houve no cliente anterior se houver
                janela_inicio_cliente_anterior = cliente_anterior.get_janela_inicio()
                tempo_espera = 0 if( tempo_acumulado >= janela_inicio_cliente_anterior ) else janela_inicio_cliente_anterior - tempo_acumulado

                # Calcula o tempo acumulado entre o cliente atual e o anterior
                tempo_acumulado = tempo_acumulado + cliente_anterior_t_servico + tempo_entre_clientes

                #Atualiza o cliente anterior e o proximo
                cliente_anterior = cliente_atual #Cliente atual passa a ser o anterior

                cliente_anterior_t_servico = cliente_anterior.get_tempo_de_servico() #Atualiza o temp ode serviço do cliente anterior

                cliente_atual = rota_clientes_nao_calculados.pop(0) #Cliente atual é agora o proximo cliente (primeiro da list de rota)

                distancia_clientes = cliente_atual.calcula_distancia_clientes(cliente_anterior) # Atualiza a distancia entre esses clientes




            instantes_entregas_rota.append(tempo_acumulado) #adiciona o instante de entreg do ultimo cliente da rota


            ##Calcula e adiciona instante do ultimo cliente (origem)
            tempo_entre_clientes = distancia_clientes / velocidade_veiculo  # Calcula tempo entre cliente anterior e o atual

            tempo_acumulado = tempo_acumulado + cliente_anterior_t_servico + tempo_entre_clientes  # Calcula o tempo acumulado entre o cliente atual e o anterior

            instantes_entregas_rota.append(tempo_acumulado)  # adiciona o instante de entreg do ultimo cliente da rota



            # print(instantes_entregas_rota) #DEBUG
            instantes_entregas_solucao.append(instantes_entregas_rota) #Adiciona os instantes da rota aos instantes da solução


        # print(instantes_entregas_solucao); #DEBUG

        return instantes_entregas_solucao



    # #Calcula a função objetivo 1 para uma dada solução ( utiliza-se de seus instantes de entrega )
    # def func_obj1_alt(self, solucao, instantes):
    #     solucao_cpy =  list(solucao) # copia da solução
    #
    #     T = self.get_ciclo_de_vida_produto()
    #
    #     t1=0
    #     t2=0
    #     t3=0
    #
    #
    #     #-------Soma do custo por unidade percorrida do veiculo-------#
    #     sum_1 = 0.0 #custo dos veiculos dados os km
    #     custo_por_unidade = self.get_custo_tranporte_unidade_distancia()  # Custo por unidade percorrida do veiculo
    #     for i in range(len(solucao_cpy)):
    #         rota= solucao[i]
    #         for j in range(len(rota) - 1):
    #             cliente_atual = rota[j]
    #             cliente_proximo = rota[j+1]
    #
    #             sum_1 += cliente_atual.calcula_distancia_clientes(cliente_proximo) * custo_por_unidade
    #     #print(f"Soma Custo transporte: {sum_1}") #DEBUG
    #
    #
    #     # -------Soma do custo pelo numero de veiculos alocados-------#
    #     sum_2 = 0.0 #custo dado o numero de veiculos da solucao
    #     n_veiculos = len(solucao)
    #     custo_por_veiculo = self.get_custo_veiculo()
    #     sum_2 = n_veiculos * custo_por_veiculo
    #     #print(f"Soma numero veiculos: {sum_2}")  # DEBUG
    #
    #
    #     # -------Soma do custo pelo adiantamento e ultrapassagem das janelas-------#
    #     sum_3 = 0.0 #Soma referente ao adiantamento das janelas
    #     w1 = self.get_w1() #Coeficiente de adiantamento
    #
    #     sum_4 = 0.0  # Soma referente a ultrapassagem das janelas
    #     w2 = self.get_w2()  # Coeficiente de ultrapassagem
    #
    #     #Percorre clientes da solução
    #     for i in range(len(solucao_cpy)):
    #         rota = solucao_cpy[i]
    #         for j in range(len(rota) - 1): #Não considera a janela de tempo quando o veiculo volta a origem
    #             cliente = rota[j]
    #             cliente_janela_inicio = cliente.get_janela_inicio()
    #             cliente_janela_fim = cliente.get_janela_fim()
    #             cliente_instante_entrega = instantes[i][j]
    #
    #             sum_3 += 0.0 if (cliente_instante_entrega >= cliente_janela_inicio) else cliente_janela_inicio - cliente_instante_entrega #Só adiciona se houver um adiantamento
    #             sum_4 += 0.0 if (cliente_janela_fim >= cliente_instante_entrega) else cliente_instante_entrega - cliente_janela_fim  # Só adiciona se houver uma ultrapassagem
    #
    #             t1 += 0.0 if (cliente_instante_entrega >= cliente_janela_inicio) else 1
    #
    #             t2 += 0.0 if (cliente_janela_fim >= cliente_instante_entrega) else 1
    #
    #
    #
    #     #aplicando coeficientes
    #     sum_3 = (sum_3/1) * w1
    #     sum_4 = (sum_4/1) * w2
    #     #print(f"Soma Adianto(W1): {sum_3}")  # DEBUG
    #     #print(f"Soma Atraso(W2): {sum_4}")  # DEBUG
    #     #print(f"t1: {t1}")
    #     #print(f"t2: {t2}")
    #
    #
    #     # -------Soma do custo pelos danos aos produtos no instante de entrega-------#
    #     sum_5 = 0 #Armazena a soma de danos ao produto
    #     w3 = self.get_w3()  # Coeficiente dos danos
    #
    #     # Percorre clientes da solução
    #     for i in range(len(solucao_cpy)):
    #         rota = solucao_cpy[i]
    #         for j in range(len(rota) - 1):
    #             cliente = rota[j]
    #             cliente_demanda = cliente.get_demanda()
    #             cliente_instante_entrega = max(instantes[i][j],cliente.get_janela_inicio())
    #
    #             sum_5 += self.phi(cliente_instante_entrega,T)*cliente_demanda
    #
    #
    #     sum_5 = sum_5*w3
    #     #print(f"Soma danos(W3):  {sum_5}")  # DEBUG
    #
    #     return sum_1+sum_2+sum_3+sum_4+sum_5
    #
    #
    #
    #
    #
    #
    #
    #     ###################OBJ2
    #
    # # Calcula a função objetivo 1 para uma dada solução ( utiliza-se de seus instantes de entrega )
    # def func_obj2_alt(self, solucao, instantes  ):
    #
    #     T = self.get_ciclo_de_vida_produto()
    #     dados_cliente = self.__dados_cliente
    #
    #     numerador = 0.0
    #     denominador = 0.0
    #
    #     for i in range(len(solucao)):
    #         rota = solucao[i]
    #         rota_instantes = instantes[i]
    #
    #         for j in range(len(rota)):
    #             cliente = rota[j]
    #
    #             #instante de atendimento é igual a janela de tempo em caso de adiantamento
    #             cliente_ti = max(rota_instantes[j],cliente.get_janela_inicio())
    #
    #             numerador += self.beta(cliente_ti,T) * cliente.get_demanda()
    #             #print(f"Sum Freshness: {numerador}")
    #             denominador += cliente.get_demanda()
    #
    #
    #     obj2 = numerador/denominador
    #     return obj2
