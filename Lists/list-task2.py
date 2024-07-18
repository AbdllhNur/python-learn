my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
for number in my_list:
    new_list = []
    if my_list not in new_list :
        new_list.append(number)

my_list = new_list[:]
#
print("The list with unique elements only:")
print(my_list)
