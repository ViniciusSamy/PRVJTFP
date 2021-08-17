import xlsxwriter
import numpy as np

def write_res(path, p, res, instancia_dir):
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 20)

    worksheet.write('A1', "Custo de Transporte por unidade de distância")
    worksheet.write('B1', p.get_custo_tranporte_unidade_distancia() )

    worksheet.write('A2', "Custo Fixo Veiculo")
    worksheet.write('B2', p.get_custo_veiculo() )

    worksheet.write('A3', "Numero máximo de veiculos")
    worksheet.write('B3', p.get_numero_max_veiculos())

    worksheet.write('A4', "Capacidade Veiculo")
    worksheet.write('B4', p.get_capacidade_veiculo())

    worksheet.write('A5', "Velocidade Veiculo")
    worksheet.write('B5', p.get_velocidade_veiculo())

    ####
    worksheet.write('A7', "Numero clientes")
    worksheet.write('B7', p.get_numero_clientes()-1)

    worksheet.write('A8', "Tempo de serviço")
    worksheet.write('B8', p.get_tempo_servico())


    ###
    worksheet.write('A10', "Qualidade do ṕroduto")
    worksheet.write('B10', p.get_qualidade_produto())

    worksheet.write('A11', "W1")
    worksheet.write('B11', p.get_w1())

    worksheet.write('A12', "W2")
    worksheet.write('B12', p.get_w2())

    worksheet.write('A13', "W3")
    worksheet.write('B13', p.get_w3())

    worksheet.write('A13', "W3")
    worksheet.write('B13', p.get_w3())

    worksheet.write('A14', "INSTACIA USADA")
    worksheet.write('B14', instancia_dir)


    ##
    results = np.copy(res.F)
    n = results.shape[0]

    for i in range(n):
        worksheet.write(i , 4, results[i][0])
        worksheet.write(i, 5, -1*results[i][1])



    #print(res.F.shape)
    #print(n)


    workbook.close()


def write_multi(path, p, numero_geracoes, tamanho_populacao, numero_de_execucoes, all_res, all_hypervolume, instancia_dir):
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 20)

    worksheet.write('A1', "Custo de Transporte por unidade de distância")
    worksheet.write('B1', p.get_custo_tranporte_unidade_distancia() )

    worksheet.write('A2', "Custo Fixo Veiculo")
    worksheet.write('B2', p.get_custo_veiculo() )

    worksheet.write('A3', "Numero máximo de veiculos")
    worksheet.write('B3', p.get_numero_max_veiculos())

    worksheet.write('A4', "Capacidade Veiculo")
    worksheet.write('B4', p.get_capacidade_veiculo())

    worksheet.write('A5', "Velocidade Veiculo")
    worksheet.write('B5', p.get_velocidade_veiculo())

    ####
    worksheet.write('A7', "Numero clientes")
    worksheet.write('B7', p.get_numero_clientes()-1)

    worksheet.write('A8', "Tempo de serviço")
    worksheet.write('B8', p.get_tempo_servico())


    ###
    worksheet.write('A10', "Qualidade do ṕroduto")
    worksheet.write('B10', p.get_qualidade_produto())

    worksheet.write('A11', "W1")
    worksheet.write('B11', p.get_w1())

    worksheet.write('A12', "W2")
    worksheet.write('B12', p.get_w2())

    worksheet.write('A13', "W3")
    worksheet.write('B13', p.get_w3())

    worksheet.write('A13', "W3")
    worksheet.write('B13', p.get_w3())

    worksheet.write('A15', "INSTACIA USADA")
    worksheet.write('B15', instancia_dir)

    worksheet.write('A17', "Numero de Geracoes")
    worksheet.write('B17', numero_geracoes)

    worksheet.write('A18', "Tamanho da População")
    worksheet.write('B18', tamanho_populacao)

    worksheet.write('A19', "Numero de Execuções")
    worksheet.write('B19', numero_de_execucoes)





    coluna = 5
    espacamento = 5
    i = 0
    for results in all_res:
        n = results.shape[0]

        worksheet.write(0, coluna, "EXECUCAO =")
        worksheet.write(0, coluna+1, i+1)

        worksheet.write(1, coluna, "OBJ1")
        worksheet.write(1, coluna + 1, "OBJ2")
        worksheet.write(1, coluna + 2, "HYPERVOLUME")

        for j in range(n):
            worksheet.write(j+2 , coluna, results[j][0])
            worksheet.write(j+2, coluna+1, results[j][1])

        worksheet.write(2, coluna+2, all_hypervolume[i])

        i += 1
        coluna += espacamento



    #print(res.F.shape)
    #print(n)


    workbook.close()