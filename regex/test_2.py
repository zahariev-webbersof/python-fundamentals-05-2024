import re


class CreditCardValidator:
    def __init__(self):
        self.patterns = {
            'visa': r"^4[0-9]{12}(?:[0-9]{3})?$",
            'mastercard': r"^(5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[0-1][0-9]|2720)[0-9]{12}$",
            'amex': r"^3[47][0-9]{13}$",
            'diners': r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
            'discover': r"^6(?:011|5[0-9]{2})[0-9]{12}$",
            'jcb': r"^(?:2131|1800|35\d{3})\d{11}$"
        }
        self.card_types = {
            'visa': 'Visa',
            'mastercard': 'MasterCard',
            'amex': 'American Express',
            'diners': 'Diners Club',
            'discover': 'Discover',
            'jcb': 'JCB'
        }

    def validate_credit_card(self, card_number):
        for card_type, pattern in self.patterns.items():
            if re.match(pattern, card_number):
                return True, self.card_types[card_type]
        return False, None


# Example usage
cards = [
    "4111111111111111",  # Visa
    "5500000000000004",  # MasterCard
    "340000000000009",  # American Express
    "30000000000004",  # Diners Club
    "6011000000000004",  # Discover
    "3530111333300000",  # JCB
    "1234567890123456",
    "0000000000000000"# Invalid card number

]

validator = CreditCardValidator()

for card in cards:
    validity, card_type = validator.validate_credit_card(card)
    if validity:
        print(f"Card: {card} is a valid {card_type}")
    else:
        print(f"Card: {card} is invalid")
