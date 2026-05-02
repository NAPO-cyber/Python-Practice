# progrram to find prime number

start = int(input('starting number: '))
end = int(input('ending number: '))

for num in range(start, end+1):
    if num > 1:  # ignore number 0 and 1.
        
        is_prime = True # consider it is prime
        
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)