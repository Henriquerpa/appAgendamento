import pandas as pd
import psycopg2 as pg
import datetime
import time
import win32com.client as win32
import datetime
import getpass

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



#_____________________________________________________________________________________________________________
HOST= '4.228.57.67'
DATA_BASE= 'db_powerautomate'
USER= 'postgres'
PASSWORD= 'pRxI65oIubsdTlf'


class SqlFunction:

    def getbd(tbName='agendamento_vibra',comparador='<>',valor_satatus='não enviado',nome_coluna='chave_sharepoint',ordem='DESC',qtLinha='100'):  
        con = pg.connect(host=HOST, database=DATA_BASE, user=USER, password=PASSWORD)
        cur = con.cursor()

        command = f'''SELECT * FROM sc_agendamentos.{tbName}
                WHERE {nome_coluna} {comparador} '{valor_satatus}'
                ORDER BY chave_sharepoint {ordem} LIMIT {qtLinha}

                                ;
                            '''
        

        cur.execute(command)
        con.commit()
        df = pd.read_sql(command, con)
        cur.close()
        con.close()

        return df  

    def getbdStatusAgendamento(tbName='agendamento_vibra',comparador='<>',valor_satatus='não enviado',nome_coluna='chave_sharepoint',ordem='DESC',qtLinha='100'):  
        con = pg.connect(host=HOST, database=DATA_BASE, user=USER, password=PASSWORD)
        cur = con.cursor()

        command = f'''SELECT 
        tipo_solicitacao,
        status,
        produto,
        origem,
        destino,
        data_agendamento,
        horario_agendamento,
        data_descarga,
        placa_cavalo,
        placa_carreta1,
        placa_carreta2,
        cnpj_transportadora,
        nome_transportadora
          
          FROM sc_agendamentos.{tbName}
                WHERE {nome_coluna} {comparador} '{valor_satatus}'
                ORDER BY chave_sharepoint {ordem} LIMIT {qtLinha}

                                ;
                            '''
        

        cur.execute(command)
        con.commit()
        df = pd.read_sql(command, con)
        cur.close()
        con.close()

        return df  
    
print(SqlFunction.getbdStatusAgendamento())


