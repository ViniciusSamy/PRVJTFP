from Classes.Solucao import Solucao
from Classes.Problema import Problema
from Classes.Cliente import Cliente
from Modulos.Funcoes import *
from Classes.KmeansST import KmeansST
from math import ceil
import numpy as np
import Classes.Pymoo.rotina_pymoo as algoritmo_pymoo
from FuncoesAuxiliares import write_multi


#------------PARAMETROS------------#
#Problema
velocidade_veiculo_km_h = 30.0
velocidade_veiculo_m_s = velocidade_veiculo_km_h / 3.6
custo_transporte_unidade_distancia = 0.5
tempo_servico_clientes = 5
custo_fixo_veiculo = 50.0
capacidade_fixa_veiculos = 50

w1 = 1
w2 = 1
w3 = 2

beta = 0.75 #Valor minimo da função beta de aceitação de um cliente
T = 12.0 #Life clicle (usado no calculo da função objetivo 2)



#Kmeans
k_clusters = 4; #numero de clusters
lim_iteracoes = -1 ; #limite de interações (-1)->Sem limite
k1 = 1.0
k2 = 1.5
k3 = 2.0
alpha1 = 0.5
alpha2 = 0.5
#----------------------------------#



# #----------LENDO-INTANCIA----------#
# instancia_dir = 'venv/Instancias/100/R101.txt'
# #instancia_dir = 'venv/Instancias/TesteDeMesa.txt'
# nome_instancia, max_veiculos, capacidade_veiculos, clientes = ler_instancia(instancia_dir)
# capacidade_veiculos = capacidade_fixa_veiculos
# #----------------------------------#
#
#
#
# #---------CRIANDO-PROBLEMA---------#
# p = Problema()
# p.set_numero_clientes(len(clientes))
# p.set_numero_max_veiculos(max_veiculos)
# p.set_capacidade_veiculo(capacidade_veiculos)
# p.set_dados_cliente(clientes)
# p.set_velocidade_veiculo(velocidade_veiculo_km_h)
# p.set_custo_tranporte_unidade_distancia(custo_transporte_unidade_distancia)
# p.set_custo_veiculo(custo_fixo_veiculo)
# p.set_tempo_servico(tempo_servico_clientes)
# p.att_tempo_servico() #Atualiza o tempo de servico para todos os clientes do problema com exeção da origem
# p.set_qualidade_produto(beta)
# p.set_ciclo_de_vida_produto(T)
# ##
# p.att_janelas_de_tempo(1/60)
#
# p.set_w1(w1)
# p.set_w2(w2)
# p.set_w3(w3)
#
# p.print() #Printa Dados do Problema
# #----------------------------------#




#---------CRIANDO-PROBLEMA---------#
#n_amostra_clientes = 11
#p.set_numero_clientes(n_amostra_clientes)
#p.set_dados_cliente(clientes[:n_amostra_clientes])
#print(clientes[:n_amostra_clientes])
#print(len(clientes[:n_amostra_clientes]))
#p.print()
#----------------------------------#


#----GERANDO-E-PRINTANDO-SOLUÇÂO---#
# solucao1 = p.criando_solucao_aleatoria()
# instantes1 = p.calcula_instantes_de_entrega(solucao1)
# for rota in solucao1:
#     print('----------ROTA-----------')
#     for cliente in rota:
#         print(cliente)
#     print()
#----------------------------------#



#---GERANDO-E-PRINTANDO-INSTANTES--#
# for i in range(len(solucao1)):
#     rota  = solucao1[i]
#     rota_instantes = instantes1[i]
#     print(f'----------------------------ROTA {i}----------------------------')
#     for j in range( len(rota) ):
#         print(rota[j])
#         print(f'=>t[{j}]={rota_instantes[j]}')
#         print(f'=>B[{j}] = B({rota_instantes[j]}) = {p.beta(rota_instantes[j],T)} \n')
#
#----------------------------------#



#---------FUNÇÕES=OBJETIVO---------#
# print("------OBJETIVOS------")
# #print(f"OBJ1 :{p.func_obj1_alt(solucao1,instantes1)}")
# #print(f"OBJ2 :{p.func_obj2_alt(solucao1,instantes1)}")
# print(f"OBJ1 :{p.func_obj1(solucao1,instantes1)}")
# print(f"OBJ2 :{p.func_obj2(solucao1,instantes1)}")
#----------------------------------#



# #--------------KMEANS--------------#
# print("----------------KMeansST----------------")
# kmeans = KmeansST(k1, k2, k3, alpha1, alpha2, velocidade_veiculo_m_s, clientes)
# kmeans.calcular_distancias()
# #kmeans.print()
# #kmeans.print_ST()
# demanda_total = p.get_demanda_total()
#
# k_clusters = ceil( p.get_demanda_total()/p.get_capacidade_veiculo())
# clusters = kmeans.executar(k_clusters, lim_iteracoes)
#
# matriz_ST = kmeans.get_matriz_distancias_ST()
#
# #----------------------------------#

# #----GERANDO-E-PRINTANDO-SOLUÇÂO---#
# solucao2 = p.criando_solucao_clusterizada(clusters, matriz_ST)
# instantes2 = p.calcula_instantes_de_entrega_1(solucao2)
# print(solucao1)
# print(solucao2)
# #for rota in solucao2:
# #    print('----------ROTA-----------')
# #    for cliente in rota:
# #        print(cliente)
# #    print()
# #print(clusters)
# print("------OBJETIVOS------")
# print(f"OBJ1 :{p.func_obj1(solucao2,instantes2)}")
# print(f"OBJ2 :{p.func_obj2(solucao2,instantes2)}")
# #----------------------------------#



# #-----------TESTE-PYMOO------------#
# numero_geracoes = 100
# tamanho_populacao = 100
# numero_de_execucoes = 1
# res , hypervolumes = algoritmo_pymoo.run(p, numero_geracoes, tamanho_populacao, numero_de_execucoes)
# #----------------------------------#
#
#
# #-------------Output---------------#
# print()
# path = "../../Documentos/UFOP/IC/Resultados/SemVNS/Saida.xlsx"
# write_res(path, p, res, instancia_dir)


#-------RODANDO VARIAS INSTANCIAS-------#
instancias = [ "R101", "R102", "R103", "R104", "R105", "R106", "R107", "R108", "R109", "R110", "R111" ]
n_clientes = "100"

for instancia in instancias:
    # ----------LENDO-INTANCIA----------#
    instancia_dir = f'venv/Instancias/{n_clientes}/{instancia}.txt'
    # instancia_dir = 'venv/Instancias/TesteDeMesa.txt'
    nome_instancia, max_veiculos, capacidade_veiculos, clientes = ler_instancia(instancia_dir)
    capacidade_veiculos = capacidade_fixa_veiculos
    # ----------------------------------#

    # ---------CRIANDO-PROBLEMA---------#
    p = Problema()
    p.set_numero_clientes(len(clientes))
    p.set_numero_max_veiculos(max_veiculos)
    p.set_capacidade_veiculo(capacidade_veiculos)
    p.set_dados_cliente(clientes)
    p.set_velocidade_veiculo(velocidade_veiculo_km_h)
    p.set_custo_tranporte_unidade_distancia(custo_transporte_unidade_distancia)
    p.set_custo_veiculo(custo_fixo_veiculo)
    p.set_tempo_servico(tempo_servico_clientes)
    p.att_tempo_servico()  # Atualiza o tempo de servico para todos os clientes do problema com exeção da origem
    p.set_qualidade_produto(beta)
    p.set_ciclo_de_vida_produto(T)
    ##
    p.att_janelas_de_tempo(1 / 60)

    p.set_w1(w1)
    p.set_w2(w2)
    p.set_w3(w3)

    #p.print()  # Printa Dados do Problema
    # ----------------------------------#


    print(f"INSTANCIA: {instancia}")
    numero_geracoes = 30
    tamanho_populacao = 30
    numero_de_execucoes = 2
    all_res, all_hypervolumes = algoritmo_pymoo.run(p, numero_geracoes, tamanho_populacao, numero_de_execucoes)

    print("################################")
    #print(all_res.shape)
    #print(all_res)
    #print(all_hypervolumes.shape)
    #print(all_hypervolumes)

    path = f"../../Documentos/UFOP/IC/Resultados/SemVNS/{instancia}.xlsx"
    write_multi(path, p, numero_geracoes, tamanho_populacao, numero_de_execucoes, all_res, all_hypervolumes, instancia_dir)
