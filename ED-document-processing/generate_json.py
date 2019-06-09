import json
import func
import os
from decode_jsons_cyr import decode_json
filling_functions = [elem for elem in dir(func) if elem.startswith("gr")]
print(filling_functions)


def generate():
    wonderful_declaration_dict = {}
    for function_name in filling_functions:
        method = getattr(func, function_name)
        try:
            res = method()
            if type(res) == list:
                res = " ".join(res)
            print("Function {} passed and returned {}".format(function_name, res))
            wonderful_declaration_dict[function_name] = res
        except:
            print("Cannot run function {}, skipping".format(function_name))
            continue
    wonderful_declaration_dict = decode_json(wonderful_declaration_dict)
    return wonderful_declaration_dict


def serialize(declaration_dict, path=os.path.join("..", "Documents", "all_fields.json")):
    with open(path, "w") as json_destination:
        json.dump(declaration_dict, json_destination)


if __name__ == "__main__":
    print(serialize(generate()))
