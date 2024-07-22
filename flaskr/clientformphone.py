from random import randint
from json import dump
from flask import(
    Flask,
    request,
    redirect,
    Blueprint,
    render_template,
)
from . import ip

bp = Blueprint('clientformphone', __name__)

@bp.route('/clientformphone', methods=['GET', 'POST'])
def clientformphone():
    if request.method  == 'POST':
        mydict = {
            'tipo':request.form.to_dict()['tipo'],
            'solicitacao':request.form.to_dict()['solicitacao'],
            'data':request.form.to_dict()['data'],
            'centrodecusto':request.form.to_dict()['centrodecusto'],
            'solicitante':request.form.to_dict()['solicitante'],
            'descricao':request.form.to_dict()['descricao'],
            'empregados':request.form.to_dict()['empregados'],
            'motorista':'',
            'veiculo':'',
            'placa':'',
            'kminicial':'',
            'kmfinal':'',
            'kmrodado':'',
            'horainicio':'',
            'horafinal':'',
            'horatotal':'',
            'statuscliente':'on',
            'statusmotorista':'off',
            'id':randint(100_000_000_000_000 ,999_990_999_999_999)
        }
        with open(f'./aguiartransportes/flaskr/proc/{mydict["id"]}','w') as file:
            dump(mydict, file, indent=4)

        with open(f'./aguiartransportes/flaskr/index.html','r') as pagina:
            paginaweb = pagina.read()

        with open(f'./aguiartransportes/flaskr/templates/prochtml/{mydict["id"]}.html','w') as file:
            file.write(f"""{paginaweb}""")

        return redirect('/homephone')


    return render_template('clientformphone.html', myip=ip.myip())



