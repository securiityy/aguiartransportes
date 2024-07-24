import sqlite3
import csv
from random import randint
from json import dump
from flask import(
    Flask,
    send_file,
    request,
    redirect,
    Blueprint,
    render_template,
)
from . import ip

bp = Blueprint('/downloadfile', __name__)

@bp.route('/downloadfile', methods=['GET'])
def downloadfile():
    conn = sqlite3.connect('./aguiartransportes/empresa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM services;")
    dados = cursor.fetchall()
    with open('./aguiartransportes/flaskr/downloadfile/empresa.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([i[0] for i in cursor.description])
        escritor.writerows(dados)
    conn.commit()
    conn.close()
    path = "./downloadfile/empresa.csv"
    return send_file(path, as_attachment=True)
    return redirect('/homephone')




