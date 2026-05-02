# fibonacci sequence program w/o user input

term = 10   # number of terms
first = 0   # first number
second = 1  # second number

for i in range(term):
    print(first)

    next = first + second
    first = second
    second = next