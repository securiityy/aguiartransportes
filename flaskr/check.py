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

bp = Blueprint('/check', __name__)

@bp.route('/check', methods=['GET'])
def check():
    return render_template('check.html',myip=ip.myip())
