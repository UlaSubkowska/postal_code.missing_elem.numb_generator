# PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
#
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

def missing_elements(input_list, n):
    element = 1
    end = n
    list_of_missing = []

    while element <= end:
        if element not in input_list:
            list_of_missing.append(element)
        element += 1
    return list_of_missing


print(missing_elements([2, 3, 7, 4, 9], 10))
