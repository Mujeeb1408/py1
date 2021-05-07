# calculating average of best of 2 out of 3
print('Enter the test marks1')
a = float(input())
print('Enter the test marks2')
b = float(input())
print('Enter the test marks3')
c = float(input())
if a > b > c or b > a > c:
    m1 = a
    m2 = b
    print(m1)
    print(m2)
elif  b > c > a or c > b > a:
    m1 = b
    m2 = c
    print(m1)
    print(m2)
elif a > c > b or c > a > b:
    m1 = a
    m2 = c
    print(m1)
    print(m2)
avg = (m1 + m2) / 2
print('Average best of 2 out of 3 is :' + str(avg))
