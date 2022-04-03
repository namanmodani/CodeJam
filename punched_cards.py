# Google Code Jam 2022
# Punched Cards
# Naman Modani

t = int(input())
for i in range(t):
    print('Case #' + str(i + 1) + ':')
    x, y = map(int, input().split(' '))

    for j in range(2 * x + 1):
        s = ''
        if j == 0:
            s = '..'
            for k in range(y - 1):
                s += '+-'
            s += '+'
            print(s)
        elif j == 1:
            s = '..'
            for k in range(y - 1):
                s += '|.'
            s += '|'
            print(s)
        elif j % 2 == 0:
            for k in range(y):
                s += '+-'
            s += '+'
            print(s)
        else:
            for k in range(y):
                s += '|.'
            s += '|'
            print(s)
