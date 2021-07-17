import xlsxwriter
import numpy as np

def write_res(path, p, res):
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


    ##
    results = np.copy(res.F)
    n = results.shape[0]

    for i in range(n):
        worksheet.write(i , 4, results[i][0])
        worksheet.write(i, 5, -1*results[i][1])



    print(res.F.shape)
    print(n)


    workbook.close()