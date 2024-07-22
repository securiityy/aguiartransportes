from flask import(
    Flask,
    send_file,
    request,
    redirect,
    Blueprint,
    render_template,
)
import subprocess
from time import sleep 

bp = Blueprint('/downloadcsvempresa', __name__)

@bp.route('/downloadcsvempresa', methods=['GET'])
def downloadcsvempresa():
    caminho_script = './aguiartransportes/flaskr/downloadfile/openpdf.py'
    process = subprocess.Popen(["python", caminho_script])
    path = "./downloadfile/empresa30dias.csv"
    sleep(2)
    for i in range(200000000):
        pass
    print('00000000000000000000')
    return send_file(path, as_attachment=True)
    return redirect('/homephone')

