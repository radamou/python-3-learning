def defaultArgumentFunction(prompt, retries = 4, reminder = 'Please retry again'):
    while True:
        retries = retries - 1
        print('prompt', retries)
        ok = input(prompt)
        if (ok in 'y', 'ye', 'yes'):
            return True
        if(ok in 'n', 'no', 'nop', 'nope'):
            return False
        if(retries < 0):
            print('raise an error')
            raise ValueError('invalid user response')
        print(reminder)

defaultArgumentFunction('t')
defaultArgumentFunction('t')
defaultArgumentFunction('nn')
defaultArgumentFunction('for')
defaultArgumentFunction('for')

#warning on mutables objects arguments
def functionWithMutableObjectAsArgument(a, mutableObject = []):
    mutableObject.append(a)
    return mutableObject

functionWithMutableObjectAsArgument(1)
functionWithMutableObjectAsArgument(2)
print(functionWithMutableObjectAsArgument(3)) #the array is not erase on each call

#safe use of mutables objects
def functionWithMutableObjectAsArgumentSafeUse(a, mutableObject = None):
    if mutableObject == None:
        mutableObject = []
        mutableObject.append(a)
    return mutableObject

functionWithMutableObjectAsArgumentSafeUse(10)
functionWithMutableObjectAsArgumentSafeUse(12)
print(functionWithMutableObjectAsArgumentSafeUse(18))

#function arguments manipulation
def weiredFunctionArgumentBehavior(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

weiredFunctionArgumentBehavior(1000)                                          # 1 positional argument
weiredFunctionArgumentBehavior(voltage=1000)                                  # 1 keyword argument
weiredFunctionArgumentBehavior(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
weiredFunctionArgumentBehavior(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
weiredFunctionArgumentBehavior('a million', 'bereft of life', 'jump')         # 3 positional arguments
weiredFunctionArgumentBehavior('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword