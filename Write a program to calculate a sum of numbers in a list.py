def sum_list(temp_list):
    sum = 0
    for item in temp_list:
        sum += item
    return sum


size = int(input("Enter List Length : "))
my_list = []
for _ in range(size):
    temp = int(input("Enter List Item : "))
    my_list.append(temp)

print("Sum of All Numbers in List is : ", sum_list(my_list))