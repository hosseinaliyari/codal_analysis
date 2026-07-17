import finpy_tse as tse
from infrastructure.common.DatetimeHelper import DatetimeHelper

class DownloadMarketCap:
    
    def download_market_cap():
        data= tse.Get_MarketWatch(save_excel=False)
        df=data[0]
        df['bt']=10000000000
        df['Value']=df['Value']/df['bt']
        df['Market Cap']=df['Market Cap']/df['bt']
        df['Market Cap']=round(df['Market Cap'])
        df=df[['Final','Final(%)','Market Cap']]
        df=df.filter(items=["Ticker","Final","Final(%)","Market Cap"])
        df["UpdateDate"]=DatetimeHelper.now_jalali_str()
        df=df.reset_index()
        return df