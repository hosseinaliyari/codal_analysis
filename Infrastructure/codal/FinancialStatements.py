import pandas as pd
import requests
import re
import json
from infrastructure.common.ToEnglishDigits import to_english_digits

class FinancialStatements:

    def __init__(self, symbols, start_date, end_date):

        if isinstance(symbols, str):
            symbols = [symbols]

        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date

        self.start_day = start_date[8:10]
        self.start_month = start_date[5:7]
        self.start_year = start_date[2:4]

        self.end_day = end_date[8:10]
        self.end_month = end_date[5:7]
        self.end_year = end_date[2:4]
        self.headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36" }

    def SeasonalRequest(self,symbol): 
        seasonal_request = []
        page = [1, 2, 3]
        for p in page:
            adres = ("https://search.codal.ir/api/search/v2/q?"
                    f"&Symbol={symbol}"
                    "&Audited=true"
                    "&AuditorRef=-1"
                    "&Category=1"
                    "&Childs=false"
                    "&CompanyState=-1"
                    "&CompanyType=1"
                    "&Consolidatable=true"
                    f"&FromDate=14{self.start_year}%2F{self.start_month}%2F{self.start_day}"
                    "&IsNotAudited=false"
                    "&Length=-1"
                    "&LetterType=-1"
                    "&Mains=true"
                    "&NotAudited=true"
                    "&NotConsolidatable=true"
                    f"&PageNumber={p}"
                    "&Publisher=false"
                    f"&ToDate=14{self.end_year}%2F{self.end_month}%2F{self.end_day}"
                    "&TracingNo=-1"
                    "&search=true")
            heder = self.headers 
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

    def Profit_web(self, url_):
        heder = self.headers 
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


    def Equity_web(self,url_):
        heder = self.headers 
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

    def financialStatements(self):
        rows = []
        for s in self.symbols:
            seasonal_request  = self.SeasonalRequest(s)
            for l in seasonal_request:
                    title = l.split('"Title":"')[1:]
                    title = title[0].split('"')[0]
                    Title = to_english_digits(title)
                    Parts = Title.split()
                    gozaresh = l.split('"Url":"')[1:][0].split('","HasExcel"')[0]
                    Profit_url = 'https://codal.ir' + gozaresh + '&&sheetId=1'
                    Equity_url = 'https://codal.ir' + gozaresh + '&&sheetId=0'
                    Profit, profit_last  = self.Profit_web(Profit_url)
                    Equity = self.Equity_web(Equity_url)
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