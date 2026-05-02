# fibonacci sequence program with user input for range
n = int(input('enter the range: '))
first = 0 
second = 1

for i in range(n):
    print(first)

    next = first + second
    first = second
    second = next