import generate_json
import populate_file
import os


def collect_data():
    generate_json.serialize(generate_json.generate())  # generates "all_fields.json" file
    populate_file.populate_from_json(os.path.join("..", "Documents", "all_fields.json"),
                                     os.path.join("..", "Documents", "declarac.xlsx"))
