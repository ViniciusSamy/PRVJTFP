from pymoo.model.mutation import Mutation
import numpy as np
import time

from pymoo.operators.crossover.order_crossover import random_sequence


def mutacao_inversao(y, seq, inplace=True):
    y = y if inplace else np.copy(y)

    seq = seq if not None else random_sequence(len(y))
    start, end = seq

    y[start:end + 1] = np.flip(y[start:end + 1])
    return y

def mutacao_troca(y, inplace=True):
    y = y if inplace else np.copy(y)

    i_1 = np.random.randint(len(y))
    i_2 = np.random.randint(len(y))
    while i_1 == i_2:
        i_2 = np.random.randint(len(y))


    temp = y[i_1]
    y[i_1] = y[i_2]
    y[i_2] = temp


    return y

class MeuMutation(Mutation):

    def __init__(self, prob=1.0):
        super().__init__()
        self.prob = prob

    def _do(self, problem, X, **kwargs):
        Y = X.copy()
        for i, y in enumerate(X):
            if np.random.random() < self.prob:
                #seq = random_sequence(int(len(y)/6))
                #Y[i] = mutacao_inversao(y, seq, inplace=True)
                Y[i] = mutacao_troca(y, inplace=True)

        return Y