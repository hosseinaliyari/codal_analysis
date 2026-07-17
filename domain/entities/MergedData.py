class MergedData:
    def __init__(
        self,
        Symbol,
        Title,
        period,
        date,
        year,
        Profit,
        profit_last,
        Equity,
        Price,
        ChangePercent,
        MarketValue,
        UpdateDate,
        Adjustment,
        PortfolioChange,
        Comment,
        DollarNima,
        InterestRate,
        ProfitForecast,
        ValueForecast,
        PerDifference
    ):
        self.Symbol = Symbol
        self.Title = Title
        self.period = period
        self.date = date
        self.year = year
        self.Profit = Profit
        self.profit_last = profit_last
        self.Equity = Equity
        self.Price = Price
        self.ChangePercent = ChangePercent
        self.MarketValue = MarketValue
        self.UpdateDate = UpdateDate
        self.Adjustment = Adjustment
        self.PortfolioChange = PortfolioChange
        self.Comment = Comment
        self.DollarNima = DollarNima
        self.InterestRate = InterestRate
        self.ProfitForecast = ProfitForecast
        self.ValueForecast = ValueForecast
        self.PerDifference = PerDifference