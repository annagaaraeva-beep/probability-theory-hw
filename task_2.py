import csv
from math import comb
#part_2.1
y_true = []
preds = []


with open("8b8ba14d-2d85-4240-afa0-e3f83b2a8d34.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        row = [int(x) for x in row]
        y_true.append(row[0])
        preds.append(row[1:])

N = len(y_true)
n = 11

ens = []
for row in preds:
    if sum(row) > n/2:
        ens.append(1)
    else:
        ens.append(0)

#part_2.2
accs = []
for j in range(n):
    correct = 0
    for i in range(N):
        if preds[i][j] == y_true[i]:
            correct += 1
        accs.append(correct/N)

for j in range(n):
    print("clf_"+str(j+1)+":", accs[j])
print("середня точність:", sum(accs)/n)
print("найкраща точність:", max(accs))

ens_correct = 0
for i in range(N):
    if ens[i] == y_true[i]:
        ens_correct += 1
ens_acc = ens_correct/N
print("Точність ансамблю:", ens_acc)

#part_2.3
p = 0.6
m = 5
theory = 0
for k in range(m+1, n+1):
    theory += comb(n,k)*p**k*(1-p)**(n-k)
print("теоритична ймовірність:", theory)
print("різниця", ens_acc - theory)

#коментар
"""
Теоретична ймовірність визначає математичне сподівання істинного результату,
обчислене для ідеальної математичної моделі з нескінченною кількістю спроб.
Файл містить лише одну реалізацію з N = 250 об'єктів. Тому відхилення на кілька 
відсотків від теоретичного значення цілком нормальне.
"""