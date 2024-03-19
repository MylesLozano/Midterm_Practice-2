#Sum of multiples code
def sum_multiple(x,y,limit):
    sum = 0
    for i in range(limit):
        if i % x == 0 or i % y == 0:
            sum += i
    return sum 

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
limit = int(input("Enter the limit: "))

print(f"The sum of multiples of {x} or {y} up to {limit} is {sum_multiple(x,y,limit)}")