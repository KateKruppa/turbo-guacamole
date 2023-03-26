# 1 задача

x = [3, 4, 5, 6, 7, 8] #задаем список
print('введите число от -6 до 5') #просим ввести число
n = int(input()) #n - число, которое ввел человек


def tess(x, n):  #создаем функцию
    return x[n]  # просим вернуть элемент под номером n


print(tess(x, n))  # выводим элемент под номером, который запрашивали

# 2 задача

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('введите число от 0 до 8')
N = int(input())


def tess(x, N):
    return x[N] ** N  # возвращаем в код элемент под номером n, в степени n


print(tess(x, N))  # выводим получившееся значение

# 3 задача

print('введите предложение или слово')
s = input()  # задаем строку
print('введите букву, номер которой хотите найти')
g = input()
k = 0  # задаем переменную равную нулю
i = ()


def poisk(s, g, k=0):
    for i in range(len(s)):  # бегаем по списку равному по длине заданной строки#
        if s[i] == g:  # если нашли нужную букву, то#
            k += 1  # прибавляем 1 к переменной#
            if k == 2:  # если переменная равна 2, то#
                return i # возвращаем номер второй нужной буквы в списке


print(poisk(s, g)) # выводим этот номер, если буква встречается один раз, то выводит None

# 4 задача

s = '101011000'  # задаем строку
r = s[::-1]  # переворачиваем строку
k = 0  # задаем переменную количества нулей равную нулю


for i in range(len(s)):
    if r[i] == '0':  # если нашли ноль, то
        k = k + 1  # к переменной прибавляем 1
    if r[i] == '1':  # если нашли 1, то
        break  # останавливаем наш алгоритм


print(k)  # вывод количества нулей

# 5 задача

s = 'нажал кабан на баклажан'  # задаем строку
print(s)  # вывод входной строки для удобства
r = s[::-1]  # переворачиваем строку
print(r)  # вывод перевернутой строки

# 6 задача

print('введите ряд чисел через пробел')
massivprim = input().split() # принимаем список
massivprim2 = list(map(int, massivprim)) # переводим все элементы из строк в числа


if len(set(massivprim2)) == 1: # все одинаковые числа записываются в множество, если таких множеств 1, то
    print('True') # выводим тру
else:
    print('False') # если не одно, то фолс

# 7 задача

print('введите пароль')
password = input()


def bolshbukv(password):
    for d in password:
        if d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':  # проверяем есть ли в строке большие латинские буквы
            return True
    return False


def malbukv(password):
    for d in password:
        if d in 'abcdefghijklmnopqrstuvwxyz': # проверяем есть ли в строке маленькие латинские буквы
            return True
    return False


def kakietocifri(password):
    for g in password:
        if g in '1234567890': # проверяем есть ли в строке цифры
            return True
    return False


def vsevmeste(password):
    if len(password) < 16:
        return False

    if not bolshbukv(password):
        return False

    if not malbukv(password):
        return False

    if not kakietocifri(password):
        return False
    return True # прогоняем строку по всем параметрам, если хотя бы по одному не подходит, то выводим фолс, если пароль суперский - тру


print(vsevmeste(password))

# 8 задача

s = [1, 2, [3, 4], 5, [6, [7, 8]], 9]


def flatten(d):
    a = []
    for i in d:
        if isinstance(i,list): # проверяем элемент списка по типу, если встретили список, то
            a.extend(flatten(i)) # добавляем его элементы в а
        else:
            a.append(i) # в противном случае просто добавляем элемент в а
    return a


print(flatten(s))

# 9 задача

q = {'a': 5, 'b': 2, 'c': 9, 'd': 4, 'e': 6, 'f': 7}


def charon(v):
    l = 0
    n = 0
    for i in v:
        if v[i] > l:
            l = v[i] # если элемент больше переменной, то записываем его в переменную
            n = i # сюда записываем ключ самого большого элемента
    return n, l


print(charon(q))

# 10 задача

X = [1,3,2,3,2,4]


def garage(q):
    w = {} # создаем словарь
    for i in q:
        if i in w.keys():
            w[i] += 1 # если i уже есть в словаре, то прибавляем 1
        else:
            w[i] = 1 # если нет - приравниваем к 1
    return [e for e in q if w[e] > 1] # возвращаем е, которая бежит по списку, если в словаре этот элемент больше 1, т.е. встречается не один раз


print(garage(X))