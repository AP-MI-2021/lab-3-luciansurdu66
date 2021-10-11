def read_list():
    lst = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst


"Proprietatea 5"


def is_palindrome(x):
    """
    Verifică dacă un număr este palindrom
    :param x: număr întreg
    :return: Valoarea de adevăr in funcție de caz
    """
    copy = x
    y = 0
    while copy != 0:
        y = y * 10 + copy % 10
        copy = copy // 10
    if x == y:
        return True
    return False


def all_palindromes(lst):
    """
    Verifică dacă toate numerele dintr-o listă sunt palindroame
    :param lst: listă de numere întregi
    :return: Valoarea de adevăr în funcție de caz
    """
    for i in lst:
        if not is_palindrome(i):
            return False
    return True


def get_longest_all_palindromes(lst: list[int]) -> list[int]:
    """
    Determină cea mai lungă subsecvență de palindroame
    :param lst: Listă de numere întregi
    :return: Cea mai lungă subsecvență de palindroame
    """
    subarray = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_palindromes(lst[i:j+1]) and len(lst[i:j+1]) > len(subarray):
                subarray = lst[i:j+1]
    return subarray


"Proprietatea 17"


def is_below_average(lst: list[int], average: float):
    """
    Calculează și verifică dacă media numerelor nu depășește o valoare citită
    :param lst: Listă de numere întregi
    :param average: Număr real
    :return: Valoarea de adevăr în funcție de caz
    """
    suma = 0
    for x in lst:
        suma = suma + x
    if suma/len(lst) < average:
        return True
    return False


def get_longest_average_below(lst: list[int], average: float) -> list[int]:
    """
    Determină cea mai lungă subsecvență de numere a căror medie nu depășește o valoare citită
    :param lst: Listă de numere întregi
    :param average: Număr real
    :return: Cea mai lungă secvență de numere a căror medie nu depășește o valoare citită
    """
    subarray = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if is_below_average(lst[i: j + 1], average) and len(lst[i: j + 1]) > len(subarray):
                subarray = lst[i: j + 1]
    return subarray


"Teste"


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([16, 2332, 151, 99, 0, 2, 42, 4]) == [2332, 151, 99, 0, 2]
    assert get_longest_all_palindromes([12, 42, 23, 193, 52]) == []


def test_get_longest_average_below():
    assert get_longest_average_below([1, 2, 3], 3) == [1, 2, 3]
    assert get_longest_average_below([1, 2, 3], 2) == [1, 2]
    assert get_longest_average_below([1, 1, 1, 1, 1], 1) == []


def main():
    test_get_longest_all_palindromes()
    test_get_longest_average_below()
    lst = []
    while True:
        print('1. Citire date.')
        print('2. Determinare cea mai lungă subsecvență cu palindroame')
        print('3. Determinare cea mai lungă subsecvență cu suma numerelor mai mică ca o valoare citită')
        print('x. Ieșire')
        optiune = input('Dați opțiunea: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(get_longest_all_palindromes(lst))
        elif optiune == '3':
            average = float(input("Valoarea dată pentru medie"))
            print(get_longest_average_below(lst, average))
        elif optiune == 'x':
            break
        else:
            print("Opțiune greșită! Reîncercați!")


if __name__ == '__main__':
    main()
