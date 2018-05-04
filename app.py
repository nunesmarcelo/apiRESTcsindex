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
        reader = csv.reader(ficheiro, delimiter=',', quoting=csv.QUOTE_NONE)
        lista = []
        for read in reader:
            lista.append(read)
        return lista


@app.route('/')
def landing():
    return "Para requisitar número de conferencias em uma area, acesse: =>  " \
           "<a href=\"buscar_conferencias_por_area/nomedaarea/NOMEDACONFERENCIA\"> " \
           "127.0.0.1:5000/buscar_conferencias_por_area/nomedaarea/NOMEDACONFERENCIA" \
           " </a>"


@app.route('/buscar_conferencias_por_area/<string:area>/<string:conferencia>', methods=['GET', 'POST'])
def data(area, conferencia):
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
            if arquivo[0] == conferencia:
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
        # return str(quantidade_conferencias)
    else:
        abort(404)

# Allow the filename to be included in the path
@app.route('/risky_csv_sender/<filename>')
def csv_sender(filename):
    # Make sure that they cannot request files outside of your CSV DIR
    if re.search(r'/', filename) or re.search(r'^\.', filename):
        return "Illegal Filename, File Not Found", 404

    full_filename = CSV_DIR + filename
    return flask.send_file(full_filename,
                           mimetype='text/csv',
                           as_attachment=True,
                           attachment_filename=filename
                           )


@app.route('/safer_faster_simpler_file_sender/<filename>')
def safe_csv_sender(filename):
    return flask.send_from_dir(filename,
                               mimetype='text/csv',
                               as_attachment=True,
                               attachment_filename=filename
                               )


if __name__ == '__main__':
    app.run()
