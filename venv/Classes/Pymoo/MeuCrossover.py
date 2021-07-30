import numpy as np, random
from math import ceil, floor
import time

from pymoo.model.crossover import Crossover


def cruzamento(a, b, size_corte):
    """
    OPERADOR ORDER CROSSOVER(OX) -> DAVIS, L. Applying adaptive algorithms to epistatic domains. In: IJCAI. [S.l.: s.n.], 1985. v. 85,
p. 162–164.
     """

    assert len(a) == len(b)

    if(len(a) <= 1):
        raise Exception("Numero de variaveis pequeno demais para realizar cruzamento")

    intervalo_size = len(a) * size_corte
    #print(f"intervalo_size={intervalo_size}")
    indice_max = ceil(len(a) - intervalo_size)
    #print(f"indice_max={indice_max}")
    n_elems = floor(intervalo_size)
    #print(f"n_elems={n_elems}")
    indice = random.randint(0, indice_max)
    #print(f"indice={indice}")

    a_corte = a[indice: indice+n_elems]
    b_corte = b[indice: indice + n_elems]

    # print(f"a_corte={a_corte}({len(a_corte)})")
    # print(f"a_rest={a_rest}({len(a_rest)})")
    # print(f"a={a}({len(a)})")

    # print(f"b_corte={b_corte}({len(b_corte)})")
    # print(f"b_rest={b_rest}({len(b_rest)})")
    # print(f"b={b}({len(b)})")


    #-------------FILHO 1-------------#
    y1 = np.full( (len(a)) , -1, dtype=int)
    y1[indice: indice + n_elems] = a_corte

    #Adiciona os elementos de b em y partindo do ponto de corte de ambos
    indice_b = indice + n_elems -1
    indice_y1 = indice + n_elems -1


    while -1 in y1 :

        if ( y1[indice_y1] == -1  ):

            while b[indice_b] in y1:
                indice_b = indice_b + 1 if indice_b + 1 < len(b) else 0

            y1[indice_y1] = b[indice_b]

        indice_y1 = indice_y1 + 1 if indice_y1 +1 < len(y1) else 0




    # -------------FILHO 2-------------#
    y2 = np.full((len(b)), -1, dtype=int)
    y2[indice: indice + n_elems] = b_corte

    # Adiciona os elementos de a em y partindo do ponto de corte de ambos
    indice_a = indice + n_elems - 1
    indice_y2 = indice + n_elems - 1

    while -1 in y2:

        if (y2[indice_y2] == -1):

            while a[indice_a] in y2:
                indice_a = indice_a + 1 if indice_a + 1 < len(a) else 0

            y2[indice_y2] = a[indice_a]

        indice_y2 = indice_y2 + 1 if indice_y2 + 1 < len(y2) else 0


    assert len(y1) == len(set(y1))
    assert len(y2) == len(set(y2))



    return y1, y2




class MeuCrossover(Crossover):


    def __init__(self, tam_corte, n_parents, n_offsprings, **kwargs):
        self.size_corte = tam_corte
        super().__init__(n_parents=n_parents, n_offsprings=n_offsprings, **kwargs)

    def _do(self, problem, X, **kwargs):
        #print("CRUZAMENTO")

        _, n_matings, n_var = X.shape
        Y = np.full((self.n_offsprings, n_matings, n_var), -1, dtype=int)



        for i in range(n_matings):
            a, b = X[:, i, :]
            #print("CRUZOU")
            y1, y2 = cruzamento(a, b, self.size_corte)
            Y[0, i, :] = y1
            Y[1, i, :] = y2

        return Y


