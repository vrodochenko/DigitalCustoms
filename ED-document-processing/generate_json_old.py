import os

filenames_of_documents = ["Agreement",
                          "CMR",
                          "Contract",
                          "Invoice"]

procedures_in_directory = os.listdir()
procedures_in_directory = [elem[:-3] for elem in procedures_in_directory if elem.endswith(".py")]
procedures_in_directory.remove("generate_json")

json_generating_procedures = [fname for fname in procedures_in_directory if
                              fname.split(".")[0] not in filenames_of_documents]

for json_generating_procedure in json_generating_procedures:
    __import__(json_generating_procedure)

