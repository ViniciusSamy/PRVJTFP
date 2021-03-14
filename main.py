
print("Hello World")

from Classes.Solucao import Solucao
from Classes.Problema import Problema
from Classes.Cliente import Cliente
from Modulos.Funcoes import *
from Classes.KmeansST import KmeansST

##PARAMETROS

velocidade_veiculo_km_h = 30.0
velocidade_veiculo_m_s = velocidade_veiculo_km_h / 3.6
custo_transporte_unidade_distancia = 0.5
tempo_servico_clientes = 5
custo_fixo_veiculo = 50.0
beta = 0.75


w1 = 10
w2 = 10
w3 = 20

beta = 0.75

##LENDO INTANCIA
instancia_dir = 'venv/Instancias/25/R201.txt'
nome_instancia, max_veiculos, capacidade_veiculos, clientes = ler_instancia(instancia_dir)



#CRIANDO PROBLEMA
p = Problema()
p.set_numero_clientes(len(clientes))
p.set_numero_max_veiculos(max_veiculos)
#p.set_capacidade_veiculo(capacidade_veiculos)
p.set_capacidade_veiculo(50)
p.set_dados_cliente(clientes)
p.set_velocidade_veiculo(velocidade_veiculo_m_s)
p.set_custo_tranporte_unidade_distancia(custo_transporte_unidade_distancia)
p.set_custo_veiculo(custo_fixo_veiculo)
p.set_tempo_servico(tempo_servico_clientes)
p.att_tempo_servico() #Atualiza o tempo de servico para todos os clientes do problema com exeção da origem

p.set_w1(w1)
p.set_w2(w2)
p.set_w3(w3)

p.print()

#GERANDO E PRINTANDO SOLUÇÂO
solucao1 = p.criando_solucao_fixa()
instantes1 = p.calcula_instantes_de_entrega_2(solucao1)
for rota in solucao1:
    print('----------ROTA-----------')
    for cliente in rota:
        print(cliente)
    print()

for i in range(len(solucao1)):
    rota  = solucao1[i]
    rota_instantes = instantes1[i]
    print(f'----------------------------ROTA {i}----------------------------')
    for j in range( len(rota) ):
        print(rota[j])
        print(f'=>t[{j}]={rota_instantes[j]}\n')





#p.calcula_instantes_de_entrega(solucao1)
print("------------")
print(p.func_obj1(solucao1,instantes1))
print(p.func_obj2(solucao1,instantes1)) #IMPLEMENTAR BETA



print("----------------KMeansST----------------")
kmeans = KmeansST(1.0, 1.5, 2.0, 0.5, 0.5, velocidade_veiculo_m_s, clientes)

kmeans.calcular_distancias()
kmeans.print()




#print('###########################')

#solucao2 = p.criando_solucao_aleatoria_3(clientes)
#for rota in solucao2:
#    print('----------ROTA-----------')
#    for cliente in rota:
#        print(cliente)
#    print()


#print(clientes[0].calcula_distancia_clientes(clientes[1]) )



#p.set_numero_veiculos(5)
#p.set_capacidade_veiculo(3)
#p.set_velocidade_veiculo(4.7)
#p.set_custo_tranporte_por_km(2.5)
#p.set_custo_veiculo(3.7)

#p.set_numero_clientes(3)
#p.set_dados_cliente([['S' , 2 ,3], ["f" , 2 ,3 ]])

#p.set_qualidade_produto(0.4)
#p.set_ciclo_de_vida_produto(0.3)

#p.set_w1(10)
#p.set_w2(2)
#p.set_w3(15)

#p.print()

#p.criando_solucao(10)

#TESTANDO SOLUÇÂO
#s = Solucao(10)

#rota
#v1 = [2, 4, 10, 5, 7]
#v2 = [1, 3, 6]
#v3 = [8, 11, 9, 12]
#caminho = []
#caminho.append(v1)
#caminho.append(v2)
#caminho.append(v3)
#tam_rota = [len(v1),len(v2), len(v3)]
#n_veiculos = 3


#outros
#id = 25
#dist_percorrida = 5.0
#custo_objetivo = 1.2
#quali_objetivo = 3.5
#crow_1 = 10.5
#crow_2 = 13.5

#s.set_id(id)
#s.set_tamanho_rota_por_veiculo(tam_rota)
#s.set_numero_veiculos(n_veiculos)
#s.set_caminho_da_solucao(caminho)
#s.set_distancia_percorrida(dist_percorrida)
#s.set_custo_objetivo1(custo_objetivo)
#s.set_qualidade_objetivo2(quali_objetivo)
#s.set_crownding_distance_objetivo1(crow_1)
#s.set_crownding_distance_objetivo2(crow_2)

#s.print()

