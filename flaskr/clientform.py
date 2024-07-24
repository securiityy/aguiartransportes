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

bp = Blueprint('clientform', __name__)

@bp.route('/clientform', methods=['GET', 'POST'])
def clientform():
    if request.method  == 'POST':
        print('-----')
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
            'id':randint(100_000_000_000_000 ,999_990_999_999_999),
            'valorservico':'',
        }
        with open(f'./aguiartransportes/flaskr/proc/{mydict["id"]}','w') as file:
            dump(mydict, file, indent=4)

        with open(f'./aguiartransportes/flaskr/index.html','r') as pagina:
            paginaweb = pagina.read()

        with open(f'./aguiartransportes/flaskr/templates/prochtml/{mydict["id"]}.html','w') as file:
            file.write(f"""{paginaweb}""")

        return redirect('/home')


    return render_template('clientform.html', myip=ip.myip())

























