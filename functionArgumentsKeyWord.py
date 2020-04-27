def functionWithDictionaryArgument(kind, *arguments, **dictionary):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for key in dictionary:
        print(key, ":", dictionary[key])

functionWithDictionaryArgument("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def standardArgument(argument):
    print(argument)
# / for positional only, * keywordOnly
#def positionalOlyParam(posOnly, /):
#    print('positional only parameter', argument)
#def keyOnlyParamter(*, argument): 
#    print(argument)
#def combinedExample(posOnly, /, standard, *, kwdOnly):
#    print(posOnly, keyOnlyParamter, standardArgument)
