# Exception - Error Handling
Courses = ["html", "css"]
try:
    your_age = int(input("Enter your age: "))
    x = 2 / your_age
    print(Courses[2])
except IndexError:
    print("this is an index error")
except (ValueError, ZeroDivisionError):
    print("this is an error value")

Courses = ["html", "css"]
try:
    file = open("file.txt")
    your_age = int(input("Enter your age: "))
    x = 2 / your_age
    # print(Courses[2])
except Exception as error:
    print("an error occured")
    # print(error)
    # print(type(error))
else :
    print("you entered valid number")
finally:
    file.close()



