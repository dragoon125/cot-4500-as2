# Neville's method
x = [3.6, 3.8, 3.9]
val = [1.675, 1.436, 1.318]
w = 3.7

neville = [[0.0 for _ in range(len(x))] for _ in range(len(x))]

for i in range(len(x)):
    neville [i][0] = val[i]

for i in range(1, len(x)):
    for j in range(1, i+1):
        term1 = (w - x[i - j]) * neville[i][j - 1]
        term2 = (w - x[i]) * neville[i - 1][j - 1]

        neville[i][j] = (term1 - term2) / (x[i] - x[i - j])

for i in range(len(x)):
    for j in range(i + 1):
        if(i == 1):
            if(j == i):
                print(format(neville[i][j]))
    #print()

print()

# Newton's forward method
xi = [7.2, 7.4, 7.5, 7.6]
fxi = [23.5492, 25.3913, 26.8224, 27.4589]

lim = len(xi)
diffs = [[0.0 for _ in range(lim)] for _ in range(lim)]

for i in range(lim):
    diffs[i][0] = fxi[i]

for i in range(1, lim):
    for j in range(1, i + 1):
        diffs[i][j] = (diffs[i][j-1] - diffs[i-1][j-1]) / (xi[i] - xi[i - j])

for i in range(lim):
    for j in range(i + 1):
        #if(i == 1):
        if(j == i and i > 0):
            if(i <= 3):
                print(format(diffs[i][j]))
print()

# f(7.3)

x = [7.2, 7.4, 7.5, 7.6]
val = [23.5492, 25.3913, 26.8224, 27.458]
w = 7.3

neville = [[0.0 for _ in range(len(x))] for _ in range(len(x))]

for i in range(len(x)):
    neville [i][0] = val[i]

for i in range(1, len(x)):
    for j in range(1, i+1):
        term1 = (w - x[i - j]) * neville[i][j - 1]
        term2 = (w - x[i]) * neville[i - 1][j - 1]

        neville[i][j] = (term1 - term2) / (x[i] - x[i - j])

for i in range(len(x)):
    for j in range(i + 1):
        if(i == 1):
            if(j == i):
                print(format(neville[i][j]))
print()

# Divided difference Hermite Polynomial approximation matrix
x = [3.6, 3.8, 3.9]
fx = [1.675, 1.436, 1.318]
fxi = [-1.195, -1.188, -1.182]

lim = len(x)
diffs = [[0.0 for _ in range(lim)] for _ in range(lim)]

for i in range(lim):
    diffs[i][0] = x[i]

for i in range(lim):
    diffs[i][1] = fx[i]

for i in range(lim):
    for j in range (2):
        print(diffs[i][j], end=' ')
    print();

count = 0
print()

# cubic spline interpolation
temp = [
        [1.0,  0.0,   0.0,   0.0],
        [3.0, 12.0,   3.0,   0.0],
        [0.0,  3.0,  10.0,   2.0],
        [0.0,  0.0,   0.0,   1.0],[0.0,  0.0,   1.0,   0.0], [0.0, -0.02702703, 0.10810811, 0.0]
    ]

for row in temp:
    print("[", end="")
    for val in row:
        print(f"{val: .0f}", end="")
        if val != row[-1]:
            print(" ", end="")
    print("]")
