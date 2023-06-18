# задача 1

n = int(input())
purchases = {}

for i in range(n):
    buyer, item, quantity = input().split()
    if buyer not in purchases:
        purchases[buyer] = {}
    purchases[buyer][item] = purchases[buyer].get(item, 0) + int(quantity)

for buyer, items in purchases.items():
    print(buyer + ":")
    for item, quantity in items.items():
        print(item, quantity)

# задача 2

countries = []
while True:
    country = input()
    if country == "СТОП":
        break
    countries.append(country)

unique_countries = set(countries)

for country in unique_countries:
    print(f"{country} встречается в строках:", end=" ")
    for i in range(len(countries)):
        if countries[i] == country:
            print(i, end=" ")
    print()

# задача 3

numbers = [3, 5, 6, 3, 7, 0, 2, 8, 7, 9, 1, 4]

count = 0

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        count += 1

print("Количество элементов, которые больше двух своих соседей: ", count)

# задача 4

lst = list(map(int, input().split()))
k = int(input())

for i in range(k, len(lst) - 1):
    lst[i] = lst[i + 1]

lst.pop()

print(lst)

# задача 5

n = int(input())

arr = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    arr[i][n-i-1] = 1

for i in range(n):
    for j in range(n-i-1):
        arr[i][j] = 0

for i in range(n):
    for j in range(n-i, n):
        arr[i][j] = 2

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()

# задача 6

def read_last(lines, file):
    with open(file, 'r', encoding='UTF-8') as f:
        content = f.readlines()[-lines:]
        for line in content:
            print(line.strip())

read_last(3, 'article.txt')

# задача 7

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b

for num in fib(10):
    print(num)

# задача 8

word = input('Введите слово: ')

english_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
                'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
                'Y': 4, 'Z': 10}

russian_dict = {'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1, 'Й': 4, 'К': 2,
                'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5,
                'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3}

if word.isalpha() and all(letter.upper() in russian_dict for letter in word):
    score_dict = russian_dict
elif word.isalpha() and all(letter.upper() in english_dict for letter in word):
    score_dict = english_dict
else:
    print('Слово должно содержать только буквы одного алфавита')
    exit()

score = sum(score_dict[letter.upper()] for letter in word)

print(score)

# задача 9

st = "Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), то его читать не нужно"
def shortener(st):
    res = ""
    skip = 0
    for i in st:
        if i == "(":
            skip += 1
        elif i == ")":
            skip -= 1
        elif skip == 0:
            res += i
    return res
print (shortener(st))

# задача 10

lst = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7]

s = set()
for num in lst:
    if lst.count(num) > 1:
        s.add(str(num) * lst.count(num))
    else:
        s.add(num)

print(s)

# задача 11

def f(s, num):
    closest = None
    for val in s:
        if closest is None or abs(val - num) < abs(closest - num):
            closest = val
        elif abs(val - num) == abs(closest - num):
            closest = min(val, closest)
    return closest

print(f({1, 2,3, 4, 5}, 3))

# задача 12

def count_paths(x1, y1):
    if x1 == 8:
        return 1
    paths = 0
    if y1 > 1:
        paths += count_paths(x1 + 1, y1 - 1)
    if y1 < 8:
        paths += count_paths(x1 + 1, y1 + 1)
    return paths

print(count_paths(1, 4))

# задача 13

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

print(lcm(4, 6))

# задача 14

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(12, 18))

# задача 15

class A:
    '''Класс A'''

    def set_a(self, a):
        self.a = a

    def get_a(self):
        return self.a

print(A.__doc__)

obj1 = A()
obj1.set_a(10)
print(obj1.get_a())

obj2 = A()
obj2.a = 20
print(obj2.a)