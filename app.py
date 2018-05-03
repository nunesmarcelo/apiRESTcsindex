from flask import Flask,request, make_response
import flask
import re
import csv
import StringIO

app = Flask(__name__)


#MÉTODO PADRÃO - ATIVA O BOTÃO PARA TESTES
@app.route('/')
def landing():
    return """<form action="data" method="post">
            <input type="submit" name="submit" value="Get Data">
         </form>"""


# MÉTODO PARA CRIAÇÃO DA PLANILHA CSV
@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        if request.form['submit'] == 'Get Data':
            csvlist = [['item 1', 'item2'], ['box1', 'box2']]

            si = StringIO.StringIO()
            cw = csv.writer(si)
            cw.writerows(csvlist)
            output = make_response(si.getvalue())
            output.headers["Content-Disposition"] = "attachment; filename=export.csv"
            output.headers["Content-type"] = "text/csv"
            return output



#MÉTODO PARA BAIXAR A PLANILHA DO DIRETÓRIO
CSV_DIR = 'CSIndex\\data\\'

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
