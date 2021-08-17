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
from Classes.Pymoo.MeuSelection import MeuSelection
from pymoo.factory import get_termination
from pymoo.factory import get_performance_indicator
from Classes.Pymoo.BuscaLocal import BuscaLocalRepair

import numpy as np
from pymoo.factory import get_problem
from pymoo.visualization.scatter import Scatter

from pymoo.algorithms.so_brkga import BRKGA
from pymoo.algorithms.rnsga2 import RNSGA2
from pymoo.algorithms.nsga3 import NSGA3
#from pymoo.problems.single.traveling_salesman import visualize


#Roda o algortmo para resolução do problema
#Parametros
# p -> Intância da Classe Problema
# num_gen -> Inteiro com numero de gerações
# tam_pop -> Tamanho da população
def run(p, num_gen, tam_pop, n_exec):


    #---BUSCA LOCAL---#
    dados_busca_local = {
        "itrs_vns": 3,
        "itrs_vnd": 5,
        "itrs_local": 3,
        "using_VND" : False
    }

    #---CRUZAMENTO---#
    size_corte_cruzamento = 1/2
    n_filhos = 2
    n_cruzamentos = 10

    #---MUTAÇÃO---#
    prob_mutacao = 0.2


    problem = MeuProblema(p)
    algorithm = NSGA2(
        pop_size=tam_pop,
        n_offsprings=  tam_pop,
        sampling=MeuRandomSampling(p,dados_busca_local),
        crossover=MeuCrossover(size_corte_cruzamento, n_offsprings=2, n_parents=2 ),
        mutation=MeuMutation(prob=prob_mutacao),
        repair= None,
        eliminate_duplicates=True
    )

    termination = get_termination("n_gen", num_gen)



    all_results = []
    all_hypervolumes = []
    for i in range(n_exec):
        res = minimize(
            problem,
            algorithm,
            termination,
            seed=None
        )

        # Calculando hypervolume
        result = np.copy(res.F)
        for i in range(result.shape[0]):  # convertendo função obj2 para valores positivos
            result[i][1] = result[i][1] * -1



        hv = get_performance_indicator("hv", ref_point=np.array([6000, 2.0]))
        hv_value = hv.calc(result)

        # Printando Resultados
        # print(res.X)
        print(f"i={i + 1}:{res.F}")
        print("hv = ", hv_value)




        #salvando resultado e hiper-volume
        all_results.append(result)
        all_hypervolumes.append(hv_value)



    # printando resultados
    figure = Scatter(legend=True)
    for i in range(len(all_results)):
       figure.add(all_results[i], label=f"Simulação {i+1}")
    #figure.show()


    all_results = np.array(all_results)
    all_hypervolumes = np.array(all_hypervolumes)

    print ("####### ROTINA #######")
    print(repr(all_results))
    print(repr(all_hypervolumes))
    print("#######################")


    return all_results, all_hypervolumes
