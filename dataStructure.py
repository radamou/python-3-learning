from collections import deque

def data_structure_function():
    list = [123, 131, 456, 25]
    #append or list[len(a=list):] = [800]
    list.append(800)
    print(list, sep=';')
    #extend or list[len(list):] = [200, 300].
    list.extend([200, 300])
    #insert
    print(list)
    list.insert(len(list), 152)
    print(list)
    #remove
    list.remove(152)
    print(list)
    #pop
    poped = list.pop(2)
    print(poped)
    #clear or del list[:]
    list2 = [2, 3, 4, 5]
    list.clear()
    del list2[:]
    print(list2)
    list3 = [8, 9, 10, 11]
    index = list3.index(10, 0, 3)
    print(index)
    #count number of time value appear in the list
    list4 = ['machine', 'machine', 'iterable', 'iterable']
    print(list4.count('machine'))
    #sort
    print(list4.sort())
    print(list4.reverse())

#-------------------------------------------------------

#List as stack (added elements in the first one, removing the last element => last-in first-out)
stack = [1, 20]
stack.append(10)
stack.append(23)
stack.pop()
print(stack)

#list as queue (fist-in first-out)
queue = deque([23, 70])
queue.append(15)
queue.popleft()
print(queue)

#-----------------------------------------------------------
#List comprehensions => concise way to create a list
squares = []
for x in range(0, 11):
    squares.append(x**2)
print(squares)

#comprehensions list
squares_list = list(map(lambda x : x**2, range(11)))
print(squares_list)

squares_list_shirt_code = [x**2 for x in range(0, 11)]
print(squares_list_shirt_code)

#combine list with shirt code
another_shirt_code_list = [(x,y) for x in [12, 15, 12, 23] for y in [15, 18, 36] if x != y]
print(another_shirt_code_list)

#flaten a vector [num for elem in vec for num in elem]
vec = [
    [
        [13, 15], 
        [21, 23], 
        [7, 9]
    ],
    [10, 5, 7], 
    [14, 8, 15]
]
flatten_vec = [x for item in vec for x in item]
print(flatten_vec)

#test => find how to flatten alls arrays in vec

#------------------------------------------------------
#tuple and sequence
#tuple = values separate by comma
tuple_one = "rama", 'pyton is weired'
print(tuple_one)
tuple_two = "rama", 1
print(tuple_two)
tuple_tree = ((1, 2, 3), (4, 5, 6))
print(tuple_tree)

#tuples are immutable 
#tuple_one[0] = 123 will display error 

#empty tuple
empty_tuple = ()
one_data_tuple = 'one date',

print(empty_tuple)
print(one_data_tuple)

#sequence
sequence = 'very', 'weired', 'langage'
var1, var2, var = sequence
print(var1)
print(var2)
print(var)