from reportlab.pdfgen import canvas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import sqlite3
import csv


from os import path,remove
from datetime import datetime, timedelta


def deletefile(filepath):
    if path.exists(filepath):
        remove(filepath)
    else:
        pass


def convert():
    data_de_hoje = datetime.today().date()
    data_de_sete_dias_atras = data_de_hoje - timedelta(days=30)
    data_de_hoje_formatada = data_de_hoje.strftime('%Y-%m-%d')
    data_de_sete_dias_atras_formatada = data_de_sete_dias_atras.strftime('%Y-%m-%d')
    con = sqlite3.connect('./aguiartransportes/empresa.db')
    cur = con.cursor() 
    cur.execute(f"""
    select *
    from services
    where data <= '{data_de_hoje_formatada}'
    and data >= '{data_de_sete_dias_atras_formatada}';
    """)
    dados = cur.fetchall()

    with open('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([i[0] for i in cur.description])
        writer.writerows(dados)
    con.commit()
    con.close()
################################################################################
#                               OPEN - Create graph                            #
################################################################################
def graph_one():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    contagem_produtos = df['data'].value_counts()
    plt.figure(figsize=(10, 5))
    contagem_produtos.plot(kind='bar', color='blue', width=0.8)
    plt.title('Quantidade de viagem por data em 30 dias.')
    plt.xlabel('data')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=-90)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-1.png')

def graph_two():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    contagem_produtos = df['solicitacao'].value_counts()
    plt.figure(figsize=(8, 5))
    contagem_produtos.plot(kind='bar', color='blue', width=0.8)
    plt.title('Quantidade por tipo de solicitanção em 30 dias.')
    plt.xlabel('Tipo de solicitação')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=-90)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-2.png')

def graph_three():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    contagem_produtos = df['tipo'].value_counts()
    plt.figure(figsize=(8, 5))
    contagem_produtos.plot(kind='bar', color='blue', width=0.8)
    plt.title('Quantidade por ( tipo ) em 30 dias.')
    plt.xlabel('Tipo')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=-90)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-3.png')

def graph_four():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    contagem_produtos = df['motorista'].value_counts()
    plt.figure(figsize=(8, 5))
    contagem_produtos.plot(kind='bar', color='blue', width=0.8)
    plt.title('Quantidade viagem por motorista em 30 dias.')
    plt.xlabel('Motorista')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=-90)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-4.png')

def graph_five():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    contagem_produtos = df['placa'].value_counts()
    plt.figure(figsize=(8, 5))
    contagem_produtos.plot(kind='bar', color='blue', width=0.8)
    plt.title('Quantidade viagem por veiculo em 30 dias.')
    plt.xlabel('Placa')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=-90)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-5.png')

def graph_six():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    contagem_produtos = df['solicitante'].value_counts()
    plt.figure(figsize=(8, 5))
    contagem_produtos.plot(kind='bar', color='blue', width=0.8)
    plt.title('Quantidade viagem por solitante em 30 dias.')
    plt.xlabel('Solitante')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=-90)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-6.png')

def graph_seven():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    contagem_produtos = df['centrodecusto'].value_counts()
    plt.figure(figsize=(8, 5))
    contagem_produtos.plot(kind='bar', color='blue', width=0.8)
    plt.title('Quantidade viagem por centrodecusto em 30 dias.')
    plt.xlabel('Solitante')
    plt.ylabel('Quantidade')
    plt.xticks(rotation=-90)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-7.png')

def graph_eight():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    plt.figure(figsize=(10, 10))
    df.groupby('solicitacao')['valorservico'].sum().plot(kind='pie', autopct='%1.0f%%', startangle=10)
    plt.title('Distribuição de Custos total em reais por solicitanção')
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-8.png')

def graph_nine():
    df = pd.read_csv('./aguiartransportes/flaskr/downloadfile/empresa30dias.csv')
    plt.figure(figsize=(10, 10))
    df.groupby('tipo')['valorservico'].sum().plot(kind='pie', autopct='%1.0f%%', startangle=10)
    plt.title('Distribuição de Custos total em reais por (Tipo)')
    plt.savefig('./aguiartransportes/flaskr/downloadfile/graph-9.png')



################################################################################
#                            CLOSE - Create graph                              #
################################################################################





def pdfgraph(c):
    # Titulo logo imagem.
    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/logo.jpeg', 200,730, width=200,height=90)

    # Texto relatorio.
    c.drawString(1,700,"      Este relatório oferece um resumo detalhado do desempenho de transporte da nossa empresa nos últimos")
    c.drawString(1,680,"   30 dias. Durante este período, monitoramos de perto nossa operação para garantir a eficiência, segurança ")
    c.drawString(1,659,"   e satisfação do cliente, refletidos em dados estatísticos detalhados disponíveis no documento. ")

    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-1.png', 0,480, width=300,height=150)
    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-2.png', 298,480, width=300,height=150)

    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-3.png', 0,330, width=300,height=150)
    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-4.png', 298,340, width=300,height=150)

    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-5.png', 0,180, width=300,height=150)
    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-6.png', 298,180, width=300,height=150)

    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-7.png', 0,20, width=300,height=150)

def pdftable(c):

    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-8.png', 0,530, width=300,height=300)
    c.drawInlineImage('./aguiartransportes/flaskr/downloadfile/graph-9.png', 298,530, width=300,height=300)





# gera as imagem e os dados para colocar no pdf
convert()
graph_one()
graph_two()
graph_three()
graph_three()
graph_four()
graph_five()
graph_six()
graph_seven()
graph_eight()
graph_nine()

# gera o pdf com os dados
c = canvas.Canvas('./aguiartransportes/flaskr/downloadfile/relatorio30dias.pdf')
pdfgraph(c)
c.showPage()
pdftable(c)
c.showPage()
c.save()

# deleta os arquivos depois de gerar o pdf
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-1.png')
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-2.png')
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-3.png')
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-4.png')
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-5.png')
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-6.png')
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-7.png')
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-8.png')
deletefile('./aguiartransportes/flaskr/downloadfile/./graph-9.png')
