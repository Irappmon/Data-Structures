def find_non_duplicate_number(list_of_numbers):
    """
    This Program accepts a list of numbers, which contains all numbers twice except one. Returns that one number
     which is single.
    :param list_of_numbers:
    :return: Number that didn't occur twice.
    """
    sign = 1
    sum = 0
    for number in list_of_numbers:
        sum += (number*sign)
        sign *= -1
    return abs(sum)


if __name__ == "__main__":
    list_of_numbers = [4, 3, 2, 2, 3, 4, 1]
    unpaired_number = find_non_duplicate_number(list_of_numbers)
    print(unpaired_number)
