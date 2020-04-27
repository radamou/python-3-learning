def documentationString():
    """Do no thing, but document it

    Oh, realy, this function doen't do anything
    """
    pass

print(documentationString.__doc__)


#Function annotation (are completly optional)
def  AnnotatedTypeFunction(ham: str, eggs: str = 'eggs') -> str:
    print("Annotatetions list", AnnotatedTypeFunction.__annotations__)
    print("Arguments", ham, eggs)
    return ham + 'and' + eggs

AnnotatedTypeFunction('spam')