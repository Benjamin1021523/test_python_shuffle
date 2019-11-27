arr_len = 100
shuffles = 100000

a = [i for i in range(arr_len)]

import random

with open('.test.json', 'w') as f:
    f.write('{"a":[\n')
    for _ in range(shuffles):
        random.shuffle(a)
        f.write("{}".format(a))
        f.write(',\n')
    random.shuffle(a)
    f.write("{}".format(a))
    f.write('\n]}')

import json

arr = json.loads(open('.test.json', 'r').read())['a']

def func():
    result = []
    for i in range(len(a)):
        result.append([0] * len(a))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            result[ arr[i][j] ][j] += 1
    m = []
    M = []
    for i in result:
        m.append(min(i))
        M.append(max(i))
    print(min(m), "{}%".format(abs(min(m) - shuffles / arr_len) / (shuffles / arr_len) * 100), sep='\t')
    print(max(M), "{}%".format(abs(max(M) - shuffles / arr_len) / (shuffles / arr_len) * 100), sep='\t')

print("陣列長度：{}，洗牌次數：{}".format(arr_len, shuffles))
print("期望值：{}，每個元素平均應該在每個索引出現這個次數".format(shuffles / arr_len))
func()
