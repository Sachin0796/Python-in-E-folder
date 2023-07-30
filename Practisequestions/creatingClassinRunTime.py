def test():
    return 1

base_class = type("BaseClass",(function,),test())
C1 = type("C1",(base_class,),{'val3':5,'val2':15})
C2 = type("C2",(base_class,),{'val4':10})

def classCreator(bool):
    if bool:
        return C1()
    else:
        return C2()
    
print(classCreator(True))
print(classCreator(False).val)