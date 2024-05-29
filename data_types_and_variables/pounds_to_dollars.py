from forex_python.converter import CurrencyRates

currency_rates = CurrencyRates()

amount_gbp = 100  # Example amount

rate_gbp_to_usd = currency_rates.get_rate('GBP', 'USD')

amount_usd = amount_gbp * rate_gbp_to_usd

print(f"{amount_gbp} GBP is equal to {amount_usd:.2f} USD")
