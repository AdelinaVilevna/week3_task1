# Qustion 1
# list_ = [1, 2, 3, 4, 5, 6]
# list2 = [number for number in list_ if number % 2 == 0]
# print(list2)

# 2 way

# list_ = range(2,100)
# list2 = [number for number in list_ if number % 2 == 0]
# print(list2)


# Question 2
# list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# list2 = [y**2 for x in list1 for y in x]
# print(list2)


# Question 3
# list_ = ["12", "15", "16", "17"]
# list2 = [int(number) for number in list_]
# print(list_)

# Question 4

dict1= {'a': 5, 'b': 3, 'c': 8, 'd': 14}
dict_new = {key : 'Foo' if val % 3 else 'bar' for key, val in dict1.items() if val % 3 == 0 or val % 5 == 0 }
print(dict_new)