Q = int(input())
N_i = [str(input()) for i in range(Q)]
j = 0

for j in range(len(N_i)):
    if N_i[j][-1] == "o":
        N_i[j] += "es"
        print(N_i[j])
    elif N_i[j][-1] == "x":
        N_i[j] += "es"
        print(N_i[j])
    elif N_i[j][-1] == "s":
        N_i[j] += "es"
        print(N_i[j])
    elif N_i[j][-2:] == "ch":
        N_i[j] += "es"
        print(N_i[j])
    elif N_i[j][-2:] == "sh":
        N_i[j] += "es"
        print(N_i[j])

    elif N_i[j][-1] == "f":
        N_i[j] = N_i[j].rstrip("f")
        N_i[j] += "ves"
        print(N_i[j])
    elif N_i[j][-2:] == "fe":
        N_i[j] = N_i[j].rstrip("ef")
        N_i[j] += "ves"
        print(N_i[j])

    elif N_i[j][-1] == "y":
        if N_i[j][-1] != ("a" or "i" or "u" or "e" or "o"):
            N_i[j] = N_i[j].rstrip("y")
            N_i[j] += "ies"
            print(N_i[j])
    else:
        N_i[j] += "s"
        print(N_i[j])

    j += 1