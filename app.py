# encoding: utf-8
from flask import Flask, abort, make_response
import flask
import re
import csv
import StringIO

app = Flask(__name__)

CSV_DIR = 'data\\'

def ler_arquivo_para_list(nome_arquivo):
    with open(nome_arquivo, 'rU') as ficheiro:
        reader = csv.reader(ficheiro)
        lista = []
        for read in reader:
            lista.append(read)
        return lista


@app.route('/')
def landing():
    return "<h2> Página do GitHub </h2>" \
           "Acesse: <a href=\"https://github.com/nunesmarcelo/apiRESTcsindex\">https://github.com/nunesmarcelo/apiRESTcsindex </a>" \
           "<h3>Publicações </h3>" \
           "1-Para requisitar número de publicações de uma em uma area, acesse: =>  " \
           "<a href=\"buscar_conferencia_por_area/nomedaarea/NOMEDACONFERENCIA\"> " \
           "127.0.0.1:5000/buscar_conferencia_por_area/nomedaarea/NOMEDACONFERENCIA" \
           " </a> <hr>" \
           "2-Para requisitar número de publicações de todas as conferências  em uma area, acesse: =>" \
           "<a href=\"buscar_todas_conferencias_area/nomedaarea/\">" \
           "127.0.0.1:5000/buscar_todas_conferencias_area/nomedaarea/" \
           " </a> <hr>" \
           "<h3>Scores </h3>" \
           "3-Para requisitar os scores de todos os departamentos de uma area, acesse: =>" \
            "<a href=\"scores_departamentos_uma_area/nomedaarea/\">" \
           "127.0.0.1:5000/scores_departamentos_uma_area/nomedaarea/" \
           " </a> <hr>" \
           "4-Para requisitar os scores de um departamento de uma area, acesse: =>" \
           "<a href=\"score_departamento_uma_area/nomedaarea/nomedodepartamento\">" \
           "127.0.0.1:5000/score_departamento_uma_area/nomedaarea/nomedodepartamento" \
           " </a> <hr>" \
            "<h3>Professores </h3>" \
           "5-Para saber os professores de um departamento de uma area, acesse: =>" \
           "<a href=\"professores_departamento_uma_area/nomedaarea/nomedodepartamento\">" \
           "127.0.0.1:5000/professores_departamento_uma_area/nomedaarea/nomedodepartamento" \
           " </a> <hr>" \
           "6-Para saber todos os professores de uma area, acesse: =>" \
           "<a href=\"professores_departamentos_uma_area/nomedaarea/\">" \
           "127.0.0.1:5000/professores_departamentos_uma_area/nomedaarea/" \
           " </a> <hr>" \
           "<h3> Papers </h3>" \
           "7- Para listar todos os papers de uma area, acesse: =>" \
           "<a href=\"papers_uma_area/nomedaarea/\">" \
           "127.0.0.1:5000/papers_uma_area/nomedaarea/" \
           " </a> <hr>" \
           "8- Para listar todos os papers de um determinado ano de uma área, acesse: =>" \
           "<a href=\"papers_uma_area_ano/nomedaarea/ano\">" \
           "127.0.0.1:5000/papers_uma_area_ano/nomedaarea/ano" \
           " </a> <hr>" \
           "9- Para listar todos os papers de um departamento de uma área, acesse: =>" \
           "<a href=\"papers_uma_area_departamento/nomedaarea/departamento\">" \
           "127.0.0.1:5000/papers_uma_area_departamento/nomedaarea/departamento" \
           " </a> <hr>" \
           "10- Para listar todos os papers de um autor de uma área, acesse: =>" \
           "<a href=\"papers_uma_area_autor/nomedaarea/autor\">" \
           "127.0.0.1:5000/papers_uma_area_autor/nomedaarea/autor" \
           " </a> <hr>"


######################### AREA DE CONFERÊNCIAS #######################################
@app.route('/buscar_conferencia_por_area/<string:area>/<string:conferencia>', methods=['GET', 'POST'])
def buscar_conferencia_uma_area(area, conferencia):
    ok_area = 0
    quantidade_conferencias = 0

    # Verificacao da integridade do nome da area passada, ele deve estar na planilha areas.csv da pasta do arquivo
    areas = ler_arquivo_para_list("areas.csv")
    for item in areas:
        #Se o nome da area vinda estiver na planilha de areas, podemos prosseguir.
        if str(item)[2:-2] == area:
            ok_area = 1

    # CONFERE SE A AREA PASSADA ESTÁ ENTRE OS NOMES EXISTENTES DE ÁREAS, SENÃO, GERA O ERRO 404.
    if ok_area == 1:
        caminho = CSV_DIR+area+"-out-confs.csv"
        arquivos = ler_arquivo_para_list(caminho)

        for arquivo in arquivos:
            if conferencia:
                if arquivo[0] == conferencia:
                    quantidade_conferencias += int(arquivo[1])
            else:
                quantidade_conferencias += int(arquivo[1])

        saida = []
        saida.append(quantidade_conferencias)
        si = StringIO.StringIO()
        cw = csv.writer(si)
        cw.writerow(saida)
        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=export.csv"
        output.headers["Content-type"] = "text/csv"

        return output
    else:
        abort(404)


@app.route('/buscar_todas_conferencias_area/<string:area>', methods=['GET', 'POST'])
def buscar_todas_de_uma_area(area):
    return buscar_conferencia_uma_area(area, None)

############ FIM ÁREA CONFERENCIAS #################

######################### ÁREA DEPARTAMENTOS ######################################
@app.route('/scores_departamentos_uma_area/<string:area>', methods=['GET', 'POST'])
def scores_departamentos_uma_area(area):
    return score_departamento_uma_area(area, None)


@app.route('/score_departamento_uma_area/<string:area>/<string:departamento>/<string:departamento2>', methods=['GET', 'POST'])
def score_com_barra(area,departamento,departamento2):
    texto = departamento+"/"+departamento2
    return score_departamento_uma_area(area, texto)

@app.route('/score_departamento_uma_area/<string:area>/<string:departamento>', methods=['GET', 'POST'])
def score_departamento_uma_area(area,departamento):
    ok_area = 0

    # Verificacao da integridade do nome da area passada, ele deve estar na planilha areas.csv da pasta do arquivo
    areas = ler_arquivo_para_list("areas.csv")
    for item in areas:
        #Se o nome da area vinda estiver na planilha de areas, podemos prosseguir.
        if str(item)[2:-2] == area:
            ok_area = 1

    # CONFERE SE A AREA PASSADA ESTÁ ENTRE OS NOMES EXISTENTES DE ÁREAS, SENÃO, GERA O ERRO 404.
    if ok_area == 1:
        caminho = CSV_DIR+area+"-out-scores.csv"
        arquivos = ler_arquivo_para_list(caminho)

        si = StringIO.StringIO()
        cw = csv.writer(si)
        for arquivo in arquivos:
            if departamento:
                if arquivo[0] == departamento:
                    linha = arquivo[0]+','+arquivo[1]
                    cw.writerow([linha])
            else:
                linha = arquivo[0] + ',' + arquivo[1]
                cw.writerow([linha])

        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=export.csv"
        output.headers["Content-type"] = "text/csv"

        return output
    else:
        abort(404)

############ FIM ÁREA DEPARTAMENTOS #################

######################### ÁREA PROFESSORES ######################################
@app.route('/professores_departamentos_uma_area/<string:area>', methods=['GET', 'POST'])
def professores_departamentos_uma_area(area):
    return professores_departamento_uma_area(area, None)


@app.route('/professores_departamento_uma_area/<string:area>/<string:departamento>/<string:departamento2>', methods=['GET', 'POST'])
def professores_com_barra(area,departamento,departamento2):
    texto = departamento+"/"+departamento2
    return professores_departamento_uma_area(area, texto)

@app.route('/professores_departamento_uma_area/<string:area>/<string:departamento>', methods=['GET', 'POST'])
def professores_departamento_uma_area(area,departamento):
    ok_area = 0

    # Verificacao da integridade do nome da area passada, ele deve estar na planilha areas.csv da pasta do arquivo
    areas = ler_arquivo_para_list("areas.csv")
    for item in areas:
        #Se o nome da area vinda estiver na planilha de areas, podemos prosseguir.
        if str(item)[2:-2] == area:
            ok_area = 1

    # CONFERE SE A AREA PASSADA ESTÁ ENTRE OS NOMES EXISTENTES DE ÁREAS, SENÃO, GERA O ERRO 404.
    if ok_area == 1:
        caminho = CSV_DIR+area+"-out-profs.csv"
        arquivos = ler_arquivo_para_list(caminho)

        si = StringIO.StringIO()
        cw = csv.writer(si)
        for arquivo in arquivos:
            if departamento:
                if arquivo[0] == departamento:
                    linha = arquivo[0]+','+arquivo[1]
                    cw.writerow([linha])
            else:
                linha = arquivo[0] + ',' + arquivo[1]
                cw.writerow([linha])

        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=export.csv"
        output.headers["Content-type"] = "text/csv"

        return output
    else:
        abort(404)

############ FIM ÁREA PROFESSORES #################

######################### ÁREA PAPERS ######################################
@app.route('/papers_uma_area/<string:area>', methods=['GET', 'POST'])
def papers_uma_area(area):
    return papers_geral(area, None, None, None)

@app.route('/papers_uma_area_ano/<string:area>/<string:ano>', methods=['GET', 'POST'])
def papers_uma_area_ano(area,ano):
    return papers_geral(area, str(ano), None, None)

@app.route('/papers_uma_area_departamento/<string:area>/<string:departamento>', methods=['GET', 'POST'])
def papers_uma_area_departamento(area,departamento):
    return papers_geral(area, None, departamento, None)


@app.route('/papers_uma_area_departamento/<string:area>/<string:departamento>/<string:departamento2>', methods=['GET', 'POST'])
def papers_departamento_com_barra(area,departamento,departamento2):
    texto = departamento+"/"+departamento2
    return papers_geral(area,None, texto, None)

@app.route('/papers_uma_area_autor/<string:area>/<string:autor>', methods=['GET', 'POST'])
def papers_uma_area_autor(area, autor):
    return papers_geral(area, None, None, autor)

@app.route('/papers_geral/<string:area>/<string:ano>/<string:departamento>/<string:autor>', methods=['GET', 'POST'])
def papers_geral(area,ano,departamento,autor):
    ok_area = 0

    # Verificacao da integridade do nome da area passada, ele deve estar na planilha areas.csv da pasta do arquivo
    areas = ler_arquivo_para_list("areas.csv")
    for item in areas:
        #Se o nome da area vinda estiver na planilha de areas, podemos prosseguir.
        if str(item)[2:-2] == area:
            ok_area = 1

    # CONFERE SE A AREA PASSADA ESTÁ ENTRE OS NOMES EXISTENTES DE ÁREAS, SENÃO, GERA O ERRO 404.
    if ok_area == 1:
        caminho = CSV_DIR+area+"-out-papers.csv"
        arquivos = ler_arquivo_para_list(caminho)

        si = StringIO.StringIO()
        cw = csv.writer(si)
        for arquivo in arquivos:
            if not ano and not departamento and not autor:
                linha = arquivo[0]+','+arquivo[1]+','+arquivo[2]+','+arquivo[3]+','+arquivo[4]
                cw.writerow([linha])
            if ano and not departamento and not autor:
                if arquivo[0] == ano:
                    linha = arquivo[0] + ',' + arquivo[1] + ',' + arquivo[2] + ',' + arquivo[3] + ',' + arquivo[4]
                    cw.writerow([linha])
            if not ano and departamento and not autor:
                if arquivo[3] == departamento:
                    linha = arquivo[0] + ',' + arquivo[1] + ',' + arquivo[2] + ',' + arquivo[3] + ',' + arquivo[4]
                    cw.writerow([linha])
            if not ano and not departamento and autor:
                autores = arquivo[4].split('; ')
                for separado in autores:
                    if separado == autor:
                        linha = arquivo[0] + ',' + arquivo[1] + ',' + arquivo[2] + ',' + arquivo[3] + ',' + arquivo[4]
                        cw.writerow([linha])

        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=export.csv"
        output.headers["Content-type"] = "text/csv"

        return output
    else:
        abort(404)

############ FIM ÁREA PAPERS #################


if __name__ == '__main__':
    app.run()
