from infrastructure.tsetmc.DownloadMarketCap import DownloadMarketCap
from infrastructure.repositories.RepositoriesTsetmc import RepositoriesTsetmc

class UpdateMarketUseCase:

    def execute():

        DownloadMarketCap.download_market_cap()

        RepositoriesTsetmc.update_market_value()

        return {
            "success": True,
            "message": "Market updated successfully."
        }