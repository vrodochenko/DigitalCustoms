import json


def decode_json(input_json):
    out_json = {}
    for elem in input_json:
        out_json[elem]=json.loads(input_json[elem])
    return out_json


if __name__ == "__main__":
    a = {"gr11_1": "\"SW\"", "gr11_2": "\"\\u0428\\u0412\\u0415\\u0419\\u0426\\u0410\\u0420\\u0418\\u042f\"",
         "gr12": "\"900015.2000000001\"", "gr14_1": "\"3664069397/366401001\""}
    c = decode_json(a)
    print(c)