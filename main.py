import json
import jsonschema

file = open("class.json")

schema = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'surname': {'type': 'string'},
            'sex': {'type': 'string'},
            'age': {'type': 'integer', 'minimum': 0}
        },
        'required': ['name', 'age']
    }
}
if __name__ == '__main__':

    data = json.load(file)

    num = input("Enter 1 to print out json content: "
                "\nEnter 2 to print out type in some data: "
                "\nEnter 3 to print out minors"
                "\nEnter 4 to check the validity of the file JSON")
    if num == "1":
        for i in data['students']:
            print(i)

    if num == "2":
        student = {
            "name": input("Enter student name: "),
            "surname": input("Enter student surname: "),
            "sex": input("Enter student sex: "),
            "age": input("Enter student age: "),
        }
        data['students'].append(student)
        with open("class.json", "w+") as writeIn:
            json.dump(data, writeIn)

    if num == "3":
        for i in data['students']:
            if i['age'] < "18":
                print(i)
            # print(data)

    if num == "4":
        try:
            jsonschema.validate(data['students'], schema)
            print('User is valid')
        except jsonschema.exceptions.ValidationError as e:
            print('User is invalid because: ', e.message)

    file.close()
