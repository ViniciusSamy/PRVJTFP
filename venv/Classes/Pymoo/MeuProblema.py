import matplotlib.pyplot as plt
import numpy as np
from pymoo.model.sampling import Sampling
from pymoo.model.repair import Repair
from scipy.spatial.distance import pdist, squareform, cdist
from pymoo.model.problem import Problem


class MeuProblema(Problem):

    def __init__(self, n_clientes, **kwargs):



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
        f1 = self.obj1(x)
        f2 = self.obj2(x)
        print(f"f1:{f1} | f2:{f2} | X:{x}")

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

        # plot cities using scatter plot
        ax.scatter(solution[:, 0], solution[:, 1], s=250)
        plt.show()
        #fig.suptitle("Route length: %.4f" % problem.get_route_length(x))
        fig.show()
        if show:
            fig.show()


#SAMPLES
class MeuRandomSampling(Sampling):

    def _do(self, problem, n_samples, **kwargs):
        X = np.full((n_samples, problem.n_var), 0, dtype=int)
        for i in range(n_samples):
            X[i, :] = np.random.permutation(problem.n_var) + 1
            print(X[i])
        return X


#REPAIR
class StartFromTenRepair(Repair):

    def _do(self, problem, pop, **kwargs):
        X = pop.get("X")
        #print(X)
        I = np.where(X == 10)[1]
        #print(I)
        #print("------------------------")
        #print(I)
        for k in range(len(X)):
            i = I[k]
            x = X[k]
            _x = np.concatenate([x[i:], x[:i]])
            pop[k].set("X", _x)
        #print(pop.get())

        return pop
