def all_thing_is_obj(object: any) -> int:
    string_type = ""
    object_type = type(object)
    if object_type == list:
        string_type = "List"
    elif object_type == tuple:
        string_type = "Tuple"
    elif object_type == set:
        string_type = "Set"
    elif object_type == dict:
        string_type = "Dict"
    elif object_type == str:
        string_type = f"{object} is in the kitchen"
    else:
        print("Type not found")
        return 42

    print(f"{string_type} : {object_type}")
    return 42
