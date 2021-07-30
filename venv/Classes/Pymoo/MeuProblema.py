import matplotlib.pyplot as plt
import numpy as np
from pymoo.model.sampling import Sampling
from pymoo.model.repair import Repair
from scipy.spatial.distance import pdist, squareform, cdist
from pymoo.model.problem import Problem
from Classes.Pymoo.BuscaLocal import buscaLocal, sleep


class MeuProblema(Problem):

    def __init__(self, p, **kwargs):
        self.dados_problema = p
        n_clientes = p.get_numero_clientes() -1 #subrai a origem
        self.n_clientes = n_clientes

        super(MeuProblema, self).__init__(
            n_var=n_clientes,
            n_obj=2,
            xl=1,
            xu=n_clientes,
            type_var=int,
            elementwise_evaluation=True,
            **kwargs
        )

    def _evaluate(self, x, out, *args, **kwargs):
        f1, f2 = self.dados_problema.objs(x)

        f2 = f2 * -1 #Como f2 originalmente deve ser maximizada, multiplica-se por -1 e converte para minimização
        #print(f"f1:{f1} | f2:{f2} | X:{x}")

        out['F'] = [f1,f2]

    def get_route_length(self, x):
        n_cities = len(x)
        dist = 0
        for k in range(n_cities - 1):
            i, j = x[k], x[k + 1]
            dist += self.D[i, j]

        last, first = x[-1], x[0]
        dist += self.D[last, first]  # back to the initial city
        return dist



    def obj1(self,x):
        n_clientes = len(x)
        cost = 0
        for i in range(n_clientes):
            cost += i * x[i]


        return cost

    def obj2(self,x):
        n_clientes = len(x)
        cost = 0
        for i in range(n_clientes):
            cost += np.random.randint(1,20) * (x[i]%2)
        return cost



##VISUALIZAÇÃO
def visualize(solution, fig=None, ax=None, show=True, label=True):
    with plt.style.context('ggplot'):

        if fig is None or ax is None:
            fig, ax = plt.subplots()

        ax.scatter(solution[:, 0], solution[:, 1], s=250)
        plt.show()



#SAMPLES
class MeuRandomSampling(Sampling):
    def __init__(self, problema, numero_buscas):
        self.n_buscas = numero_buscas
        self.problema_externo = problema

    def _do(self, problem, n_samples, **kwargs):
        X = np.full((n_samples, problem.n_var), 0, dtype=int)
        for i in range(n_samples):
            X[i, :] = np.random.permutation(problem.n_var) + 1


        buscaLocal(X,self.n_buscas, self.problema_externo)
        print(f"POP INICIAL ({len(X)})")
        return X


#SAMPLES
class RandomSamplingExterno(Sampling):
    def __init__(self, problema, numero_buscas):
        self.n_buscas = numero_buscas
        self.problema_externo = problema

    def _do(self, problem, n_samples, **kwargs):

        X = np.full((n_samples, problem.n_var), 0, dtype=int)
        for i in range(n_samples):
            X[i, :] = np.random.permutation(problem.n_var) + 1
            #print(X[i])

        buscaLocal(X,self.n_buscas, self.problema_externo)
        return X




