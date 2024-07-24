from json import(
    dump,
    loads,
)
import sqlite3
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

bp = Blueprint('tabela', __name__)

@bp.route('/tabela', methods=['GET'])
def tabela():
    con = sqlite3.connect('./aguiartransportes/empresa.db')
    cur = con.cursor()
    cur.execute('select * from services;')
    data = cur.fetchall()
    con.commit()
    con.close()
    return render_template('tabela.html',data=data, myip=ip.myip())
