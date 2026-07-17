from infrastructure.repositories.RepositoriesTsetmc import get_Price_Tsetmc 
from infrastructure.repositories.RepositoriesFinancialStatements import get_codal_financialStatements
from infrastructure.repositories.RepositoriesEconomicData import RepositoriesEconomicData
from infrastructure.repositories.RepositoriesFinancialAdjustments import RepositoriesFinancialAdjustments
import numpy as np

class MergeDataProcessor:
    def merge_data(self):
        price = get_Price_Tsetmc()
        codal = get_codal_financialStatements()
        ecodata = RepositoriesEconomicData().get_EconomicData()
        adjustments = RepositoriesFinancialAdjustments().get_FinancialAdjustments()
        merged = (
            codal
            .merge(price, on="Symbol", how="left")
            .merge(adjustments, on="Symbol", how="left")
            .merge(ecodata, left_on="year", right_on="Year",how="left" ).drop(columns=["Year","UpdateDate_y"])
        )
        merged["ProfitForecast"] = (
        np.select(
        [
            merged["period"] == 12,
            merged["period"] == 9,
            merged["period"] == 6,
            merged["period"] == 3
        ],
        [
            merged["Profit"] ,
            merged["Profit"] * 4 / 3,
            merged["Profit"] * 2,
            merged["Profit"] * 4

        ],
        default=merged["Profit"]
        )).round().astype(int)
        merged["ValueForecast"] =round((merged['Equity']+ ((merged["ProfitForecast"] +merged['Adjustment'] + merged['PortfolioChange'] ) / merged['InterestRate'])))
        merged["PerDifference"]= round((merged["MarketValue"]-merged['ValueForecast'])/merged['ValueForecast'],1)*100
        return merged 