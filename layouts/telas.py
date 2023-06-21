import PySimpleGUI as sg
import pandas as pd
from util.fucaoSql import SqlFunction

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def telaInicial():

    layout = [
        [sg.Push(), sg.Text('MENU PRINCIPAL', size=(15,0), font=('Arial',12),justification='center'), sg.Push()],
        [sg.Push(),sg.Button('Relatório'),sg.Button('Status Agendamento'),sg.Push(),]

    ]
    return layout

def telaRelatorio():

    layout = [
        [sg.Push(), sg.Text('Relatorios', size=(15,0), font=('Arial',12),justification='center'), sg.Push()],
        [sg.Push(),sg.Button(''),sg.Push()]


    ]
    return layout

def statusAgendamento():
    df = SqlFunction.getbdStatusAgendamento()
    
    listValue= df.values.tolist()
    headerList= [
                'SOLICITAÇÃO'
                'STATUS',
                'PRODUTO',
                 'ORIGEM',
                 'DESTINO',
                 'AGENDAMENTO',
                 'HORA',
                 'DESCARGA',
                 'CAVALO',
                 'CARRETA 1',
                 'CARRETA 2',
                 'CNPJ',
                 'TRANSPORTADORA',
                 
                 ]

        
    layout = [
        [sg.Push(),sg.Text('Status de Agendamento', size=(25, 0), font=('Arial', 20), justification='center'), sg.Push()],
        [sg.Push(),sg.Text('STATUS:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Push()],
        [sg.Push(),sg.Text('PRODUTO:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Push()],
        [sg.Push(),sg.Text('Filtro 1:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Text('Filtro 1:'), sg.Input(),sg.Push()],
        [sg.Push(),sg.Text('_____________________________________________________________________________________________________', size=(300, 0), font=('Arial', 20), justification='center'), sg.Push()],
        [sg.Push(),sg.Button('Filtrar'),sg.Button('Limpar'),sg.Push()],
        [sg.Push(),sg.Table(listValue, headerList, def_col_width=20, auto_size_columns=True, max_col_width=35, justification='center', vertical_scroll_only=False,size=(0,40)),sg.Push()],
        [sg.Push(), sg.Button('Fechar'), sg.Push()]
    ]

    return layout
