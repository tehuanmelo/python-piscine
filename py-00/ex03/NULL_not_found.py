def NULL_not_found(object: any) -> int:
    # your code here
    import math as math

    string_type = ""
    object_type = type(object)

    if object_type == type(None):
        string_type = f"Nothing: None {object_type}"
    elif object_type == float and math.isnan(object):
        string_type = f"Cheese: nan {object_type}"
    elif object_type == int and object == 0:
        string_type = f"Zero: 0 {object_type}"
    elif object_type == str and object == "":
        string_type = f"Empty: {object_type}"
    elif object_type == bool and object is False:
        string_type = f"Fake: False {object_type}"
    else:
        print("Type not found")
        return 1

    print(string_type)
    return 0
