import math

def factorial(n):
   return math.factorial(n)
def c(n, r):
   return factorial(n) // (factorial(r) * factorial(n-r))
def hat_check(n):
    if n == 0: return 1
    if n == 1: return 0
    hc = [0]*(n+1)
    hc[0] = 1; hc[1] = 0
    for i in range(2, n+1):
        hc[i] = factorial(i) - sum([c(i, i-j) * hc[j] for j in range(i)])
    return hc[n]

if __name__ == "__main__":
    for i in range(50):
        print(i, hat_check(i))