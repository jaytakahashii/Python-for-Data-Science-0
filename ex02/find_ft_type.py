def all_thing_is_obj(object: any) -> int:
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: f"{object} is in the kitchen",
    }

    t = type(object)

    if t in type_map:
        print(type_map[t], ":", t)
    else:
        print("Type not found")

    return 42
