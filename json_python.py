import  json

data = {
    "name": "Владимир",
    "age": 17,
    "is_student": True,
    "courses": ["Python", "QA Automation", "API Testing"],
    "address": {
        "city": "Москва",
        "zip": "101000"
    }
}

json_data = json.dumps(data, indent=2, ensure_ascii=False)
print(json_data)

json_string = '{"name": "Константин", "age": 38, "is_student": true}'
json_dict = json.loads(json_string)
print(json_dict)

with open('json_example.json', 'r', encoding='utf-8') as file:
    data_json = json.load(file)
    print(data_json)


with open('json_user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
