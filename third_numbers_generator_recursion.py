#  ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

from decimal import Decimal

list_of_numbers = []
step = 0.5
end = 5.5


def numbers_generator(number):
    if number > end:
        return list_of_numbers
    else:
        list_of_numbers.append(Decimal(number))
        return numbers_generator(number + step)


print(numbers_generator(2))
