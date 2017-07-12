import yaml

customer = [
	{"name": "jon", "age": "2", "gender": "man"},
	{"name": "fuck", "age": "12", "gender": "woman"},
	{"name": "head", "age": "11", "gender": "man"},
	{"name": "pussy", "age": "15", "gender": "man"}
]

yaml_str = yaml.dump(customer)
print(yaml_str)
print("--- --- ---")

data = yaml.load(yaml_str)
for p in data:
	print(p["name"])