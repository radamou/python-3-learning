#Anonymous function
def makeDecrementor(n):
    return lambda x : x-1

increment = makeDecrementor(45)
print(increment(45))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pair : pair[1]) #sort by second tuple value => 'one', 'two', etc
pairs.sort(key = lambda pair : pair[0]) #sort by first tuple value => (1, 2, 3, 4)
print(pairs)

