# Write a program which displays all numbers which are divisible by 7
# but not a multiple of 5 between 1000 and 2000.

for i in range(1000, 2001):
    if i%7==0 and i%5!=0:
        print(i)
