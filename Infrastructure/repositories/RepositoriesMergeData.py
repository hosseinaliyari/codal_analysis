from domain.entities.MergedData import MergedData
from domain.repositories.IMergedData import IMergedData
from infrastructure.connection.connection_text import get_connection
from processing.MergeData import MergeDataProcessor

class RepositoriesMergedData(IMergedData):

    def update_MergedData(self):
        query=("""
            INSERT OR IGNORE INTO MergedData
            (Symbol, Title, period, date, year, Profit, profit_last, Equity, Price, ChangePercent, MarketValue, UpdateDate, Adjustment,
            PortfolioChange, Comment, DollarNima, InterestRate, ProfitForecast, ValueForecast, PerDifference)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """)
        MergedData = MergeDataProcessor().merge_data()
        rows = list(MergedData.itertuples(index=False, name=None))
        conn = get_connection()
        conn.executemany(query, rows)
        conn.commit()
        conn.close()