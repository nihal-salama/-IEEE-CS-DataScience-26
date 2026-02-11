num = input("Enter a positive integer: ")
power = len(num)
sum = 0
for i in range(power):
    sum += pow(int(num[i]),power) 
if sum == int(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")