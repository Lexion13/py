import yaml

yaml_str = """
PriceList:
	-
		item_id: 1000
		name: Banana
		color: yellow
		price: 800
		
	-
		item_id: 1001
		name: orange
		color: orange
		price: 1400
		
	-
		item_id: fuck
		name: fuck
		color: fuck
		price: fuck
		
"""

data = yaml.load(yaml_str)

for item in data['PriceList']:
	print(item["name"], item["price"])