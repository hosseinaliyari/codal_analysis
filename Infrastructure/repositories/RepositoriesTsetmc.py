from infrastructure.tsetmc.market_cap import Market_Cap
from infrastructure.connection.connection_text import get_connection

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

def update_market_value():
    market = Market_Cap()
    rows = list(market.itertuples(index=False, name=None))
    conn = get_connection()
    conn.executemany(query, rows)
    conn.commit()
    conn.close()