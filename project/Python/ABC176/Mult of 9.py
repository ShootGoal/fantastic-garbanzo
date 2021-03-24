
N = int(input())
s = str(N)
array = list(map(int, s))
s_array = sum(array)
s_array2 = int(s_array)
s_array3 = s_array2 % 9
if s_array3 == 0:
    print("Yes")
else:
    print("No")
