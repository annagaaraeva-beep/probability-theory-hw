import random
from math import comb
import matplotlib.pyplot as plt
#part_3.2
random.seed(67)
n = 11
p = 0.6
theory = 0
for k in range(6, n+1):
    theory += comb(n,k)*p**k*(1-p)**(n-k)

#part_3.1
def ensemble_accuracy(N):
    ens_correct = 0
    for _ in range(N):
        y = random.randint(0,1)
        votes_for_1 = 0
        for j in range(n):
            is_correct = random.random() < p
            if is_correct:
                pred = y
            else:
                pred = 1-y
            votes_for_1 += pred
        if votes_for_1 > n/2:
            ens_pred = 1
        else:
            ens_pred = 0

        if ens_pred == y:
            ens_correct += 1 

    return ens_correct/N

#part_3.2
sizes = [100, 1000, 10000]
repeats = 300
results = []

for N in sizes:
    accs = []
    for r in range(repeats):
        accs.append(ensemble_accuracy(N))
    results.append(accs)

#part_3.3
print("теоретична ймовірність:", theory)
for i in range(len(sizes)):
    mean_acc = sum(results[i])/repeats
    print("N =", sizes[i], " середня точність:", mean_acc)

#part_3.4
plt.boxplot(results, labels=["100","1000","10000"])
plt.axhline(theory, color="red", linestyle="--", label="теоретична ймовірність")
plt.ylabel("емпірична точність ансамблю")
plt.title("розкид емпіричних точностей")
plt.legend()
plt.show()

#коментар
"""
Для всіх трьох N середня емпірична точність має бути дуже близькою до 0,7535.
Вона не зміщена вбік, а лише коливається навколо цього значення. 
Розкид швидко зменшується зі зростанням N.
Для малого N окремий набір може помітно відхилятися від теоретичного значення, 
а для великого N майже кожен набір дає точність, дуже близьку до 0,7535
"""