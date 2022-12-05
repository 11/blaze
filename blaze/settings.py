import sys 
import pdb
import json
from pathlib import Path

from .lib import find_project_root


def read_settings():
    project_dir = find_project_root()
    settings_file = project_dir / Path('blaze.json')
    if settings_file.exists():
        try:
            with open(settings_file) as blaze_json:
                settings = json.load(blaze_json)

            validate_settings(settings)
            return normalize_settings(settings)
        except json.JSONDecodeError:
            sys.exit('Error while decoding `blaze.json`')

    sys.exit('Could not find blaze.json file. Try running `blaze init`')


def set_default_settings(type='static'):
    port = 3000
    project = type
    entries = './entries'
    views = './static/views/' \
        if type == 'static' \
        else './src/views/'

    settings = {
        'project': project,
        'entries': entries,
        'views': views,
        'port': port,
    }

    return json.dumps(settings, sort_keys=True, indent=2)


def validate_settings(settings):
    project_dir = find_project_root()

    # validate views field
    views = settings.get('views', None)
    if views is None or views == '':
        sys.exit('You must set a `views` property in your `blaze.json`.\n\t The `views` directory is where blaze will save your compiled articles.')
    views = project_dir / Path(views)
    if not views.exists():
        print(f'`{str(views)}` directory not found - creating `{str(views)}` directory')
        views.mkdir()
    elif not views.is_dir():
        sys.exit(f'The `views` property in your `blaze.json` is not a valid directory.\n\t"views": "{str(views)}"')

    # validate entries field
    entries = settings.get('entries', None)
    if entries is None or entries == '':
        sys.exit('You must set an `entries` field in your `blaze.json`.\n\tThe `entries` directory is where blaze will search for your markdown files.')
    entries = project_dir / Path(entries)
    if not entries.exists():
        print(f'`{str(entries)}` directory not found - creating `{str(entries)}` directory')
        entries.mkdir()
    elif not entries.is_dir():
        sys.exit(f'The `entries` directory in your `blaze.json` is not a valid directory.\n\t"entries": "{str(entries)}"')

    # validate project type
    project = settings.get('project', None)
    if project is None or project == '':
        sys.exit('You must set a `project` field in your `blaze.json`.\n\tThe `project` field can be set to `static` or `single-page` - this determines how the build command bundles your app')
    elif project != 'static' and project != 'single-page':
        sys.exit('Invalid Project type `{project}`. The `project` field must be set to `static` or `single-page` - this determines you the build command bundles your app')

    # validate port
    port = settings.get('port', None)
    if port is None or port == '':
        sys.exit('You must set a `port` field in your `blaze.json`.\n\tThe `port` field determines which port the dev server will run on')
    elif port < 3000 or port > 9000:
        sys.exit('`port` must be a number between 3000 and 9000.')


def normalize_settings(settings):
    project_root = find_project_root()

    settings['views'] = project_root / Path(settings['views']) 
    settings['entries'] = project_root / Path(settings['entries']) 

    return settings
