from infrastructure.tsetmc.DownloadMarketCap import DownloadMarketCap
from infrastructure.connection.ConnectionText import get_connection
import pandas as pd

class RepositoriesTsetmc:

    def get_Price_Tsetmc():
        query=("select * from Price")
        conn = get_connection()
        df = pd.read_sql_query(query,conn)
        conn.close()
        return df
    
    def update_market_value():
        query= ("""
                INSERT INTO Price
                (Symbol, Price, ChangePercent, MarketValue, UpdateDate)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(Symbol)
                DO UPDATE SET
                    Price = excluded.Price,
                    ChangePercent = excluded.ChangePercent,
                    MarketValue = excluded.MarketValue,
                    UpdateDate = excluded.UpdateDate;
                """)
        market = DownloadMarketCap.download_market_cap()
        rows = list(market.itertuples(index=False, name=None))
        conn = get_connection()
        conn.executemany(query, rows)
        conn.commit()
        conn.close()