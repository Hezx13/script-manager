import os
import json
from pathlib import Path
def fetchFiles():
    # Determine the home directory
    home_directory = os.path.expanduser('~')
    options = json.loads(open("options.json").read())
    
    if 'ScriptDirectory' not in options:
        raise KeyError
    if 'BaseDirectory' not in options:
        with open('options.json', 'w') as file:
            data = options
            data['BaseDirectory']=home_directory
            json.dump(data, file, indent=4)

    options = json.loads(open("options.json").read())
    print(options)
    scripts_directory = os.path.join(options['BaseDirectory'], options['ScriptDirectory'])
    # List all files in the 'scripts' directory
    files = sorted(Path(scripts_directory).iterdir(), key=os.path.getctime)
    filenames = [file.name for file in files]
    return filenames
