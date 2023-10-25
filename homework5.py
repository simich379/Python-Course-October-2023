# ##################################################
# Problem 1 : Create a list with the numbers from 1 to 10 and print it

generate_list1 = []

for i in range(1, 11):
    generate_list1.append(i)

print("The generated list in range 1- 100 is : ", generate_list1)

# ##################################################
#
# 1.1. Create a list with the numbers from 1 to 1000 and print it

generate_list2 = []
for i in range(1, 1001):
    generate_list2.append(i)
print("The generated list in range 1- 1000 is : ", generate_list2)
# ##################################################

# ##################################################
#
# 2. Reverse the order of the elements in the list from problem 1 and print the result.
generate_list1.reverse()
print("List 1 - reversed :", generate_list1)
generate_list2.reverse()
print("List 2 - reversed :", generate_list2)

# ##################################################
# 3. Given a list of words, create a new list containing the lengths of each word.

n = int(input("Input a size for the list "))
input_list = []
for _ in range(1, n + 1):
    input_list.append(input('Enter a word: '))

print(input_list)

new_list = []
for item in input_list:
    new_list.append(len(item))

print(new_list)


# # #################################################
# 3.1. Given a list of words, create a new dictionary mapping every word to it's length.

# size_n = int(input("Input a size for the list "))
# ls = []
# for _ in range(1, size_n + 1):
#     ls.append(input('Enter a word: '))
#
# print(ls)
#
# n_list = []
# for item in ls:
#     n_list.append(len(item))
#
# print(new_list)
#
# new_dic = dict(zip(ls, n_list))
#
# for (key, value) in new_dic.items():
#     new_dic[key] = value
#
# print("The mapped dict:", new_dic)
#

# ##################################################
# 4. Write a function that takes a list and returns the sum of all even numbers in the list.
# ##################################################
def even_num_in_list(list=None):
    if list is None:
        list = []
    sum = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            sum += list[i]
    return sum


a = [1, 22, 3, 4, 5, 8, 9]
print("The sum of all even numbers in the list is : ", even_num_in_list(a))
# ##################################################
# Given a tuple of integers, find the maximum and minimum values without using built-in
# functions.


t = (4, 87, 99, 23, 65)


def minmax(_tuple):
    _min = _tuple[0]
    _max = _tuple[0]
    for i in range(len(_tuple)):
        if _min > _tuple[i]:
            _min = _tuple[i]
        if _max < _tuple[i]:
            _max = _tuple[i]
    return _min, _max


print("The min and max value of tuple is ", minmax(t))

# ##################################################
# Implement a basic queue structure ( as a global var ) by defining two functions `enqueue` and `dequeue.
# ##################################################

q_l = []

print("Enter the number of elements ")
maxsize = int(input())
i = 0
q = 0

front = -1
rear = -1

for q in range(0, maxsize):  # for creating an array with user input number of 0s
    q_l.append(0)


def isFull():
    if rear == maxsize:
        return 1
    else:
        return 0


def isEmpty():
    if front == -1 and rear == -1:
        return 1
    elif front == rear:
        return 1
    else:
        return 0


def enqueue(elem):
    global front
    global rear

    if isEmpty() == 1:
        front = 0
        rear = 0
        q_l[rear] = elem
        rear = rear + 1
    else:
        q_l[rear] = elem
        rear = rear + 1


def dequeue():
    global front
    global rear

    if isEmpty() == 1:
        return 1
    else:
        front = front + 1


q_size = int(input("Input a size for a queue! "))
i = 0
while i <= q_size:

    print("Add an element ?(0) \nDelete an element?(1) \nDisplay the elements?(2)\n")
    a = int(input("Choose a command! "))
    if a == 0:
        if isFull() == 1:
            print("Queue is full")
            break
        else:
            b = int(input())
            enqueue(b)
    if a == 1:
        dequeue()
    if a == 2:
        for c in range(front, rear):
            print(q_l[c])
    i = i + 1


# ##################################################
# 7. Create a dictionary that maps students to their bank account number. Some students may
# have multiple bank accounts


def add_values_in_dict(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


stud_accounts = {'Simona': ['BGDFGHJ456FGH', 'BGDFGHJ5789kGH'],
                 'Metodi': ['BGDFGHJ4567YU'],
                 'Neli': ['BGDFGHJ45690', 'BGDERT657UI'],
                 'Sasho': ['BGDFGHJ456FGH']
                 }

students_accounts = add_values_in_dict(stud_accounts, 'Sasho', ['BG2345WERFVYT'])
print('Contents of the dictionary: ')
print(students_accounts)


# ##################################################
# 8. Think of a function that can hash lists. Implement it and test it
def simple_hash(s=[]):
    hash_code = 0
    for char in range(0, len(s)):
        hash_code += ord(char)
    # ord() returns the ASCII value of a character
    return hash_code
# ##################################################
