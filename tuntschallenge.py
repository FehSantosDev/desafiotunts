from __future__ import print_function
from google.oauth2 import service_account
import gspread
import time


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# The ID spreadsheet.
SPREADSHEET_ID = '1icxV7fCtMm4JE7D_qsTERKH2etFsJ_0U-VENFUuzlLM'
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
ac = gspread.authorize(creds)
works = ac.open_by_key(SPREADSHEET_ID)
wsheet = works.get_worksheet(0)


def approved_and_disapproved():
    line = 4
    column = 4
    x = 0

    while x < 25:
        p1 = float(wsheet.cell(line, column).value)
        column += 1
        p2 = float(wsheet.cell(line, column).value)
        column += 1
        p3 = float(wsheet.cell(line, column).value)
        column = 4
        m = (p1+p2+p3)/3

        absence = int(wsheet.cell(line, 3).value)
        if absence > 15:
            wsheet.update_cell(line, 7, 'Reprovado por Falta')
            wsheet.update_cell(line, 8, '0')
        else:
            if m < 50:
                wsheet.update_cell(line, 7, 'Reprovado por Nota')
                wsheet.update_cell(line, 8, '0')
            elif 50 <= m < 70:
                wsheet.update_cell(line, 7, 'Exame Final')
                #Cálculo Final
                naf = 100 - m
                wsheet.update_cell(line, 8, naf)
            elif m>= 70:
                wsheet.update_cell(line, 7, 'Aprovado')
                wsheet.update_cell(line, 8, '0')
        print ("{0:.2f}".format(m))
        line += 1
        x += 1
        #time.sleep(x) porque a API do Google limita o npumero de requisições por usuário por 2 minutos
        time.sleep(2)

approved_and_disapproved()
