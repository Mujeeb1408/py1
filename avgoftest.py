#to find the average of 2 test marks out of 3 test marks
print('Enter the test marks')
a = float(input())
b = float(input())
c = float(input())
avg = (a+b+c)/3
print('Average of the test is')
print(avg)
#calculating the best of 2 average
if a < b and a < c:
    avg = (b+c)/2
    print('Best of 2 average is' + str(avg))
elif b < c:
    avg = (a+c) / 2
    print('Best of 2 average is' + str(avg))
else:
    avg = (a+b) / 2
    print('Best of 2 average is' + str(avg))
