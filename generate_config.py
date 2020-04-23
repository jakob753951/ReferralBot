import json
with open('fields.json') as cfgFile:
	fields = json.loads(cfgFile.read())

with open('configuration.py', 'w') as out_file:
	out_file.write(f"""\
import json

class configuration:
\tdef __init__(self, {', '.join([f"{field} = ''" for field in fields])}):
""")


	for field in fields:
		out_file.write(f'\t\tself.{field} = {field}\n')
	
	sep = ',\n\t\t'
	out_file.write(f"""
def load_config(filename):
	with open(filename) as cfgFile:
		jsonfile = json.loads(cfgFile.read())
	
	args = (
		{sep.join([f"jsonfile['{field}']" for field in fields])}
	)
	conf = configuration(*args)
	return conf
""")
	
