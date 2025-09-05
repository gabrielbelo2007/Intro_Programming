def credit_validation():
    card_number = input("Number: ")
    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 16:
        print("INVALID")
        return
    
    def luhn_check(number):
        total = 0
        reverse_digits = number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    def get_card_type(number):
        if (len(number) == 15 and number.startswith(('34', '37'))):
            return "AMEX"
        elif (len(number) == 16 and number.startswith(tuple(str(i) for i in range(51, 56)))):
            return "MASTERCARD"
        elif (len(number) in [13, 16] and number.startswith('4')):
            return "VISA"
        else:
            return "INVALID"

    if luhn_check(card_number):
        print(get_card_type(card_number))
    else:
        print("INVALID")

credit_validation()