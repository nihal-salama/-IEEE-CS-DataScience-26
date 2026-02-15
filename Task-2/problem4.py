num_of_stu = int(input())
stu_data_dict = {

}
for i in range(num_of_stu):
    stu_data = input().split()
    name = stu_data[0]
    grades = list(map(float,stu_data[1:]))
    stu_data_dict.update({name : grades})
    
query_name = input().capitalize()
grades = stu_data_dict[query_name]
sum = 0
for i in range(len(grades)):
    sum += grades[i]

print(f"{(sum / len(grades)):.2f}")