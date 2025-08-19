def NULL_not_found(object: any) -> int:
    try:
        obj_type = type(object)
        output = ""

        if (obj_type is type(None)):
            output = 'Nothing: '
        elif (obj_type is float and object != object):
            output = 'Cheese: '
        elif (obj_type is int and object == 0):
            output = 'Zero: '
        elif (obj_type is str and not object):
            output = 'Empty: '
        elif (obj_type is bool and not object):
            output = 'Fake: '
        else:
            print('Type not Found')
            return 1
        output += f"{object} {obj_type}"
        print(output)
        return 0
    except Exception as e:
        print(f"Error: {e}")
