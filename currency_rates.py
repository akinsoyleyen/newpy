from forex_python.converter import CurrencyRates   

currency = CurrencyRates()

usd_dict = currency.get_rates('USD')

usd_to_try = usd_dict['TRY']




