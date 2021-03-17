#Classe para manipulação e amazenamento de cada solução
class Solucao:

    #---------INDENTIFICADOR---------#
    __id = 0 # [int] indentificador da solução

    #---------DADOS DAS ROTAS---------#
    __tamanho_rota_por_veiculo = [] # [list] Armazena o tamanho da rota(numero de clientes visitados) de cada veiculo i alocado na solução
    __numero_veiculos = 0 # [int] numero de Veiculos Alocados
    __distancia_percorrida =0.0 # [float] distancia total percorrida

    __caminho_da_solucao = []  # [list] Caminho da solução em questão ( lista de listas onde cada indice i representa um veiculo
                                # e para cada veiculo existe outra lista e cada elemento dessa lista j respresenta um cliente

    #---------VALORES OBJETIVOS---------#
    __custo_objetivo1 = 0.0 # [float] Variável que armazena o custo associado a solução em relação ao objetivo1(min)
    __qualidade_objetivo2= 0.0 # [float] Variável que armazena o ganho de qualidade associado a uma solução em relação ao obj2(max)

    #---------VALORES CROWNDING---------#
    __crownding_distance_objetivo1 = 0.0 # [float] Como usar esse trem ?
    __crownding_distance_objetivo2 = 0.0 # [float] Como usar esse trem ?



    # -----------CONSTRUTOR------------#
    def __init__(self, id):
        self.__id = id;



    #-----------SETTERS-----------#
    def set_id(self, id):
        #verifica tipo
        if (type(id) is int ):
            self.__id = id
            return True;
        else:
            return False;

    def set_tamanho_rota_por_veiculo(self, tamanho_rota_por_veiculo):
        # verifica tipo
        if (type(tamanho_rota_por_veiculo) is list):
            self.__tamanho_rota_por_veiculo = tamanho_rota_por_veiculo
            return True;
        else:
            return False;

    def set_numero_veiculos(self, numero_veiculos):
        # verifica tipo
        if (type(numero_veiculos) is int):
            self.__numero_veiculos = numero_veiculos
            return True;
        else:
            return False;

    def set_distancia_percorrida(self, distancia_percorrida):
        # verifica tipo
        if (type(distancia_percorrida ) is float):
            self.__distancia_percorrida  = distancia_percorrida
            return True;
        else:
            return False;

    def set_caminho_da_solucao(self, caminho_da_solucao):
        # verifica tipo
        if (type(caminho_da_solucao) is list):
            self.__caminho_da_solucao = caminho_da_solucao
            return True;
        else:
            return False;

    def set_custo_objetivo1(self, custo_objetivo1):
        # verifica tipo
        if (type(custo_objetivo1) is float):
            self.__custo_objetivo1 = custo_objetivo1
            return True;
        else:
            return False;

    def set_qualidade_objetivo2(self, qualidade_objetivo2):
        # verifica tipo
        if (type(qualidade_objetivo2) is float):
            self.__qualidade_objetivo2 = qualidade_objetivo2
            return True;
        else:
            return False;

    def set_crownding_distance_objetivo1(self, crownding_distance_objetivo1):
        # verifica tipo
        if (type(crownding_distance_objetivo1) is float):
            self.__crownding_distance_objetivo1 = crownding_distance_objetivo1
            return True;
        else:
            return False;

    def set_crownding_distance_objetivo2(self, crownding_distance_objetivo2):
        # verifica tipo
        if (type(crownding_distance_objetivo2) is float):
            self.__crownding_distance_objetivo2 = crownding_distance_objetivo2
            return True;
        else:
            return False;



    # -----------GETTERS-----------#
    def get_id(self):
        return self.__id

    def get_tamanho_rota_por_veiculo(self):
        return self.__tamanho_rota_por_veiculo

    def get_numero_veiculos(self):
        return self.__numero_veiculos

    def get_distancia_percorrida(self):
        return self.__distancia_percorrida

    def get_caminho_da_solucao(self):
        return self.__caminho_da_solucao

    def get_custo_objetivo1(self):
        return self.__custo_objetivo1

    def get_qualidade_objetivo2(self):
        return self.__qualidade_objetivo2

    def get_crownding_distance_objetivo1(self):
        return self.__crownding_distance_objetivo1

    def get_crownding_distance_objetivo2(self):
        return self.__crownding_distance_objetivo2


    #-----------PRINT-----------#
    def print(self):
        print(f"id = {self.get_id()}"
              f"\ntamanho_rota_por_veiculo = { self.get_tamanho_rota_por_veiculo()}"
              f"\nnumero_veiculos = { self.get_numero_veiculos()}"
              f"\ndistancia_percorrida = { self.get_distancia_percorrida()}"
              f"\ncaminho_da_solucao = { self.get_caminho_da_solucao()}"
              f"\ncusto_objetivo1 = { self.get_custo_objetivo1()}"
              f"\nqualidade_objetivo2 = { self.get_qualidade_objetivo2()}"
              f"\ncrownding_distance_objetivo1 = { self.get_crownding_distance_objetivo1()}"
              f"\ncrownding_distance_objetivo2 = { self.get_crownding_distance_objetivo2()}")