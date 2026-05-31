students = ["sarvin" , "mina" , "ali" , "Abbas"]
newList = []
new_list1 = ["Abbas", 3.12 , 4, True]
new_list2 = list(("abbas" , "ali" , 'hoda'))
print(type(new_list1))
print(students)
print(new_list1)

# zero_list = [0] * 20
# print(zero_list)
#
# numbers = list(range(10))
# numbers[0] = 4
# print (numbers)
# print(len(students))
print(students)
print(students[len(students) - 1] )
print(students[-1])

print(students[0:2])
print(students[:2])
print(students[2:])
print(students[::2])
#from last item to first item
print(students[::-1])

students[0] = "Nikoo"
print(students)

# packing & unpacking
nums = [1,2,3,4,5]
first = nums[0]
second = nums[1]
third = nums[2]
#unpacking
#first , second , third = nums
print(nums)
print(first , second , third)
first, second, *others = nums
print(first, second, others)

first, *others, last = nums
print(first, last, others)

students.append("Zahra")
students.append("Hamed")
print(students)

students += ["user1" , "user2" , "user3"]
students = students + new_list1
print(students)

students.extend('hoda')
students.extend(['hoda'])
print(students)

students.insert(2, 'masoud')
print(students)

students[2:3] = ["add1", "add2"]
print(students)

# students[2:3] = ["add3", "add4"]
# print(students)


