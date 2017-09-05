
for x in range(1, 1000, 2):
    print x     # prints all odd numbers 1-1000

for y in range(5, 1000001, 5):
    print y     #prints all multiples 5-1,000,000

def sum(a): # sums all values in an array
    total = 0
    for i in range(len(a)):
        total += a[i]
    print total

def avg(b): # prints the average of all values in an array
    total = 0
    for j in range(len(b)):
        total += b[j]
    print total/len(b)

x = [1, 2, 5, 10,255, 3]

sum(x)
avg(x)