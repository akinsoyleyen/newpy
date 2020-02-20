from forex_python.converter import CurrencyRates   
from forex_python.converter import CurrencyCodes

def usd_to_try():
    
    currency = CurrencyRates()
    currency_symbol = CurrencyCodes().get_symbol('USD')


    convert_amount = input('How much money would you like to convert?')
    convert_amount = int(convert_amount)

    usd_to_try_converter = currency.convert('USD', 'TRY', convert_amount )

    print(currency_symbol + str(usd_to_try_converter))

def usd_to_try()


