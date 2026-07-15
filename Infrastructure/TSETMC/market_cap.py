from infrastructure.common.datetime_helper import now_jalali_str
import finpy_tse as tse

def Market_Cap():
    data= tse.Get_MarketWatch(save_excel=False)
    df=data[0]
    df['bt']=10000000000
    df['Value']=df['Value']/df['bt']
    df['Market Cap']=df['Market Cap']/df['bt']
    df['Market Cap']=round(df['Market Cap'])
    df=df[['Final','Final(%)','Market Cap']]
    df=df.filter(items=["Ticker","Final","Final(%)","Market Cap"])
    df["UpdateDate"]=now_jalali_str()
    df=df.reset_index()
    return df