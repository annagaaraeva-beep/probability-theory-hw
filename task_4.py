import random
from math import comb

random.seed(67)
n = 11

def P(n, p):
    m=(n-1)//2
    total = 0
    for k in range(m+1, n+1):
        total += comb(n,k)*p**k*(1-p)**(n-k)
    return total
def run(N, q, p0, p1):
    y_true = []
    preds = []

    for i in range(N):
        y = random.randint(0,1)
        D = 1 if random.random() <q else 0
        if D == 1:
            p_corr = p1
        else:
            p_corr = p0

        row = []
        for j in range(n):
            is_correct = random.random() < p_corr  
            if is_correct:
                row.append(y)
            else:
                row.append(1-y)
        y_true.append(y)
        preds.append(row)

    accs = []
    for j in range(n):
        correct = 0
        for i in range(N):
            if preds[i][j] == y_true[i]:
                correct += 1
            accs.append(correct/N)

    ens_correct = 0
    for i in range(N):
        if sum(preds[i]) > n/2:
            ens_pred = 1
        else:
            ens_pred = 0
        if ens_pred == y_true[i]:
            ens_correct += 1
    ens_acc = ens_correct/N

    theory_single = (1-q)*p0+q*p1
    theory_ens = (1-q)*P(n,p0)+q*P(n,p1)
    print("q=", q, "p0=", p0, "p1=", p1)
    for j in range(n):
        print("  clf_" + str(j + 1) + ":", accs[j])
    print("  середня точність окремих:", sum(accs)/n)
    print("  теоретична точність окремого:", theory_single)
    print("  емпірична точність ансамблю:", ens_acc)
    print("  теоретична точність ансамблю:", theory_ens)
    print()

#part_4.5
run(500, 0.4, 0.8, 0.3)
#part_4.6
run(500, 0.1, 0.65, 0.15)

#коментар
""" 
За нових параметрів точність ансамблю стала вищою(0,7665), 
ніж точність незалежного ансамблю (0,7535).
"""