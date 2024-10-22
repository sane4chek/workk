def get_multiplied_digits(number) -> int:
    str_number = (str(number))
    first = str_number[0]
    intFirst = int(first)
    if len(str_number) > 1:
        return int(intFirst * get_multiplied_digits(int(str_number[1:])))  # рекурсивный вызов
    else:
        return int(intFirst)  # базовый случай


result = get_multiplied_digits(40203)
print(result)
