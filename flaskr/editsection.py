import sqlite3
from os import remove
from random import randint
from json import dump,load
from flask import(
    Flask,
    request,
    redirect,
    Blueprint,
    render_template,
)
from . import ip

bp = Blueprint('editsection', __name__)

@bp.route('/editsection/<int:idsection>', methods=['GET','POST'])
def editsection(idsection):
    if request.method == 'POST':
        alll = request.form.to_dict()
        if 'salvar' in request.form.to_dict():
            if request.form.to_dict()['salvar'] == 'salvar':
                del alll['salvar']
                with open(f'./aguiartransportes/flaskr/proc/{idsection}','w') as file:
                    file.write('')
                    dump({**alll}, file, indent=4)
                #return redirect(f'/editsection/{idsection}') 

        elif request.form.to_dict()['salvarguardar'] == 'salvarguardar':
            del alll['salvarguardar']
            del alll['statuscliente']
            del alll['statusmotorista']
            conn = sqlite3.connect('./aguiartransportes/empresa.db')
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO services (
                tipo, solicitacao, data, centrodecusto, solicitante,
                descricao, empregados,motorista,veiculo,placa,kminicial,kmfinal,
                kmrodado,horainicio,horafinal,horatotal,id
                )
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)""",
                tuple(alll.values())
            )
            conn.commit()
            conn.close()
            remove(f'./aguiartransportes/flaskr/proc/{idsection}')
            remove(f'./aguiartransportes/flaskr/templates/prochtml/{idsection}.html')
            return redirect(f'/check')
           
    with open(f'./aguiartransportes/flaskr/proc/{idsection}', 'r') as file:
        return render_template(
            f'prochtml/{idsection}.html',
            idsection=idsection,
            data=load(file),
            myip=ip.myip(),
        )
 
