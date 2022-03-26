from collections import Counter
mod=10**9+7  
a, b = list(map(int, input().split()))
a_score = list(map(int, input().split()))
b_score = list(map(int, input().split()))

def n_same_k_different(n, k):
    ans = []
    if k == 1:
        return [[n]]
    for i in range(n+1):
        for j in n_same_k_different(n-i, k-1):
            ans.append([i]+j)
    return ans


def divide_combination(n, k):
    dp = [1] * (n + 1)
    for i in range(1, k):
        for j in range(i+1, n+1):
            dp[j] += dp[j - i -1]
    return dp[-1]


def combi(score_list, n):
    cnt = Counter(score_list)
    # print(cnt)
    box_divide_list = n_same_k_different(n, len(cnt))
    # print(box_divide_list)
    s=0
    for inner in box_divide_list:
        m=1
        for i in range(len(inner)):
            # print(inner)
            # print(cnt.values())
            # print(i)
            if list(cnt.values())[i]==1: m*=divide_combination(inner[i], list(cnt.values())[i])%mod
        s+=m
    return s%mod

print(combi(a_score, sum(b_score)) * combi(b_score, sum(a_score)) % mod)