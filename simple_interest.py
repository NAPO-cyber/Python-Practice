# program to calculate simple interest

p = int(input('enter principal amount: '))
r = int(input('enter rate of interest: '))
t = int(input('enter time period (in yeaars): '))

# SI = P*R*T / 100

si = p*r*t / 100
print(f'SI of each year on your given amount is: {si}')
print(f'you earn {si/t} each year')
