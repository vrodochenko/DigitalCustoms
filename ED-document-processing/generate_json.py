import json
import func

filling_functions = [elem for elem in dir(func) if elem.startswith("gr")]
print(filling_functions)


def generate():
    wonderful_declaration_dict = {}
    for function_name in filling_functions:
        method = getattr(func, function_name)
        try:
            res = method()
            if type(res) == list:
                " ".join(res)
            print("Function {} passed and returned {}".format(function_name, res))
            wonderful_declaration_dict[function_name] = res
        except:
            print("Cannot run function {}, skipping".format(function_name))
            continue
    return wonderful_declaration_dict


def serialize(declaration_dict, path="all_fields.json"):
    with open(path, "w") as json_destination:
        json.dump(declaration_dict, json_destination)


if __name__ == "__main__":
    serialize(generate())