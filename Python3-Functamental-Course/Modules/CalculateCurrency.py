def CheckCurrency(amount,currency):
    if isinstance(currency,str):
        if currency == '$':
            return amount / 4000