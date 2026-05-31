# lambda function
# higher order function
# list comprehension
import expression

from function import multiply


def sum(a):
    return a+a

lambda parameters : expression

sum_func = lambda num : num + num
print(sum_func(5))

multiply_func = lambda x , y : x * y
print(multiply_func(5, 2))

# high order function
def function_builder (x):
    return lambda y : x + y

add_test1 = function_builder(5)
print(add_test1(10))
print(add_test1(20))

# sort
scores =[4,1,5,2,7,3]
scores.sort()
print(scores)

classScore = [("mina" , 4) ,
              ("Abbas" , 8) ,
              ("Babas" , 2) ,
              ("Nikoo" , 18)]
classScore.sort()
classScore.sort(key = lambda x: x[1])
print(classScore)

# map
result = map(lambda x: x[0], classScore)
print(list(result))

result = map(lambda x: (x[0], x[1] >5), classScore)
print(list(result))

# filter
result = filter(lambda x: x[1] > 5, classScore)
print(list(result))

# list comprehension
# [expression for item in list]
# convert map to list comprehension
result = map(lambda x: x[0], classScore)

list_comprehension =  [x[1] for x in classScore]
print(list_comprehension)

# convert filter to list comprehension
result = [item for item in classScore if item[1] > 5]
print(result)
