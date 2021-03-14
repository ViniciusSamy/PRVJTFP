import numpy as np
from Classes.Cliente import Cliente

class KmeansST:



    #Parametros para Distancia Espaco Temporal
    __A = 0.0 # [float] Representa a janela de maior tamanho dos clientes
    __alpha1 = 0.0 # [float] Coeficiente que atribui peso para a distância espacial
    __alpha2 = 0.0 # [float] Coeficiente que atribui peso para a distância temporal
    __max_temporal = 0.0 # [float] Maior distancia temporal na matriz de distancia
    __min_temporal = 0.0 # [float] Menor distancia temporal na matriz de distancia
    __max_espacial = 0.0 # [float] Maior distancia espacial na matriz de distancia
    __min_especial = 0.0 # [float] Menor distancia espacial na matriz de distancia
    __velocidade_veiculo = 0.0 # [float] Velocidade do veiculo



    #Parametros para distancia Temporal
    __k1 = 0.0 # [float] parametro usado para o calculo do tempo salvo quando medimos o tempo entre dois clientes
    __k2 = 0.0 # [float] parametro usado para o calculo do tempo salvo quando medimos o tempo entre dois clientes
    __k3 = 0.0 # [float] parametro usado para o calculo do tempo salvo quando medimos o tempo entre dois clientes



    #Esturas de Armazenamento
    __clusters = [] # [list of list] Armazena todos os clusters so problema.
    __matriz_distancias_S = [] # [list of list] Armazena as distancias espaciais entre todos os cliente
    __matriz_distancias_T = [] # [list of list] Armazena as distancias temporais entre todos os cliente
    __matriz_distancias_ST = [] # [list of list] Armazena as distancias espaciais e temporais entre todos os cliente
    __dados_clientes = [] # [list of list] lista que armazena os dados de cada cliente i como vetor e j um atributo desse cliente


    #-----------CONSTRUTOR------------#
    def __init__(self, k1=0.0, k2=0.0, k3=0.0, alpha1=0.0, alpha2=0.0 , velocidade_veiculo = 0.0, dados_clientes = []):
        self.set_k1(k1)
        self.set_k2(k2)
        self.set_k3(k3)
        self.set_alpha1(alpha1)
        self.set_alpha2(alpha2)
        self.set_velocidade_veiculo(velocidade_veiculo)
        self.set_dados_clientes(dados_clientes)



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
        clientes = self.get_dados_clientes()

        linha_espacial = []
        linha_temporal = []
        for cliente_i in clientes:
            coluna_espacial = []
            coluna_temporal = []

            for cliente_j in clientes:
                #Distancia Espacial
                distancia_espacial = self.distancia_espacial(cliente_i, cliente_j)
                coluna_espacial.append(distancia_espacial)

                #Distancia Temporal
                distancia_temporal = self.distancia_temporal(cliente_i, cliente_j)
                coluna_temporal.append(distancia_temporal)
                print(distancia_temporal, end=" ")


            linha_espacial.append(coluna_espacial)
            linha_temporal.append(coluna_temporal)
            print()

        self.__matriz_distancias_S = linha_espacial
        self.__matriz_distancias_T = linha_temporal




    def distancia_espacial(self, cliente_i, cliente_j):
        return cliente_i.calcula_distancia_clientes(cliente_j)


    def distancia_temporal(self, cliente_i, cliente_j):

        #Parametros
        velocidade_veiculo = self.get_velocidade_veiculo()
        k1 = self.get_k1()
        k2 = self.get_k2()
        k3 = self.get_k3()
        A = self.calcula_maior_janela()


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

        distancia_temporal = k1*A  - (integral_antecipado + integral_normal + integral_atrasado)/(b_linha - a_linha)

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
        A = 0.0

        for cliente in clientes:
            janela_inicio = cliente.get_janela_inicio()
            janela_fim = cliente.get_janela_fim()
            if(janela_fim - janela_inicio > A):
                A = janela_fim - janela_inicio

        return A


    def print(self):
        print(f"\nk1 = {self.get_k1()}"
              f"\nk2 = {self.get_k2()}"
              f"\nk3 = {self.get_k3()}"
              f"\nalpha1 = {self.get_alpha1()}"
              f"\nalpha2 = {self.get_alpha2()}"
              f"\nclusters = {self.get_clusters()}"
              f"\nMatriz_s= {self.get_matriz_distancias_S()}"
              f"\nMatriz_t = {self.get_matriz_distancias_T()}"
              f"\nMatriz_ST = {self.get_matriz_distancias_ST()}"
              f"\nvelocidade= {self.get_velocidade_veiculo()}"
              f"\ndados_clientes= {self.get_dados_clientes()}")
