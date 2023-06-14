#задача 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose(matrix))

#задача 2

a = [('Семен', 1, 'Катя', 'Ваулина'), ('Мыша', 13, 'Маша', 'Великжанина'), ('Котик', 13, 'Лера', 'Еловских'), ('Люцифер', 100, 'Настя', 'Вдовина'), ('Китти', 13, 'Катя', 'Ваулина')]


def optimize(pets):

    owners = {}

    for pet in pets:
        name, age, owner_name, owner_surname = pet
        owner = (owner_name, owner_surname)
        if owner not in owners:
            owners[owner] = []
        owners[owner].append((name, age))

    return owners

print(optimize(a))

#задача 3

import re
from collections import Counter
string = "Это строка с несколькими словами, слова не должны повторяться, но если они вдруг повторятся, то они должны не высветиться точно"
def rarest_word(phrase):
    words = re.findall(r'\w+', phrase.lower())
    count = Counter(words)
    rarest_count = count.most_common()[-1][1]
    rarest_words = [word for word, freq in count.items() if freq == rarest_count]
    return sorted(rarest_words)[0]
print(rarest_word(string))

#задача 4

string = "This is a sample string"
def most_common_letter(string):
    count = {}
    for c in string.lower():
        if c.isalpha():
            count[c] = count.get(c, 0) + 1
    max_count = max(count.values())
    return sorted([c for c in count if count[c] == max_count])[0]
print(most_common_letter(string))

#задача 5

string = "милашка как шалим"
def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])
print(is_palindrome(string))

#задача 6

arr = [1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
def sort_by_frequency(arr):
    count = {}
    for i, n in enumerate(arr):
        count[n] = count.get(n, [0, i])
        count[n][0] += 1
    return [pair[0] for pair in sorted(count.items(), key=lambda x: (-x[1][0], x[1][1]))]
print(sort_by_frequency(arr))

#задача 7

string = "Это строка с непрерывной последовательностью слов"
def has_sequence_of_three_words(string):
    words = string.split()
    for i in range(len(words) - 2):
        if words[i].isalpha() and words[i+1].isalpha() and words[i+2].isalpha():
            return True
    return False
print(has_sequence_of_three_words(string))

#задача 8

string = "abbcccddddeeeeeeeeeffffff"
def max_consecutive_length(string):
    max_len = 1
    cur_len = 1
    prev_char = string[0]
    for c in string[1:]:
        if c == prev_char:
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 1
        prev_char = c
    return max_len
print(max_consecutive_length(string))

#задача 9

expression = "2+2*2"
def evaluate_expression(expression):
    return eval(expression)
print(evaluate_expression(expression))

#задача 10

dicts_list = [{'a': 1, 'b': 2}, {'a': 3, 'c': 4}, {'d': 5}]
def merge_and_sum_dicts(dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            result[k] = result.get(k, 0) + v
    return result
print(merge_and_sum_dicts(dicts_list))