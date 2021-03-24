Q = int(input())
N_i = [int(input()) for i in range(Q)]
j = 0

for j in range(len(N_i)):
    k = 2
    sum_N = 0
    while k <= N_i[j]:
        if N_i[j] % k == 0:
            sum_N += N_i[j] / k
        k += 1
    if sum_N == N_i[j]:
        print("perfect")
    elif abs(sum_N - N_i[j]) == 1:
        print("nearly")
    else:
        print("neither")
    j += 1

print("")
