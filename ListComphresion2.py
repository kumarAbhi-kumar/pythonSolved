#

myList = [i for i in range(1, 11)]
print(myList)

myList1 = [23, 25, 27, 29, 31]
myList2 = [23, 27, 31, 35, 39]

myList3 = [i for i in myList1 if i in myList2]
print(myList3)

toss = ["win", "loss"]
bat = ["1st", "2nd"]

result = [i for i in toss for i in bat]

matrix = [[col for col in range(1, 6)] for row in range(1, 6)]

myList4 = [i for i in myList if 1 <= i <= 6]

nameList = ["Kumar", "Krishna", "Jaan", "Khushi"]
newList = [i for i in nameList if len(i) < 6]
print(newList)

