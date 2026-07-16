from domain.repositories.IFinancialAdjustments import IFinancialAdjustments
from infrastructure.connection.connection_text import get_connection


class RepositoriesFinancialAdjustments(IFinancialAdjustments):

    def add(self, financial_adjustment):

        conn = get_connection()

        conn.execute("""
            INSERT INTO FinancialAdjustments
            (
                Symbol,
                Adjustment,
                PortfolioChange,
                Comment
            )
            VALUES (?,?,?,?)
        """, (
            financial_adjustment.symbol,
            financial_adjustment.adjustment,
            financial_adjustment.portfolio_change,
            financial_adjustment.comment
        ))

        conn.commit()
        conn.close()


    def get_by_symbol(self, symbol):

        conn = get_connection()

        cursor = conn.execute("""
            SELECT
                Symbol,
                Adjustment,
                PortfolioChange,
                Comment
            FROM FinancialAdjustments
            WHERE Symbol=?
        """, (symbol,))

        row = cursor.fetchone()

        conn.close()

        return row


    def get_all(self):

        conn = get_connection()

        cursor = conn.execute("""
            SELECT
                Symbol,
                Adjustment,
                PortfolioChange,
                Comment
            FROM FinancialAdjustments
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows


    def update(self, financial_adjustment):

        conn = get_connection()

        conn.execute("""
            UPDATE FinancialAdjustments
            SET
                Adjustment=?,
                PortfolioChange=?,
                Comment=?
            WHERE Symbol=?
        """, (
            financial_adjustment.adjustment,
            financial_adjustment.portfolio_change,
            financial_adjustment.comment,
            financial_adjustment.symbol
        ))

        conn.commit()
        conn.close()


    def delete(self, symbol):

        conn = get_connection()

        conn.execute("""
            DELETE FROM FinancialAdjustments
            WHERE Symbol=?
        """, (symbol,))

        conn.commit()
        conn.close()