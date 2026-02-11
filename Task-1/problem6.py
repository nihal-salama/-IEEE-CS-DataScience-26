num = int(input("Enter a +ve num: "))

for i in range(1,11):
    if i % 4 == 0:
        continue
    if i == 10:
        print(i * num)
        break
    print(i * num , end=",")