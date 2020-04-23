import json

class configuration:
	def __init__(self, token = '', prefix = '', description = '', name = '', referral_levels = []):
		self.token = token
		self.prefix = prefix
		self.description = description
		self.name = name
		self.referral_levels = referral_levels

def load_config(filename):
	with open(filename) as cfgFile:
		jsonfile = json.loads(cfgFile.read())
	
	args = (
		jsonfile['token'],
		jsonfile['prefix'],
		jsonfile['description'],
		jsonfile['name'],
		jsonfile['referral_levels']
	)
	conf = configuration(*args)
	return conf
