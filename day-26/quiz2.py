with open('day-26/file1.txt') as file1:
    f1_nums = file1.readlines()

with open('day-26/file2.txt') as file2:
    f2_nums = file2.readlines()


print(f1_nums)
print(f2_nums)


nums_list1 = [int(num.strip()) for num in f1_nums]
nums_list2 = [int(num.strip()) for num in f2_nums]

print(nums_list1)
print(nums_list2)

result = [num for num in nums_list1 if num in nums_list2]
print(result)

result = list(set.intersection(set(nums_list1), set(nums_list2)))
print(result)