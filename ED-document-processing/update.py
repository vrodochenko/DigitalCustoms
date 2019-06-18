from populate_file import *
if "all_fields.json" in os.listdir("D:\DigitalCustoms\Documents"):
    source = os.path.join("..", "Documents", "all_fields.json")
    target = os.path.join("..", "Documents", "declarac.xlsx")
    populate_from_json(source, target)