'''
""" work with JASON file"""
import json
with open('data\\sw_templates.json') as fu:
	templates = json.load(fu)

#print(templates)

for section, commands in templates.items():
	print(section)
	print('\n'.join(commands))
#	print('\n', commands)
'''

""" work with CSV files"""
import csv
with open('data\\sw_data.csv') as fuu:
	'''
	my_reader = csv.reader(fuu)
	for row in my_reader:
		print(row)
	'''
	'''
	my_reader = csv.reader(fuu)
	my_headers = next(my_reader)
	print('Headers: ', my_headers)
	for row in my_reader:
		print(row)
	'''


	my_reader = csv.reader(fuu)
	my_reader2 = csv.DictReader(fuu)
	print(my_reader)
	print(my_reader2)
	'''
	for two in my_reader:
		print(two)
	'''
	for row in my_reader2:
		print(row)
#		print(row['hostname'], row['model'])

	print('Hi there!')

	for one in my_reader2:
		print(one)
