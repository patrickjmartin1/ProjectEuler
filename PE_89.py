"""
We are going to make use of the code written here
https://www.codegrepper.com/code-examples/python/convert+number+to+roman+numerals+python

"""
import csv
import numpy as np


def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val


def int_to_roman(num):
    val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
    syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


if __name__ == "__main__":
    file_name = "p089_roman.txt"
    num_list = []

    with open(file_name, 'r') as f_id:
        reader = csv.reader(f_id)
        for row in reader:
            num_list.append(row[0])

    print(num_list)

    orig_len = np.array([])
    refined_len = np.array([])
    for rom in num_list:
        this_num = roman_to_int(rom)
        this_str_correct = int_to_roman(this_num)
        print("Original: {}, Refined: {}".format(rom, this_str_correct))
        orig_len = np.append(orig_len, len(rom))
        refined_len = np.append(refined_len, len(this_str_correct))

    delta = orig_len - refined_len
    print(delta)
    print(np.sum(delta))

# This is correct! Correct answer should be 743