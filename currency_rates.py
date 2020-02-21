from forex_python.converter import CurrencyRates   
from forex_python.converter import CurrencyCodes

which_currency_from = input('FROM CURRENCY:').upper()
which_currency_to = input('TO CURRENCY:').upper()

convert_amount = input('AMOUNT:')
convert_amount = int(convert_amount)

currency = CurrencyRates()
currency_symbol = CurrencyCodes().get_symbol(which_currency_to)

currency_converted = currency.convert(which_currency_from, which_currency_to, convert_amount )
currency_converted = round(currency_converted, 2)

print(currency_symbol + ' ' + str(currency_converted))


