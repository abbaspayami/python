num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [1, 3, 5, 7, 9]
list_expreh = [item for item in num if item % 2 != 0]
print(list_expreh)

# [1, 4, 9, 16, 25]
list_exprehex = [ item ** 2 for item in num if item < 6]
print(list_exprehex)

# [1, 4, 3, 16, 5, 36, 7, 64, 9]
result = [ item ** 2 if item % 2 == 0 else item for item in num ]
print(result)

classScore = [{"name" : "sarvin" , "score" : 4} ,
              {"name" : "Abbas" , "score" : 6} ,
              {"name" : "Nikoo" , "score" : 12} ,
              {"name" : "Arman" , "score" : 16}]

# shows only score greeter than 10
result = [ item for item in classScore if item["score"] > 10]
print(result)

# shows only score greeter than 10
result = [ item for item in classScore if item["score"] > 10]
print(result)

result = [{"name" : item["name"] , "passed" : item["score"] >= 10} for item in classScore]
print(result)