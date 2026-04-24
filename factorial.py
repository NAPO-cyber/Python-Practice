# finding the factorial of a number

print('FACTORIAL OF AN INTEGER...')

num = int(input('enter an integer: '))

if num<0:
    print("no factorial for negative number.")
else:
    f = 1   # initializes the product
    for i in range(f, num+1):
        f *= i
    print(f)