# to find the largest of 3 numbers

print('Enter the 3 numbers')
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print('The largest number among 3 numbers is')
    print(a)
elif b > c:
    print('The largest number among 3 numbers is')
    print(b)
else:
    print('The largest number among 3 numbers is')
    print(c)