import sqlite3
from os import listdir
from datetime import datetime, timedelta


def totalservicosrealizados():
    con = sqlite3.connect('./aguiartransportes/empresa.db')
    cur = con.cursor() 
    cur.execute('select count(tipo) from services;')
    totalservicosrealizados = cur.fetchone()
    con.commit()
    con.close()
    return totalservicosrealizados[0]

def totalservicosnaorealizados():
    totalservicosnaorealizados = listdir('./aguiartransportes/flaskr/proc/')
    return len(totalservicosnaorealizados)

def servicosrealizadoshoje():
    data_de_hoje = datetime.today().date()
    data_de_sete_dias_atras = data_de_hoje - timedelta(days=7)
    data_de_hoje_formatada = data_de_hoje.strftime('%Y-%m-%d')
    data_de_sete_dias_atras_formatada = data_de_sete_dias_atras.strftime('%Y-%m-%d')
    con = sqlite3.connect('./aguiartransportes/empresa.db')
    cur = con.cursor() 
    cur.execute(f'''
    select count(tipo)
    from services
    where data <= '{data_de_hoje_formatada}';
    ''')
    servicosrealizadoshoje = cur.fetchall()[0][0]
    con.commit()
    con.close()
    return servicosrealizadoshoje

def servicosrealizadosemsetedias():
    data_de_hoje = datetime.today().date()
    data_de_sete_dias_atras = data_de_hoje - timedelta(days=7)
    data_de_hoje_formatada = data_de_hoje.strftime('%Y-%m-%d')
    data_de_sete_dias_atras_formatada = data_de_sete_dias_atras.strftime('%Y-%m-%d')
    con = sqlite3.connect('./aguiartransportes/empresa.db')
    cur = con.cursor() 
    cur.execute(f'''
    select count(tipo)
    from services
    where data <= '{data_de_hoje_formatada}'
    and data >= '{data_de_sete_dias_atras_formatada}';
    ''')
    servicosrealizadosemsetedias = cur.fetchall()[0][0]
    con.commit()
    con.close()
    return servicosrealizadosemsetedias

def servicosrealizadosemtrintadias():
    data_de_hoje = datetime.today().date()
    data_de_sete_dias_atras = data_de_hoje - timedelta(days=30)
    data_de_hoje_formatada = data_de_hoje.strftime('%Y-%m-%d')
    data_de_sete_dias_atras_formatada = data_de_sete_dias_atras.strftime('%Y-%m-%d')
    con = sqlite3.connect('./aguiartransportes/empresa.db')
    cur = con.cursor() 
    cur.execute(f'''
    select count(tipo)
    from services
    where data <= '{data_de_hoje_formatada}'
    and data >= '{data_de_sete_dias_atras_formatada}';
    ''')
    servicosrealizadosemtrintadias = cur.fetchall()[0][0]
    con.commit()
    con.close()
    print('========================= ', servicosrealizadosemtrintadias)
    return servicosrealizadosemtrintadias

def servicosrealizadosemumano():
    data_de_hoje = datetime.today().date()
    data_de_sete_dias_atras = data_de_hoje - timedelta(days=365)
    data_de_hoje_formatada = data_de_hoje.strftime('%Y-%m-%d')
    data_de_sete_dias_atras_formatada = data_de_sete_dias_atras.strftime('%Y-%m-%d')
    con = sqlite3.connect('./aguiartransportes/empresa.db')
    cur = con.cursor() 
    cur.execute(f'''
    select count(tipo)
    from services
    where data <= '{data_de_hoje_formatada}'
    and data >= '{data_de_sete_dias_atras_formatada}';
    ''')
    servicosrealizadosemumano = cur.fetchall()[0][0]
    con.commit()
    con.close()
    return servicosrealizadosemumano


