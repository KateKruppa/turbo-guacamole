# 1 задача
import collections
from typing import List


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1):
    print('вывод 1 задачи: ',fibonacci(6))

# 2 задача

s = [1,2,3,4,5,6]
l = [4,5,6,7,8,9]

for i in s[:]:
    if i in l:
        s.remove(i)
        l.remove(i)

print('вывод 2 задачи: ',s, l)


#3 задача

d = [1,2,2,1,1,4,4,4,1,3,3,3,3,3]
D = {}

for i in d:
    D[i] = D.get(i, 0) + 1

f = {e: c for e, c in D.items() if c >= 4}

print('вывод 3 задачи: ', f)

#4 задача

s = [1, 2, [3, 4], 5, [6, [7, 8]], 9]


def flatten(d):
    a = []
    for i in d:
        if isinstance(i,list):
            a.append(sum(flatten(i)))
        else:
            a.append(i)
    return a


print('вывод 4 задачи:',flatten(s))

#5 задача

e = [1,2,3,1,2,3,4,5,1,2,3,4,6,7]
exp: list[int] = []
max = []

for i in range(len(e)-1):
    if e[i] < e[i+1]:
        exp.append(e[i])
    else:
        exp.append(e[i])
        if len(exp) > len(max):
            max = exp
            exp = []
        if e[i] < e[i+1]:
            exp.append(e[i])

if e[-1] > e[-2]:
    exp.append(e[-1])


if len(exp) > len(max):
    max = exp
    exp = []


print('вывод 5 задачи: ',max)

#6 задача

r = 'чмаф всех в чатике'
k = [i for i in range(len(r))]
print(''.join(r[i].upper() if (i % 2 != 0) else r[i] for i in k))

#7 задача

n = int(input())
w = n*2-1
a = [ ]

for i in range(w):
   a.append([])
   for j in range(w):
       d = n - abs(j+1-n) - abs(i+1-n)
       a[i].append( '*' if d > 0 else " ")

for l in a:
    print(*l,sep='')

#8 задача



#9 задача



#10 задача