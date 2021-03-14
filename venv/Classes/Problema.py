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

    # cluster = Cluster()


    #-----------SETTERS-----------#

    def set_numero_max_veiculos(self, numero_max_veiculos):
        # verifica tipo
        if (type(numero_max_veiculos) is int):
            self.__numero_max_veiculos = numero_max_veiculos
            return True;
        else:
            return False;

    def set_capacidade_veiculo(self, capacidade_veiculo):
        # verifica tipo
        if (type(capacidade_veiculo) is int):
            self.__capacidade_veiculo = capacidade_veiculo
            return True;
        else:
            return False;

    def set_velocidade_veiculo (self, velocidade_veiculo ):
        # verifica tipo
        if (type(velocidade_veiculo) is float):
            self.__velocidade_veiculo  = velocidade_veiculo
            return True;
        else:
            return False;

    def set_custo_tranporte_unidade_distancia (self, custo_tranporte_unidade_distancia ):
        #verifica tipo
        if (type(custo_tranporte_unidade_distancia ) is float ):
            self.__custo_tranporte_unidade_distancia  = custo_tranporte_unidade_distancia
            return True;
        else:
            return False;

    def set_custo_veiculo(self, custo_veiculo):
        # verifica tipo
        if (type(custo_veiculo) is float):
            self.__custo_veiculo = custo_veiculo
            return True;
        else:
            return False;

    def set_tempo_servico(self, tempo_servico):
        # verifica tipo
        if (type(tempo_servico) is int):
            self.__tempo_servico = tempo_servico
            return True;
        else:
            return False;

    def set_numero_clientes(self, numero_clientes):
        # verifica tipo
        if (type(numero_clientes) is int):
            self.__numero_clientes = numero_clientes
            return True;
        else:
            return False;

    def set_dados_cliente(self, dados_cliente):
        # verifica tipo
        if (type(dados_cliente) is list):
            self.__dados_cliente = dados_cliente
            return True;
        else:
            return False;

    def set_qualidade_produto(self, qualidade_produto):
        # verifica tipo
        if (type(qualidade_produto) is float):
            self.__qualidade_produto = qualidade_produto
            return True;
        else:
            return False;

    def set_ciclo_de_vida_produto(self, ciclo_de_vida_produto):
        # verifica tipo
        if (type(ciclo_de_vida_produto) is float):
            self.__ciclo_de_vida_produto = ciclo_de_vida_produto
            return True;
        else:
            return False;

    def set_w1(self, w1):
        # verifica tipo
        if (type(w1) is int):
            self.__w1 = w1
            return True;
        else:
            return False;

    def set_w2(self, w2):
        # verifica tipo
        if (type(w2) is int):
            self.__w2 = w2
            return True;
        else:
            return False;

    def set_w3(self, w3):
        # verifica tipo
        if (type(w3) is int):
            self.__w3 = w3
            return True;
        else:
            return False;

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



    #-----------DEBUG-----------#

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


    #Uma vez que se setamos o tempo de servico temos que atualizar eles nos dados dos clientes
    def att_tempo_servico(self):
        clientes = self.get_dados_cliente()
        tempo_de_servico = self.get_tempo_servico()

        for cliente in clientes:
            t_servico = tempo_de_servico  if cliente.get_tempo_de_servico() > 0 else 0 #Manter a origem sem tempo de servico
            cliente.set_tempo_de_servico(t_servico)



    #Criando Solução Aleatoria respeitando as Demandas
    def criando_solucao_aleatoria(self):
        ##!!!!!!NÂO CONSIDERA DISTÂNCIAS NA GERAÇÃO
        ##!!!!!!!NÃO CONSIDERA JANELAS DE TEMPO NA GERAÇÃO

        clientes_nao_atendidos = list(self.get_dados_cliente()); #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos

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
            demanda_rota += cliente_origem.get_demanda(); #Origem não possui demanda então continua em 0

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

    #Retorna uma lista de lista com os instantes em que os clientes foram atendidos em um dada solucao
        #Um mesmo posição tanto nos instantes quanto na solução correspondem a um mesmo cliente
    def calcula_instantes_de_entrega(self, solucao):
        # !!!!!!! PRIMEIRO INSTATE DA ROTA É IGUAL A JANELA DE TEMPO DO PRIMEIRO CLIENTE

        solucao_copia = list(solucao); #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos




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

            velocidade_veiculo = self.get_velocidade_veiculo();


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








        #print(clientes_rota);


    ###################OBJ1

    def phi(self, instante):
        T = 720
        return np.exp(  ( (np.log(2)/T)*instante )  ) - 1

    def beta(self, instante):
        return 1 - (self.phi(instante))

    #Calcula a função objetivo 1 para uma dada solução ( utiliza-se de seus instantes de entrega )
    def func_obj1(self, solucao, instantes):
        solucao_cpy =  list(solucao) # copia da solução



        #-------Soma do custo por unidade percorrida do veiculo-------#
        sum_1 = 0 #custo dos veiculos dados os km
        custo_por_unidade = self.get_custo_tranporte_unidade_distancia()  # Custo por unidade percorrida do veiculo
        for i in range(len(solucao_cpy)):

            rota= solucao[i]
            #print()

            for j in range(len(rota) - 1):


                cliente_atual = rota[j]
                cliente_proximo = rota[j+1]

                sum_1 += cliente_atual.calcula_distancia_clientes(cliente_proximo) * custo_por_unidade

        # -------Soma do custo pelo numero de veiculos alocados-------#
        sum_2 = 0 #custo dado o numero de veiculos da solucao
        n_veiculos = len(solucao)
        custo_por_veiculo = self.get_custo_veiculo()
        sum_2 = n_veiculos * custo_por_veiculo


        # -------Soma do custo pelo adiantamento e ultrapassagem das janelas-------#
        sum_3 = 0 #Soma referente ao adiantamento das janelas
        w1 = self.get_w1() #Coeficiente de adiantamento

        sum_4 = 0  # Soma referente a ultrapassagem das janelas
        w2 = self.get_w2()  # Coeficiente de ultrapassagem

        #Percorre clientes da solução
        for i in range(len(solucao_cpy)):
            rota = solucao_cpy[i]
            for j in range(len(rota) - 1): #Não considera a janela de tempo quando o veiculo volta a origem
                cliente = rota[j]
                cliente_janela_inicio = cliente.get_janela_inicio()
                cliente_janela_fim = cliente.get_janela_fim()
                cliente_instante_entrega = instantes[i][j]

                sum_3 += 0 if (cliente_instante_entrega >= cliente_janela_inicio) else cliente_janela_inicio - cliente_instante_entrega #Só adiciona se houver um adiantamento
                sum_4 += 0 if (cliente_janela_fim >= cliente_instante_entrega) else cliente_instante_entrega - cliente_janela_fim  # Só adiciona se houver uma ultrapassagem

        #aplicando coeficientes
        sum_3 = sum_3 * w1
        sum_4 = sum_4 * w2



        # -------Soma do custo pelos danos aos produtos no instante de entrega-------#
        sum_5 = 0 #Armazena a soma de danos ao produto
        w3 = self.get_w3()  # Coeficiente dos danos

        # Percorre clientes da solução
        for i in range(len(solucao_cpy)):
            rota = solucao_cpy[i]
            for j in range(len(rota) - 1):
                cliente = rota[j]
                cliente_demanda = cliente.get_demanda()
                cliente_instante_entrega = instantes[i][j]

                sum_5 += self.phi(cliente_instante_entrega)*cliente_demanda

        sum_5 = sum_5*w3

        return sum_1+sum_2+sum_3+sum_4+sum_5







        ###################OBJ2 FALTA IMPLETEMNTAR


    def func_obj2(self, solucao, instantes):


        numerador = 0.0
        denominador = 0.0

        for i in range(len(solucao)):
            rota = solucao[i]
            rota_instantes = instantes[i]

            for j in range(len(rota)):
                cliente = rota[j]
                cliente_ti = rota_instantes[j]

                numerador += self.beta(cliente_ti) * cliente.get_demanda()
                #print(f"Sum Freshness: {numerador}")
                denominador += cliente.get_demanda()


        obj2 = numerador/denominador
        return obj2





   ##########################################################
    def criando_solucao_aleatoria_2(self):
        ##!!!!!!!!!!!PROBLEMA: Não Considerao numero maximo de veiculos
        ##!!!!!!!!!!!PROBLEMA: Não Cosidera a qualidade minima
        ##!!!!!!!!!!!PROBLEMA: Não considera as Janelas de Tempo

        clientes_nao_atendidos = list(self.get_dados_cliente()); #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos

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
            demanda_rota += cliente_origem.get_demanda();

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

        clientes_nao_atendidos = list(clientes); #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos

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
            demanda_rota += cliente_origem.get_demanda();

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
        L_1 #não é ordenado pois obedecem as janelas
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

        clientes_nao_atendidos = list(self.get_dados_cliente()); #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos

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
            demanda_rota += cliente_origem.get_demanda(); #Origem não possui demanda então continua em 0

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
                    break;

                #Se a demanda da rota ja atingiu a capacidade maxima do veiculo sai do loop
                if(demanda_rota == capacidade_veiculo):
                    break


                i += 1 # incrementa o iterador


            rota.append(cliente_origem) #A rota termina na origem

            solucao.append(rota) #Adiciona a rota a solução


            #print('append na solucao') #DEBUG
            #print(rota) #DEBUG

        return solucao

    def calcula_instantes_de_entrega_2(self, solucao):
        # !!!!!!! PRIMEIRO INSTATE DA ROTA É IGUAL A JANELA DE TEMPO DO PRIMEIRO CLIENTE

        solucao_copia = list(solucao); #cria uma copia da lista de clientes, com finalidade de armazenar os clientes nao atendidos




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

            velocidade_veiculo = self.get_velocidade_veiculo();



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
