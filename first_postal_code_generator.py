# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

def postal_code_generator(code1, code2):
    start_code = int(code1.replace('-', ''))
    end_code = int(code2.replace('-', ''))
    between_postal_codes = []

    while (end_code-1)>start_code:
        start_code += 1
        answer_code = str(start_code)
        between_postal_codes.append('{}-{}'.format(answer_code[:2], answer_code[2:]))
    return between_postal_codes


print(postal_code_generator('79-900', '80-155'))


