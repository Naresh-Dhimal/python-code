import random

print("The random number between 1 To 10")


list1 = []
# for i in range(0,11):
#     number = random.randrange(1 , 10)
#     if number not in list1:
#         list1.append(number)
condition = True
while condition:
    number = random.randrange(1,11)
    if number not in list1: 
        list1.append(number)
    elif len(list1) == 10:
        condition = False
    else:
        continue
print(list1)

class Person:
    def printname(self):
        print(self.name, self.age)

person = Person()
person.name = "Naresh"
person.age =  24
person.printname()
