import json

class configuration:
    def __init__(self, token = '', prefix = '.', personal_vc_id = '', personal_vc_category = '', description = '', name = ''):
        self.token = token
        self.prefix = prefix
        self.personal_vc_category = personal_vc_category
        self.personal_vc_id = personal_vc_id
        self.description = description
        self.name = name

def load_config(filename):
    with open(filename) as cfgFile:
        jsonfile = json.loads(cfgFile.read())
    
    args = (
        jsonfile['token'],
        jsonfile['prefix'],
        jsonfile['personal_vc_id'],
        jsonfile['personal_vc_category'],
        jsonfile['description'],
        jsonfile['name']
    )
    conf = configuration(*args)
    return conf