number = int(input('Input a number: '))

# for i in range(1, number + 1):
#        if (number % i == 0):
#               print(i);

count = 0
for i in range(1, number + 1):
       if (number % i == 0):
              count = count + 1

if (count == 2):
       print(number, 'is a prime number.')
else:
       print(number, 'is a composite number.')

# print(count, 'factors')
