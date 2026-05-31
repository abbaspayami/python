def greeting(name , count): # parameter
    print("*" * count)
    print("hello " + name)
    print("*" * count)

greeting("Abbas" , 50) #argument
greeting("Nikoo" , 20) #argument

def get_greeting(name):
    return "hello " + name

result =  get_greeting("Zahra")
print(result)

def sum(a,b = 0):
    return a+b

result = sum(2,3)
# print(result)

# xarg
def multiply(*numbers):
    # print(type(numbers))
    # print(numbers)
    result = 1
    for n in numbers:
        result = result * n
    return result

print(multiply(2,3,5,7))

# xxarg
def multiply_xx(**data):
    print(data)
    print(type(data))
    print(data["name"])
    for key in data.items():
        print(key)

multiply_xx(name = "Zahra", age = 20, score = 100)

# recursion
def add_on(num):
    if (num >= 10):
        return num
    sum =  num + 1
    print(sum)
    return add_on(sum)

add_on(0)

# scope

# global
name = "Nikoo_global"
def greeting():
    global name
    name = "Ali"
    print("hello " + name)

def function():
    print("hello " + name)
function()
greeting()

# nonlocal
def function1():
    name = "john"
    def function2():
        nonlocal name
        name = "ali"
    function2()
    return name

result = function1()
# print(result)

# closure
def parent_func (player):
    coins = 3
    def play_game():
        nonlocal coins
        coins -= 1
        print(f"{player} has {coins} left.")

    return play_game
user1 = parent_func("John")

user1()
user1()

