# program to find an armstrong number

num = int(input('enter a number: '))
# storing original number
orig = num
# counting digits
digits = len(str(num))
# init sum
result = 0

# main logic
while num > 0:
    digit = num % 10 # gets the last digit
    result += digit ** digits
    num = num // 10 # removes the last digit

if result == orig:
    print('this is an armstrong number...')
else:
    print('this is not an armstrong number...')