import numpy as np
from pymoo.model.repair import Repair
import numpy as np
from math import ceil
from random import randint
import copy
from time import sleep

class BuscaLocalRepair(Repair):

    def __init__(self, p):
        self.problema_externo = p

    def _do(self, problem, pop, **kwargs):

        num_buscas = 10
        X = pop.get("X")



        for i in range(len(X)):

            x = np.copy(X[i]) #Copia da solução referencia
            best = np.copy(x) #Armazena a melhor solução da vizinhaça
            obj1_best, obj2_best = self.problema_externo.objs(best) #Armazena os valores objetivos de 'best'

            pos_pivo = np.random.randint(len(x)) #Elemento pivo aletório

            for j in range(num_buscas):
                x_temp = np.copy(x) #Armazena o vizinho
                pos_temp = (pos_pivo + j +1) % len(x) #Aramazena posição a ser trocada pelo pivo

                #Operador de troca
                x_temp[pos_pivo] = x[pos_temp]
                x_temp[pos_temp] = x[pos_pivo]

                #Verifica melhora e se houver armazena a solução em 'best'
                obj1_temp, obj2_temp = self.problema_externo.objs(x_temp)
                if( (obj1_temp < obj1_best and obj2_temp >= obj2_best) or (obj1_temp <= obj1_best and obj2_temp > obj2_best)):
                    best = x_temp
                    obj1_best, obj2_best = self.problema_externo.objs(best)


            #Armazena a melhor solução
            X[i] = best

        pop.set("X", X)

        return pop

class BuscaLocal():



    def __init__(self, itrs_vns, itrs_vnd, itrs_local, using_VND, problema_externo):

        if not (type(itrs_vns) is int):
            raise Exception ( "On BuscaLocal, invalid itrs_vns parameter")
        self.__itrs_vns = itrs_vns

        if not (type(itrs_vnd) is int):
            raise Exception ( "On BuscaLocal, invalid itrs_vnd parameter")
        self.__itrs_vnd = itrs_vnd

        if not (type(itrs_local) is int):
            raise Exception ( "On BuscaLocal, invalid itrs_local parameter")
        self.__itrs_local = itrs_local

        if not (type(using_VND) is bool):
            raise Exception ( "On BuscaLocal, invalid using_VND parameter")
        self.__using_VND = using_VND

        self.__problema_externo = problema_externo

        self.estruturas_first = [movimento_troca, movimento_intercambio, movimento_inversao, movimento_cruzamento_tradicional]
        self.estruturas_VND = [movimento_troca, movimento_intercambio, movimento_inversao, movimento_cruzamento_tradicional]
        self.estruturas_VNS = [movimento_troca, movimento_intercambio, movimento_inversao, movimento_cruzamento_tradicional]



    def run(self, X):
        print( "INICIO BUSCA LOCAL")


        for i in range(len(X)):

            # Copia da solução referencia
            x = np.copy(X[i])
            # Converte para formato de Rotas
            x_rota = self.__problema_externo.converte_array_solucao(x)
            #Aplica Busca Local(VNS)
            x_rota_best = self.VNS(x_rota)
            #Remove origens das rotas para realizar conversão
            remove_origens_rota(x_rota_best)
            #Converte de Rota para NParray
            x_array_best = self.__problema_externo.converte_solucao_array(x_rota_best)


            #Armazena a melhor solução
            X[i] = x_array_best

        print("FIM BUSCA LOCAL")

    #METODO PARA AVALIAÇÃO DAs SOLUÇÔES
    def is_better(self, rota_ref, rota_in):

        obj1_ref, obj2_ref  = self.__problema_externo.func_objs(rota_ref)
        obj1_in, obj2_in = self.__problema_externo.func_objs(rota_in)
        return (obj1_ref <= obj1_in and obj2_ref > obj2_in ) or (obj1_ref < obj1_in and obj2_ref >= obj2_in )

    #METODOS DE BUSCA
    def first_improvement(self, rota):

        estruturas = self.estruturas_first
        max_itr = self.__itrs_local
        for i in range(max_itr):

            rota_itr = copy.deepcopy(rota)
            i_estrutura = i % len(estruturas)
            estruturas[i_estrutura](rota_itr)

            if self.is_better(rota_itr, rota):
                rota = rota_itr
                return rota, True

        return rota, False

    def VND(self, rota ):
        rota_scope = copy.deepcopy(rota)

        estruturas = self.estruturas_VND
        algorithm_local = self.first_improvement
        itrs = self.__itrs_vnd

        print("-----------VND----------")
        for i in range(itrs):
            k = 1

            print("ETAPA VND: ", end="")
            while k <= len(estruturas):

                rota_by_local = copy.deepcopy(rota_scope)
                rota_by_local, _ = algorithm_local(rota_by_local)

                print(rota_by_local)
                print(rota_scope)
                if self.is_better(rota_by_local, rota_scope):
                    print("better")
                    rota_scope = rota_by_local
                    k = 1
                else:
                    k = k + 1

            print("-----------END VND----------")

        return rota_scope, True

    def VNS(self, rota):

        rota_scope = copy.deepcopy(rota)

        itrs = self.__itrs_vns
        estruturas = self.estruturas_VNS
        if self.__using_VND:
            algorithm_local = self.VND
        else:
            algorithm_local = self.first_improvement

        # Rotina VNS
        print("------------VNS-----------")
        for i in range(itrs):
            k = 1

            print("ETAPA VNS: ", end="")
            while k <= len(estruturas):

                rota_neighbor = copy.deepcopy(rota_scope)
                estruturas[k - 1](rota_neighbor)

                rota_by_local, _ = algorithm_local(rota_neighbor)

                print(rota_neighbor)
                print(rota_by_local)
                print(rota_scope)
                if self.is_better(rota_by_local, rota_scope):
                    print("better")
                    rota_scope = rota_by_local
                    k = 1
                else:
                    k = k + 1

            print("---------END VNS---------")

        return rota_scope


##ESTRUTURAS DE VIZINHAÇA
def movimento_troca(rotas):

    #Eliminando origem das rotas para realizar operação
    remove_origens_rota(rotas)

    # Definindo em qual das rotas será relizada a troca
    i_rota = randint(0, len(rotas) - 1)
    repeats = 0

    while len(rotas[i_rota]) <= 1:
        repeats += 1
        i_rota = (i_rota + 1) % len(rotas)
        if (repeats == len(rotas)):
            return
            #raise Exception('In: movimento_troca ( Rotas muito pequenas para realizar trocas )')

    rota = rotas[i_rota]

    # Troca
    i_elem1 = randint(0, len(rota) - 1)
    i_elem2 = randint(0, len(rota) - 1)
    if (i_elem1 == i_elem2):
        i_elem2 = (i_elem2 + 1) % len(rota)

    temp = rota[i_elem1]
    rota[i_elem1] = rota[i_elem2]
    rota[i_elem2] = temp

    print("troca")
    adiciona_origens_rota(rotas)
    return

def movimento_intercambio(rotas):
    # Eliminando origem das rotas para realizar operação
    remove_origens_rota(rotas)


    if len(rotas) <= 1:
        raise Exception('In: movimento_intercambio ( poucas rotas )')

    # Definindo entre quais das rotas será relizada a troca
    i_rota1 = randint(0, len(rotas) - 1)
    i_rota2 = randint(0, len(rotas) - 1)
    if i_rota1 == i_rota2:
        i_rota2 = (i_rota2 + 1) % len(rotas)

    rota1 = rotas[i_rota1]
    rota2 = rotas[i_rota2]

    # Troca
    i_elem1 = randint(0, len(rota1) - 1)
    i_elem2 = randint(0, len(rota2) - 1)

    temp = rota1[i_elem1]
    rota1[i_elem1] = rota2[i_elem2]
    rota2[i_elem2] = temp

    print("intercambio")
    adiciona_origens_rota(rotas)
    return

def movimento_realocacao(rotas):
    # Eliminando origem das rotas para realizar operação
    remove_origens_rota(rotas)


    if len(rotas) <= 1:
        raise Exception('In: movimento_realocação ( poucas rotas )')

    # Definindo entre quais das rotas será relizada a troca
    i_rota1 = randint(0, len(rotas) - 1)
    i_rota2 = randint(0, len(rotas) - 1)
    if i_rota1 == i_rota2:
        i_rota2 = (i_rota2 + 1) % len(rotas)

    rota1 = rotas[i_rota1]
    rota2 = rotas[i_rota2]

    if len(rota1) <= 1 or len(rota2) <= 1:
        # Do nothing
        return
        # raise Exception('In: movimento_realocação ( Poucos clientes )')

    # Troca
    i_elem = randint(0, len(rota1) - 1)

    elem = rota1.pop(i_elem)
    rota2.append(elem)

    print("realocação")
    adiciona_origens_rota(rotas)
    return

def movimento_inversao(rotas):
    # Eliminando origem das rotas para realizar operação
    remove_origens_rota(rotas)

    # Definindo entre quais das rota será relizada a inversão
    i_rota = randint(0, len(rotas) - 1)
    repeats = 0

    while len(rotas[i_rota]) <= 1:
        repeats += 1
        i_rota = (i_rota + 1) % len(rotas)
        if (repeats == len(rotas)):
            return
            raise Exception('In: movimento_inversao ( Rotas muito pequenas para realizar trocas )')

    rota = rotas[i_rota]

    # Inversão
    intervalo = np.random.choice(len(rota), 2, replace=False)
    i_ini, i_fim = np.sort(intervalo)
    rota[i_ini:i_fim] = rota[i_ini:i_fim][::-1]

    print("inversão")
    adiciona_origens_rota(rotas)
    return

def movimento_cruzamento_tradicional(rotas):

    # Eliminando origem das rotas para realizar operação
    remove_origens_rota(rotas)

    if len(rotas) <= 1:
        raise Exception('In: movimento_cruzamento_tradicional ( poucas rotas )')

    # Definindo entre quais das rotas será relizada o cruzamento
    i_rota1 = randint(0, len(rotas) - 1)
    i_rota2 = randint(0, len(rotas) - 1)
    if i_rota1 == i_rota2:
        i_rota2 = (i_rota2 + 1) % len(rotas)

    rota1 = rotas[i_rota1]
    rota2 = rotas[i_rota2]

    # Cruzamento
    half1 = int(len(rota1) / 2)
    half2 = int(len(rota2) / 2)

    temp = rota1[half1:]
    rota1[half1:] = rota2[half2:]
    rota2[half2:] = temp

    print("cruzamento")
    adiciona_origens_rota(rotas)
    return


#CONVERSÂO DE FORMATOS PARA SOLUÇÔES
def remove_origens_rota(rotas):
  for i in range(len(rotas)):
    rotas[i] = rotas[i][1:-1]

def adiciona_origens_rota(rotas):
  for i in range(len(rotas)):
    rotas[i].insert(0,0)
    rotas[i].append(0)