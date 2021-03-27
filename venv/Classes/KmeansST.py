import numpy as np
from sklearn.cluster import KMeans
from Classes.Cliente import Cliente

class KmeansST:

    #Parametros para Distancia Espaco Temporal
    __A = 0.0  # [float] Representa a janela de maior tamanho dos clientes
    __alpha1 = 0.0  # [float] Coeficiente que atribui peso para a distância espacial
    __alpha2 = 0.0  # [float] Coeficiente que atribui peso para a distância temporal
    __max_temporal = 0.0  # [float] Maior distancia temporal na matriz de distancia
    __min_temporal = 0.0  # [float] Menor distancia temporal na matriz de distancia
    __max_espacial = 0.0  # [float] Maior distancia espacial na matriz de distancia
    __min_espacial = 0.0  # [float] Menor distancia espacial na matriz de distancia
    __velocidade_veiculo = 0.0  # [float] Velocidade do veiculo


    #Parametros para distancia Temporal
    __k1 = 0.0  # [float] parametro usado para o calculo do tempo salvo quando medimos o tempo entre dois clientes
    __k2 = 0.0  # [float] parametro usado para o calculo do tempo salvo quando medimos o tempo entre dois clientes
    __k3 = 0.0  # [float] parametro usado para o calculo do tempo salvo quando medimos o tempo entre dois clientes


    #Esturas de Armazenamento
    __clusters = []  # [list of list] Armazena todos os clusters so problema.
    __matriz_distancias_S = []  # [list of list] Armazena as distancias espaciais entre todos os cliente
    __matriz_distancias_T = []  # [list of list] Armazena as distancias temporais entre todos os cliente
    __matriz_distancias_ST = []  # [list of list] Armazena as distancias espaciais e temporais entre todos os cliente
    __dados_clientes = []  # [list of list] lista que armazena os dados de cada cliente i como vetor e j um atributo desse cliente




    #-----------CONSTRUTOR------------#

    def __init__(self, k1=0.0, k2=0.0, k3=0.0, alpha1=0.0, alpha2=0.0 , velocidade_veiculo = 0.0, dados_clientes = []):
        self.set_k1(k1)
        self.set_k2(k2)
        self.set_k3(k3)
        self.set_alpha1(alpha1)
        self.set_alpha2(alpha2)
        self.set_velocidade_veiculo(velocidade_veiculo)
        self.set_dados_clientes(dados_clientes)
        self.calcula_maior_janela()



    # -----------SETTERS-----------#

    def set_k1(self, k1):
        # verifica tipo
        if (type(k1) is float):
            self.__k1 = k1
            return True;
        else:
            return False;

    def set_k2(self, k2):
        # verifica tipo
        if (type(k2) is float):
            self.__k2 = k2
            return True;
        else:
            return False;

    def set_k3(self, k3):
        # verifica tipo
        if (type(k3) is float):
            self.__k3 = k3
            return True;
        else:
            return False;

    def set_alpha1(self, alpha1):
        # verifica tipo
        if (type(alpha1) is float):
            self.__alpha1 = alpha1
            return True;
        else:
            return False;

    def set_alpha2(self, alpha2):
        # verifica tipo
        if (type(alpha2) is float):
            self.__alpha2 = alpha2
            return True;
        else:
            return False;

    def set_velocidade_veiculo(self, velocidade_veiculo):
        # verifica tipo
        if (type(velocidade_veiculo) is float):
            self.__velocidade_veiculo = velocidade_veiculo
            return True;
        else:
            return False;

    def set_dados_clientes(self, dados_clientes):
        # verifica tipo
        if (type(dados_clientes) is list):
            self.__dados_clientes = dados_clientes
            return True;
        else:
            return False;


    #-----------GETTERS-----------#

    def get_k1(self):
        return self.__k1

    def get_k2(self):
        return self.__k2

    def get_k3(self):
        return self.__k3

    def get_alpha1(self):
        return self.__alpha1

    def get_alpha2(self):
        return self.__alpha2

    def get_clusters(self):
        return self.__clusters

    def get_matriz_distancias_S(self):
        return self.__matriz_distancias_S

    def get_matriz_distancias_T(self):
        return self.__matriz_distancias_T

    def get_matriz_distancias_ST(self):
        return self.__matriz_distancias_ST

    def get_velocidade_veiculo(self):
        return self.__velocidade_veiculo

    def get_dados_clientes(self):
        return self.__dados_clientes

    # -----------METODOS-----------#

    def calcular_distancias(self):

        #Calculo das distancias temporal e espacial
        self.calcular_distancias_temporal_e_espacial()

        #Calculo das distancias espaço temporal
        self.calcular_distancia_espaço_temporal()

    def calcular_distancias_temporal_e_espacial(self):
        clientes = self.get_dados_clientes()
        linha_espacial = []
        linha_temporal = []

        #Percorre todos os clientes (i)
        for cliente_i in clientes:
            coluna_espacial = []
            coluna_temporal = []

            #Percorre todos os clintes (j)
            for cliente_j in clientes:
                # Distancia Espacial
                distancia_espacial = self.distancia_espacial(cliente_i, cliente_j) if (cliente_i != cliente_j) else 0.0
                coluna_espacial.append(distancia_espacial)

                # Distancia Temporal
                distancia_temporal = self.distancia_temporal(cliente_i, cliente_j) if (cliente_i != cliente_j) else 0.0
                coluna_temporal.append(distancia_temporal)
                #print(distancia_temporal, end=" ")  # DEBUG

            linha_espacial.append(coluna_espacial)
            linha_temporal.append(coluna_temporal)
            #print()  # DEBUG



        #A distância temporal deve ser espelhada ou seja distancia de i para j é iqual a distancia de j para i
        #Essa distancia é então escolhida como o valor máximo entre i para j e j para i
        for i in range(len(linha_temporal)):
            for j in range(len(linha_temporal)):
                linha_temporal[i][j] = max(linha_temporal[i][j], linha_temporal[j][i])


        #Atribuindo matrizes de distância
        self.__matriz_distancias_S = linha_espacial
        self.__matriz_distancias_T = linha_temporal

    def calcular_distancia_espaço_temporal(self):

        matriz_S = self.get_matriz_distancias_S()
        matriz_T = self.get_matriz_distancias_T()
        tam_matriz = len(matriz_S)

        self.calcula_max_temporal()
        self.calcula_min_temporal()
        self.calcula_max_espacial()
        self.calcula_min_espacial()
        max_temporal = self.__max_temporal
        min_temporal = self.__min_temporal
        max_espacial = self.__max_espacial
        min_espacial = self.__min_espacial

        alpha1 = self.__alpha1
        alpha2 = self.__alpha2

        #print(f"max_t: {max_temporal}  min_t: {min_temporal}, max_s: {max_espacial}, min_s: {min_espacial}")  # DEBBUG

        linhas_espaco_temporal = []
        for i in range(tam_matriz):
            colunas_espaco_temporal = []
            for j in range(tam_matriz):

                distancia_espacial = matriz_S[i][j]
                distancia_temporal = matriz_T[i][j]
                distancia_espaco_temporal = 0.0 if(i == j) else self.distancia_espaco_temporal(
                                                                distancia_espacial, distancia_temporal,
                                                                alpha1,alpha2, max_espacial,min_espacial,
                                                                max_temporal,min_temporal
                                                                )

                colunas_espaco_temporal.append(distancia_espaco_temporal)

            linhas_espaco_temporal.append(colunas_espaco_temporal)

        self.__matriz_distancias_ST = linhas_espaco_temporal



    #---------DISTANCIA-ESPACIAL---------#
    def distancia_espacial(self, cliente_i, cliente_j):
        return cliente_i.calcula_distancia_clientes(cliente_j)

    def calcula_max_espacial(self):
        matriz_S = self.get_matriz_distancias_S()
        tam_matriz = len(matriz_S)
        maior_distancia = -1 * float("inf")
        for i in range(tam_matriz) :
            for j in range(tam_matriz):

                if( i != j and matriz_S[i][j] > maior_distancia):
                    maior_distancia = matriz_S[i][j]


        #print(maior_distancia) #DEBUG
        self.__max_espacial= maior_distancia

    def calcula_min_espacial(self):

        matriz_S = self.get_matriz_distancias_S()
        tam_matriz = len(matriz_S)
        menor_distancia = float("inf")
        for i in range(tam_matriz):
            for j in range(tam_matriz):

                if (i != j and matriz_S[i][j] < menor_distancia):
                    menor_distancia = matriz_S[i][j]

        #print(menor_distancia)  # DEBUG
        self.__min_espacial = menor_distancia



    #---------DISTANCIA-TEMPORAL---------#
    def distancia_temporal(self, cliente_i, cliente_j):

        #Parametros
        velocidade_veiculo = self.get_velocidade_veiculo()
        k1 = self.get_k1()
        k2 = self.get_k2()
        k3 = self.get_k3()
        A = self.A


        #Janela de tempo do Cliente i
        a = cliente_i.get_janela_inicio()
        b = cliente_i.get_janela_fim()
        # Janela de tempo do Cliente j
        c = cliente_j.get_janela_inicio()
        d = cliente_j.get_janela_fim()
        #Tempo de serviço cliente i
        si_cliente_i = cliente_i.get_tempo_de_servico()

        #Distancia espacial entre cliente i e j
        distancia = cliente_i.calcula_distancia_clientes(cliente_j)

        #Projeção das janelas de tempo
        a_linha = a + si_cliente_i + (distancia/velocidade_veiculo)
        b_linha = b + si_cliente_i + (distancia/velocidade_veiculo)

        #Calculo de integrais
        integral_antecipado = self.integral_antecipado(a_linha, b_linha, c, d, k1, k2)
        integral_normal = self.integral_normal(a_linha, b_linha, c, d, k1)
        integral_atrasado = self.integral_atrasado(a_linha, b_linha, c, d, k3)

        distancia_temporal = k1*A - (integral_antecipado + integral_normal + integral_atrasado)/(b_linha - a_linha)

        return distancia_temporal

    def integral_antecipado(self,a_linha, b_linha, c, d, k1, k2):

        #limite superior de integração
        t_linha = min(b_linha,c)
        integral_lim_superior = (k2*(t_linha**2))/2 + t_linha*(-(c*k1) -(c*k2) -(d*k1) )

        # limite superior de integração
        t_linha = min(a_linha, c)
        integral_lim_inferior = (k2 * (t_linha ** 2)) / 2 + t_linha * (-(c * k1) - (c * k2) - (d * k1))

        valor_integral = integral_lim_superior - integral_lim_inferior

        return valor_integral

    def integral_normal(self, a_linha, b_linha, c, d, k1):

        # limite superior de integração
        t_linha = max( min(b_linha,d), c)
        integral_lim_superior = (d*k1*t_linha) - (k1*(t_linha**2))/2

        # limite superior de integração
        t_linha = min( max(a_linha,c), d)
        integral_lim_inferior = (d*k1*t_linha) - (k1*(t_linha**2))/2

        valor_integral = integral_lim_superior - integral_lim_inferior

        return valor_integral

    def integral_atrasado(self, a_linha, b_linha, c, d, k3):

        # limite superior de integração
        t_linha = min(b_linha, d)
        integral_lim_superior = (d*k3*t_linha) - (k3*(t_linha**2))/2

        # limite superior de integração
        t_linha = max(a_linha, d)
        integral_lim_inferior = (d*k3*t_linha) - (k3*(t_linha**2))/2

        valor_integral = integral_lim_superior - integral_lim_inferior

        return valor_integral

    def calcula_maior_janela(self):
        clientes = self.get_dados_clientes()
        a = 0.0

        for cliente in clientes:
            janela_inicio = cliente.get_janela_inicio()
            janela_fim = cliente.get_janela_fim()

            if(janela_fim - janela_inicio > a):
                a = janela_fim - janela_inicio

        self.A = a

    def calcula_max_temporal(self):
        matriz_T = self.get_matriz_distancias_T()
        tam_matriz = len(matriz_T)
        maior_distancia = -1 * float("inf")
        for i in range(tam_matriz) :
            for j in range(tam_matriz):

                if( i != j and matriz_T[i][j] > maior_distancia):
                    maior_distancia = matriz_T[i][j]


        #print(maior_distancia) #DEBUG
        self.__max_temporal= maior_distancia

    def calcula_min_temporal(self):

        matriz_T = self.get_matriz_distancias_T()
        tam_matriz = len(matriz_T)
        menor_distancia = float("inf")
        for i in range(tam_matriz):
            for j in range(tam_matriz):

                if (i != j and matriz_T[i][j] < menor_distancia):
                    menor_distancia = matriz_T[i][j]

        #print(menor_distancia)  # DEBUG
        self.__min_temporal = menor_distancia



    # ---------DISTANCIA-ESPACO-TEMPORAL---------#
    def distancia_espaco_temporal(self, distancia_espacial, distancia_temporal, alpha1, alpha2, max_espacial, min_espacial, max_temporal, min_temporal):
        espacial = ( distancia_espacial-min_espacial )/( max_espacial-min_espacial )
        temporal = ( distancia_temporal-min_temporal )/( max_temporal-min_temporal )

        return alpha1*espacial + alpha2*temporal




    #--------PRINT-------#

    def print(self):
        print(f"\nk1 = {self.get_k1()}"
              f"\nk2 = {self.get_k2()}"
              f"\nk3 = {self.get_k3()}"
              f"\nalpha1 = {self.get_alpha1()}"
              f"\nalpha2 = {self.get_alpha2()}"
              f"\nclusters = {self.get_clusters()}"
              f"\nMatriz_s={self.get_matriz_distancias_S()}"
              f"\nMatriz_t = {self.get_matriz_distancias_T()}"
              f"\nMatriz_ST = {self.get_matriz_distancias_ST()}"
              f"\nvelocidade= {self.get_velocidade_veiculo()}"
              f"\ndados_clientes= {self.get_dados_clientes()}")

    def print_ST(self):
        matriz_ST = self.__matriz_distancias_ST

        l = 0
        for i in matriz_ST:
            c = 0
            for j in i:
                print(f"{round(j,2)}[{l}][{c}]", end=" ")
                c+=1
            l += 1
            print() #DEBUG
            


    def executar(self,k , n_iteracoes = -1):
        convergiu = False

        n_clientes = len(self.__dados_clientes)
        indices_clientes = [ i for i in range(1,n_clientes)]

        #print(indices_clientes) ## DEBUG
        clusters = self.gerar_centros_alatorios(indices_clientes, k)
        #print(indices_clientes) ## DEBUG
        #print(clusters) #DEBUG

        self.atribuir_clientes_cluster(indices_clientes, clusters)


        i=0
        while convergiu == False and (n_iteracoes == -1 or i < n_iteracoes):
            #print(f"in:  {clusters}") #DEBUG
            convergiu = self.recalcular_centro(clusters, convergiu)
            #print(f"out: {clusters}") #DEBUG
            self.reatribuir_clientes_cluster(clusters)
            i+=1




        #print(clusters)
        return clusters






    def gerar_centros_alatorios(self, indices, k):

        clusters = [ [] for i in range(k)]

        for i in range(k):
            indice_aleatorio = np.random.randint(low = 0 , high = len(indices))
            centro = indices.pop(indice_aleatorio)
            clusters[i].append(centro)

        return clusters

    def atribuir_clientes_cluster(self, indices_clientes, clusters ):
        for i in range(len(indices_clientes)):
            i_cliente = indices_clientes.pop(0)
            indice_clusters = self.cluster_mais_proximo(clusters, i_cliente)
            clusters[indice_clusters].append(i_cliente)

    def cluster_mais_proximo(self, clusters, indice_cliente):
        dist = self.__matriz_distancias_ST
        menor_distancia = float("inf")
        indice_mais_proximo = -1

        for i in range(len(clusters)):
            indice_centro = clusters[i][0]
            if(dist[indice_cliente][indice_centro] < menor_distancia):
                menor_distancia = dist[indice_cliente][indice_centro]
                indice_mais_proximo = i


        return indice_mais_proximo

    def recalcular_centro(self, clusters, convergiu):
        convergiu = True
        dist = self.__matriz_distancias_ST
        # percorre os clusters
        for cluster in clusters:
            #print("Cluster") #DEBUG

            min_soma = float("inf")
            min_indice = -1

            # percorre os elementos do cluster a iteração
            indice = 0  # Armazena a posicao do elemento no cluster
            for i in cluster:
                #print(f"{i} ->", end=" ") #DEBUG
                soma_distancias_i = 0  # Armazena a soma das distancias de um cliente i a todos os outros no mesmo cluster
                for j in cluster:
                    soma_distancias_i += dist[i][j]
                    #print(f"{dist[i][j]}+", end="") #DEBUG
                #print(f"= {soma_distancias_i}") #DEBUG
                # Verifica se a soma das distacias é a menor até o momento
                if (soma_distancias_i < min_soma):
                    min_soma = soma_distancias_i
                    #print(min_soma) #DEBUG
                    min_indice = indice

                indice += 1  # incrementa o indice da iteração

            # Verifica se o centro foi alterado (o centro é sempre a primeira posição '[0]')
            if (min_indice != 0):
                convergiu = False
                aux = cluster[0]
                cluster[0] = cluster[min_indice]
                cluster[min_indice] = aux


        return convergiu

    def reatribuir_clientes_cluster(self, clusters):
        indices_clientes = []
        for cluster in clusters:
            for i in range(1, len(cluster)):
                i_cliente = cluster.pop(1)
                indices_clientes.append(i_cliente)

        #print(indices_clientes)
        #print(clusters)

        for i in range(len(indices_clientes)):
            i_cliente = indices_clientes.pop(0)
            indice_clusters = self.cluster_mais_proximo(clusters, i_cliente)
            clusters[indice_clusters].append(i_cliente)
        #print(clusters) #DEBUG
        #print() #DEBUG