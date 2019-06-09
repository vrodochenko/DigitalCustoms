import json
import os


def populate_from_json(source_json_file, target_file):
    with open(source_json_file) as src:
        declaration_dict = json.load(src)
    if os.path.exists(target_file):
        result_file = target_file.split(".")[0] + "_result" + target_file.split(".")[-1]
        f = open(result_file, "w")
        try:
            with open(target_file) as tf:
                for line in tf.readlines():
                    res_line = line
                    for key in declaration_dict.keys():
                        res_line = res_line.replace(key, declaration_dict[key])
                    f.write(res_line)
        finally:
            f.close()


if __name__ == "__main__":
    populate_from_json("all_fields.json", "test.json")
