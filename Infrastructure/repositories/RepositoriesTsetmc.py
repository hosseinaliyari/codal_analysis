from infrastructure.tsetmc.market_cap import Market_Cap
from infrastructure.connection.connection_text import get_connection
import pandas as pd


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
    market = Market_Cap()
    rows = list(market.itertuples(index=False, name=None))
    conn = get_connection()
    conn.executemany(query, rows)
    conn.commit()
    conn.close()