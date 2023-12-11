import json

input =  'data/annotations/custom_val/'
names = ['mateo','lauren']
if __name__== "__main__":
# Create a list of all the JSON files that you want to combine.
    json_files = []
    for i in names:
        json_files.append('data/annotations/custom_test/{}.json'.format(i))

    # Create an empty list to store the Python objects.
    python_objects = []

    # Load each JSON file into a Python object.
    for json_file in json_files:
        with open(json_file, "r") as f:
            python_objects.append(json.load(f))

    # Dump all the Python objects into a single JSON file.
    with open("custom_test.json", "w") as f:
        json.dump(python_objects, f, indent=4)
