#  ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

from decimal import Decimal

def numbers_generator():
    start = 2
    end = 5.5
    step = Decimal(0.5)
    list_of_numbers = []

    number = Decimal(start)
    while number <= end:
        list_of_numbers.append(number)
        number += step
    return list_of_numbers


print(numbers_generator())




