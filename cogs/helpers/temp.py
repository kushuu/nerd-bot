import json

with open('US_caps.json') as json_file:
        data = json.load(json_file)
        for i in data:
            print('"' + i['abbr'].lower() + '"' + " : " + '"' + i['capital'] + '",')
            print('"' + i['name'].lower() + '"' + " : " + '"' + i['capital'] + '",')

