import os
import json
def fetchFiles():
    # Determine the home directory
    home_directory = os.path.expanduser('~')

    with open('options.json') as json_options:
        options = json.load(json_options)
        scripts_directory = os.path.join(home_directory, options['ScriptDirectory'])

        # List all files in the 'scripts' directory
        files = os.listdir(scripts_directory)

        print("Files in the 'scripts' directory:")
        for file in files:
            print(file)
        return files
