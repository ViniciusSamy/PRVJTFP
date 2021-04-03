import numpy as np
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.algorithms.so_genetic_algorithm import GA
from pymoo.optimize import minimize
from pymoo.factory import get_algorithm, get_crossover, get_mutation, get_sampling
from pymoo.problems.single.traveling_salesman import create_random_tsp_problem
from pymoo.util.termination.default import SingleObjectiveDefaultTermination
from MeuProblema import MeuProblema
from MeuProblema import MeuRandomSampling
from MeuProblema import StartFromTenRepair
from MeuProblema import  visualize
from MeuCrossover import  MeuCrossover
from MeuMutation import MeuMutation
from pymoo.factory import get_termination
#from pymoo.problems.single.traveling_salesman import visualize


def run():

    problem = MeuProblema(10)

    algorithm = NSGA2(
        pop_size=20,
        sampling=MeuRandomSampling(),
        crossover=MeuCrossover(),
        mutation=MeuMutation(),
        repair=StartFromTenRepair(),
        eliminate_duplicates=True
    )

    termination = get_termination("n_gen", 10)

    res = minimize(
        problem,
        algorithm,
        termination,
        seed=None
    )
    print(res.F)
    print(res.X)
    visualize(res.F)
