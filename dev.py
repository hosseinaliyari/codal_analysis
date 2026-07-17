from application.use_cases.UseCaseUpdateMarket import UpdateMarketUseCase

print("0 -- Download MarketCap & Save")
print("1 -- Download MarketCap & Save")
x = int(input("Enter Number : "))
if x == 0 :
    UpdateMarketUseCase.execute()
