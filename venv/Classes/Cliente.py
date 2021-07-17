#prototipo
class Cliente:
    __indice = 0  # [int] indice do cliente
    __x_coord = 0  # [int] coordenada x do cliente
    __y_coord = 0  # [int] coordenada y do cliente
    __demanda = 0  # [int] demanda do produto para o cliente
    __janela_inicio = 0  # [int] tempo que representa o inicio da janela de tempo do cliente
    __janela_fim = 0  # [int] tempo que representa o final da janela de tempo do cliente
    __tempo_de_servico = 0  # [int] tempo para prestação de serviço do cliente (quando o veiculo já está no cliente)

    #-----------CONSTRUTOR------------#

    def __init__(self, indice = 0 , x_coord = 0, y_coord = 0, demanda = 0, janela_inicio = 0, janela_fim = 0, tempo_de_servico = 0):
        self.set_indice(indice)
        self.set_x_coord(x_coord)
        self.set_y_coord(y_coord)
        self.set_demanda(demanda)
        self.set_janela_inicio(janela_inicio)
        self.set_janela_fim(janela_fim)
        self.set_tempo_de_servico(tempo_de_servico)
        return

    #-----------SETTERS------------#

    def set_indice(self, indice):
        if(type(indice) is int):
            self.__indice= indice
            return True
        else:
            return False

    def set_x_coord(self, x_coord):
        if (type(x_coord) is int):
            self.__x_coord = x_coord
            return True
        else:
            return False

    def set_y_coord(self, y_coord):
        if (type(y_coord) is int):
            self.__y_coord = y_coord
            return True
        else:
            return False

    def set_demanda(self, demanda):
        if (type(demanda) is int):
            self.__demanda = demanda
            return True
        else:
            return False

    def set_janela_inicio(self, janela_inicio):
        if (type(janela_inicio) is int or type(janela_inicio) is float):
            self.__janela_inicio = janela_inicio
            return True
        else:
            return False

    def set_janela_fim(self, janela_fim):
        if (type(janela_fim) is int or type(janela_fim) is float ):
            self.__janela_fim = janela_fim
            return True
        else:
            return False

    def set_tempo_de_servico(self, tempo_de_servico):
        if (type(tempo_de_servico) is int or type(tempo_de_servico) is float):
            self.__tempo_de_servico = tempo_de_servico
            return True
        else:
            return False

    #-----------GETTERS------------#
    def get_indice(self):
        return self.__indice

    def get_x_coord(self):
        return self.__x_coord

    def get_y_coord(self):
        return self.__y_coord

    def get_demanda(self):
        return self.__demanda

    def get_janela_inicio(self):
        return self.__janela_inicio

    def get_janela_fim(self):
        return self.__janela_fim

    def get_tempo_de_servico(self):
        return self.__tempo_de_servico

    #---------FUNCOES_AUX--------#
    def calcula_distancia_clientes(self, cliente_2):
        if(True):
            x1 = self.get_x_coord()
            y1 = self.get_y_coord()
            x2 = cliente_2.get_x_coord()
            y2 = cliente_2.get_y_coord()
            return  float((x1 - x2)**2 +(y1 - y2)**2)**0.5

        return -1



    #-----------PRINT----------#
    def __str__(self):
        return f"[ id: {self.get_indice()}, x: {self.get_x_coord()}, y: {self.get_y_coord()}, demanda: {self.get_demanda()}, janela_inicio: {self.get_janela_inicio()}, janela_fim: {self.get_janela_fim()}, tempo_servico: {self.get_tempo_de_servico()} ]"
        #return f"[id:{self.get_indice()}, x: {self.get_x_coord()}, y: {self.get_y_coord()}]"

    def __repr__(self):
        #return f"[ id: {self.get_indice()}, x: {self.get_x_coord()}, y: {self.get_y_coord()}, demanda: {self.get_demanda()}, janela_inicio: {self.get_janela_inicio()}, janela_fim: {self.get_janela_fim()}, tempo_servico: {self.get_tempo_de_servico()} ]"
        return f"[id:{self.get_indice()}]"

    def print(self):
        print(f"\nindice = {self.get_indice()}"
              f"\nx_coord = {self.get_x_coord()}"
              f"\ny_coord = {self.get_y_coord()}"
              f"\ndemanda = {self.get_demanda()}"
              f"\njanela_inicio = {self.get_janela_inicio()}"
              f"\njanela_fim = {self.get_janela_fim()}"
              f"\ntempo_de_servico= {self.get_tempo_de_servico()}"
              )

