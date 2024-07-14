import sqlite3
from flask import (
    Flask,
)
from . import(
    clientform,
    home,
    editsection,
    tabela,
)
import subprocess
import threading
from os import makedirs
def execute():
    # Execute o arquivo Python
    caminho_script = './aguiartransportes/flaskr/bot/maindiscord.py'
    process = subprocess.Popen(["python", caminho_script])
    #time.sleep(15)
    # Mate o processo
    #os.kill(process.pid, signal.SIGTERM)
    print('processo finalizado!!!')


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Criar diretorios caso nao existao
    makedirs('./aguiartransportes/flaskr/proc',exist_ok=True)
    makedirs('./aguiartransportes/flaskr/templates/prochtml',exist_ok=True)

    #Views
    app.register_blueprint(clientform.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(editsection.bp)
    app.register_blueprint(tabela.bp)

    #DB create
    conn = sqlite3.connect('./aguiartransportes/empresa.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
        tipo TEXT NOT NULL,
        solicitacao TEXT NOT NULL,
        data TEXT NOT NULL,
        centrodecusto TEXT NOT NULL,
        solicitante TEXT NOT NULL,
        descricao TEXT NOT NULL,
        empregados TEXT NOT NULL,
        motorista TEXT NOT NULL,
        veiculo TEXT NOT NULL,
        placa TEXT NOT NULL,
        kminicial TEXT NOT NULL,
        kmfinal TEXT NOT NULL,
        kmrodado TEXT NOT NULL,
        horainicio TEXT NOT NULL,
        horafinal TEXT NOT NULL,
        horatotal TEXT NOT NULL,
        id TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

    #Bot discord
    #threading.Thread(target=execute).start()




    return app
