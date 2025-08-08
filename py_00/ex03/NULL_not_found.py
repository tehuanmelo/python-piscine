from math import isnan


def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if (obj_type is type(None)):
        print(f'None : {obj_type}')
    elif (obj_type is float and isnan(object)):
        print(f'Cheese: nan {obj_type}')
    elif (obj_type is int and object == 0):
        print(f'Zero: 0 {obj_type}')
    elif (obj_type is str and not object):
        print(f'Empty: {obj_type}')
    elif (obj_type is bool and not object):
        print(f'Fake: False {obj_type}')
    else:
        print('Type not Found')
        return 1
    return 0
