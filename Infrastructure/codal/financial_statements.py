from infrastructure.common.to_english_digits import to_english_digits
import pandas as pd
import requests
import re
import json

Symbol = ['شبندر']
Start_date ='1405-01-01'
End_date = '1405-04-24'
dd, mm, yy = Start_date[8:10], Start_date[5:7], Start_date[2:4]
ddd, mmm, yyy =End_date[8:10], End_date[5:7], End_date[2:4]
    
def SeasonalRequest(n, dd, ddd, mm, mmm, yy, yyy): 
    seasonal_request = []
    page = [1, 2, 3]
    for p in page:
        adres = f'https://search.codal.ir/api/search/v2/q?&Symbol={n}&Audited=true&AuditorRef=-1&Category=1&Childs=false&CompanyState=-1&CompanyType=1&Consolidatable=true&FromDate=14{yy}%2F{mm}%2F{dd}&IsNotAudited=false&Length=-1&LetterType=-1&Mains=true&NotAudited=true&NotConsolidatable=true&PageNumber={p}&Publisher=false&ToDate=14{yyy}%2F{mmm}%2F{ddd}&TracingNo=-1&search=true'
        heder = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
        de_re = requests.get(url=adres, headers=heder).text
        #sleep(1)
        pattern = re.compile(r'"TracingNo":.*?"HasExcel"')
        de_re = re.findall(pattern, de_re)
        de_re = list(map(lambda x: x.replace(')', ''), de_re))
        de_re = list(map(lambda x: x.replace('(', ''), de_re))
        seasonal_request.extend(de_re)
    seasonal_request = [item.replace("اطلاعات و صورت‌های مالی میاندوره‌ای  دوره", "") for item in seasonal_request]
    seasonal_request = [item.replace("اطلاعات و صورت‌های مالی میاندوره‌ای تلفیقی دوره", "") for item in seasonal_request]
    seasonal_request = [item.replace("صورت‌های مالی  سال مالی منتهی به", " ۱۲ ماهه منتهی به ") for item in seasonal_request]
    seasonal_request = [item.replace("صورت‌های مالی تلفیقی سال مالی منتهی به", " ۱۲ ماهه منتهی به ") for item in seasonal_request]
    word_to_remove = ["کنترل", "هیئت", "زمانبندی"]
    seasonal_request = [item for item in seasonal_request if all(word not in item for word in word_to_remove)]
    return seasonal_request

def Profit_web(url_):
    heder = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    darkhst = requests.get(url=url_, headers=heder).text
    darkhst = darkhst.split('datasource = ')[1].splitlines()[0][:-1]
    jsondarkhst = json.loads(darkhst)['sheets'][0]
    tables = jsondarkhst['tables'][0]
    v1 = None
    v2 = None
    for cell in tables["cells"]:

        if cell["rowCode"] == 17 and cell["columnCode"] == 2:
            v1 = int(cell["value"])

        elif cell["rowCode"] == 17 and cell["columnCode"] == 3:
            v2 = int(cell["value"])
    return v1, v2

def Equity_web(url_):
    heder = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    darkhst = requests.get(url=url_, headers=heder).text
    darkhst = darkhst.split('datasource = ')[1].splitlines()[0][:-1]
    jsondarkhst = json.loads(darkhst)['sheets'][0]
    tables = jsondarkhst['tables'][0]
    cells = tables['cells']
    for cell in cells:
        if (
            cell["rowCode"] == 39 and
            cell["columnCode"] == 2
        ):
            return int(cell["value"])
    return None

def financialStatements():
    rows = []
    for s in Symbol:
        seasonal_request  = SeasonalRequest(s, dd, ddd, mm, mmm, yy, yyy)
        for l in seasonal_request:
                title = l.split('"Title":"')[1:]
                title = title[0].split('"')[0]
                Title = to_english_digits(title)
                Parts = Title.split()
                gozaresh = l.split('"Url":"')[1:][0].split('","HasExcel"')[0]
                Profit_url = 'https://codal.ir' + gozaresh + '&&sheetId=1'
                Equity_url = 'https://codal.ir' + gozaresh + '&&sheetId=0'
                Profit, profit_last  = Profit_web(Profit_url)
                Equity = Equity_web(Equity_url)
                rows.append({
                            "Symbol":s,
                            "Title": Title,
                            "period": int(Parts[0]),
                            "date": Parts[4],
                            "year" : int(Parts[4].split('/')[0]),
                            "Profit": round(Profit/10000),
                            "profit_last" : round(profit_last/10000),
                            "Equity": round(Equity/10000)
                            })
    DataForSymbol = pd.DataFrame(rows)
    return DataForSymbol
