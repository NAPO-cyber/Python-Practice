#  program to calculate compound interest  CI is like interest on interest, if you decide to invest $10000 on the ROI of 5% p.a., you will earn $500 in the first year making it $10500 when added to your principal amount, the next year interest will be on $10500 and not on $10000. Hence, interest on interest.

p = int(input('enter principal amount: '))
r = int(input('enter rate of interest: '))
t = int(input('enter number of yeaars: '))

# A (final amount) = p * (1 + r/100) ** t
# CI = A - p

a = p * (1 + r/100)**t
ci = a - p

print(f'overall final amount is: {a}')
print(f'CI on your money is: {ci}')