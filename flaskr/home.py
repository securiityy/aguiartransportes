from json import(
    dump,
    loads,
)
from os import listdir
from random import randint
from flask import(
    Flask,
    request,
    redirect,
    Blueprint,
    render_template,
)
from . import scriptdata
from . import ip

bp = Blueprint('home', __name__)

@bp.route('/home', methods=['GET'])
def home():
    lista = []
    for i in listdir('./aguiartransportes/flaskr/proc/'):
        with open(f'./aguiartransportes/flaskr/proc/{i}', 'r') as proc:
            x = [list(loads(proc.read()).values())]
        lista += x

    return render_template(
        'home.html',
        lista=lista,
        file=listdir('./aguiartransportes/flaskr/proc/'),
        data={
            'totalservicosrealizados': scriptdata.totalservicosrealizados(),
            'totalservicosnaorealizados': scriptdata.totalservicosnaorealizados(),
            'servicosrealizadoshoje': scriptdata.servicosrealizadoshoje(),
            'servicosrealizadosemsetedias': scriptdata.servicosrealizadosemsetedias(),
            'servicosrealizadosemtrintadias': scriptdata.servicosrealizadosemtrintadias(),
            'servicosrealizadosemumano': scriptdata.servicosrealizadosemumano(),
            'myip':ip.myip(),
        }
    )
