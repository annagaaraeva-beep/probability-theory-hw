from math import comb
import matplotlib.pyplot as plt

n = 11

def G(p):
    m = (n-1)//2
    total = 0
    for k in range(m+1, n+1):
        total += comb(n, k)*p**k*(1-p)**(n-k)
    return total

# part_5.1(a)
ps = []
gs = []
for i in range(1001):
    p = i/1000
    ps.append(p)
    gs.append(G(p))

plt.figure()
plt.plot(ps, gs)
plt.axvline(0.5, color="gray", linestyle=":")
plt.xlabel("p")
plt.ylabel("G_11(p)")
plt.title("точність ансамблю з 11 незалежних класифікаторів")
plt.grid(True)

#коментар
"""
Функція має S-подібну форму.
На проміжку [0, 0.5] вона є опуклою вниз, а на проміжку [0.5, 1] - опуклою вгору.
Точка p = 0.5 є точкою перегину.
"""

# part_5.5(b)
p_bar = 0.6


def A(q, d):
    p0 = p_bar+q*d
    p1 = p_bar-(1-q)*d
    return (1-q)*G(p0)+q*G(p1)


ds = []
for i in range(501):
    ds.append(i/1000)       
A_q04 = []
A_q01 = []
for d in ds:
    A_q04.append(A(0.4, d))
    A_q01.append(A(0.1, d))

plt.figure()
plt.plot(ds, A_q04, label="q = 0.4")
plt.plot(ds, A_q01, label="q = 0.1")
plt.axhline(G(p_bar), color="red", linestyle="--", label="G_11(0.6)")
plt.xlabel("d = p0 - p1")
plt.ylabel("A")
plt.title("точність ансамблю при p_bar = 0.6")
plt.legend()
plt.grid(True)

plt.show()