import os
import json
invalid_json_files = []
read_json_files = []
d=[]
def parse():
    for files in os.listdir(os.getcwd()):
      if files.endswith('.json'):
        with open(files) as json_file:
            try:
                 
                d.append(json.load(json_file))
                read_json_files.append(files)
            except ValueError, e:
                print ("JSON object issue: %s") % e
                invalid_json_files.append(files)
    print invalid_json_files, len(read_json_files)
    print d
parse()
