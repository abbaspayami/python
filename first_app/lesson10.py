# Class - Object oriented programing
# class - object

name = "Abbas"
print(type(name))
print(name.upper())

class Person:
    def __init__(self, name = 'unknown', score = 0):
        self.name = name
        self.score = score
    def eat(self):
        print(f"{self.name} is eating")

    # in order to check 2 objects are same
    def __eq__(self, other):
        return self.name == other.name and self.score == other.score
#
# first_person = Person("Abbas", 50)
# first_person.eye_color = "blue"
# first_person.score = 100
# print(first_person.eye_color)
# first_person.eat()
#
# second_person = Person("Nikoo", 300)
# print(second_person.name)
# second_person.eat()

# first_person = Person("Abbas", 50)
# second_person = Person("Abbas", 50)
# print(first_person == second_person)

# Inheritance
class Animal:
    def __init__(self, name , age):
        self.name = 'Animal'
        self.age = age
    def eat(self):
        print("eating")

class Mammal(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
    def walk(self):
        print("walking")

class fish(Animal):
    def swim(self):
        print("swimming")

cat = Mammal("cat", 4, "4kg")

print(cat.name)
print(cat.age)
print(cat.weight)

cat.walk()

# Multiple Inheritance
class Parent1:
    def common(self):
        print("common parent1")
    def feature1(self):
        print("parent1")

class Parent2:
    def common(self):
        print("common parent2")
    def feature2(self):
        print("parent2")

class Child(Parent1, Parent2):
    # def common(self):
    #     print("child common")
    def feature3(self):
        print("child")

child = Child()
child.feature1()
child.common()
