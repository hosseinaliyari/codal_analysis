class EconomicData:
    def __init__(self, year, dollar_nima, interest_rate, update_date):
        if not year:
            raise ValueError("year should  be not null!!")
        if not dollar_nima:
            raise ValueError("dollar_nima should  be not null!!")
        if not interest_rate:
            raise ValueError("interest_rate should  be not null!!")

        self.year = year
        self.dollar_nima = dollar_nima
        self.interest_rate = interest_rate
        self.update_date = update_date