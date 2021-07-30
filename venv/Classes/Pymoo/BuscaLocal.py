import numpy as np
from pymoo.model.repair import Repair
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


def buscaLocal(X, num_buscas, problema_externo):


    for i in range(len(X)):

        # Copia da solução referencia
        x = np.copy(X[i])
        # Armazena a melhor solução da vizinhaça
        best = np.copy(x)
        # Armazena os valores objetivos de 'best'
        obj1_best, obj2_best = problema_externo.objs(best)

        # Elemento pivo aletório
        pos_pivo = np.random.randint(len(x))

        for j in range(num_buscas):
            x_temp = np.copy(x) #Armazena o vizinho
            pos_temp = (pos_pivo + j +1) % len(x) #Aramazena posição a ser trocada pelo pivo

            #Operador de troca
            x_temp[pos_pivo] = x[pos_temp]
            x_temp[pos_temp] = x[pos_pivo]

            #Verifica melhora e se houver armazena a solução em 'best'
            obj1_temp, obj2_temp = problema_externo.objs(x_temp)
            if( (obj1_temp < obj1_best and obj2_temp >= obj2_best) or (obj1_temp <= obj1_best and obj2_temp > obj2_best)):
                best = x_temp
                obj1_best, obj2_best = problema_externo.objs(best)


        #Armazena a melhor solução
        X[i] = best

