from infrastructure.repositories.repositories_economic_data import Repositories_economic_data
from infrastructure.common.datetime_helper import now_jalali_str
from domain.entities.economicData import EconomicData
time = now_jalali_str()

economic_data = EconomicData(
    1404,
    150000,
    0.35,
    time
)

repo = Repositories_economic_data()

repo.add(economic_data)