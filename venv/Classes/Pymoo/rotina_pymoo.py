import numpy as np
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.algorithms.so_genetic_algorithm import GA
from pymoo.optimize import minimize
from pymoo.factory import get_algorithm, get_crossover, get_mutation, get_sampling
from pymoo.problems.single.traveling_salesman import create_random_tsp_problem
from pymoo.util.termination.default import SingleObjectiveDefaultTermination
from Classes.Pymoo.MeuProblema import MeuProblema
from Classes.Pymoo.MeuProblema import MeuRandomSampling
from Classes.Pymoo.MeuProblema import  visualize
from Classes.Pymoo.MeuCrossover import  MeuCrossover
from Classes.Pymoo.MeuMutation import MeuMutation
from pymoo.factory import get_termination
from Classes.Pymoo.BuscaLocal import BuscaLocalRepair

from pymoo.algorithms.so_brkga import BRKGA
from pymoo.algorithms.rnsga2 import RNSGA2
from pymoo.algorithms.nsga3 import NSGA3
#from pymoo.problems.single.traveling_salesman import visualize


#Roda o algortmo para resolução do problema
#Parametros
# p -> Intância da Classe Problema
# num_gen -> Inteiro com numero de gerações
# tam_pop -> Tamanho da população
def run(p, num_gen, tam_pop):

    problem = MeuProblema(p) # 'p' = representa um instancia da classe problema


    #---BUSCA LOCAL---#
    n_buscas = 10 #Numero de buscas locais
    #---CRUZAMENTO---#
    size_corte_cruzamento = 1/2
    n_filhos = 2
    #---MUTAÇÃO---#
    prob_mutacao = 0.2

    ref_point = np.array([[-0.90, 820]])


    algorithm = NSGA2(
        pop_size=tam_pop,
        n_offsprings=n_filhos ,
        sampling=MeuRandomSampling(p,n_buscas),
        crossover=MeuCrossover(size_corte_cruzamento, n_filhos),
        mutation=MeuMutation(prob=prob_mutacao),
        repair= None,
        eliminate_duplicates=True
    )

    termination = get_termination("n_gen", num_gen)

    res = minimize(
        problem,
        algorithm,
        termination,
        seed=None
    )

    print(res.F)
    print(res.X)
    visualize(res.F)

    return res
