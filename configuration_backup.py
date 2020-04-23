import json

class configuration:
	def __init__(self, token = '', prefix = '', description = '', name = ''):
		self.token = token
		self.prefix = prefix
		self.description = description
		self.name = name

def load_config(filename):
	with open(filename) as cfgFile:
		jsonfile = json.loads(cfgFile.read())
	
	args = (
		jsonfile['token'],
		jsonfile['prefix'],
		jsonfile['description'],
		jsonfile['name']
	)
	conf = configuration(*args)
	return conf