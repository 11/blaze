import sys
import json
from pathlib import Path


def read_settings():
    for folder in Path.cwd().parents:
        settings_file = folder / Path('blaze.json')
        if settings_file.exists() and settings_file.is_file():
            try:
                settings = json.loads(settings_file).decode('utf-8')
                return settings
            except json.JSONDecodeError:
                sys.exit('Error while decoding `blaze.json`')

    sys.exit('Could not find blaze.json file. Try running `blaze init`')
