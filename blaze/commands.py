import subprocess
from pathlib import Path 

from touchdown import Markdown, Html
from settings import read_settings, validate_settings, set_default_settings
from lib import (
    fill_dir, 
    batch_download,
    find_project_root, 
)


def init(folder=Path('./'), type='static'):
    if not folder.exists():
        folder.mkdir()

    if type == 'static':
        # create folder structure
        print('Initializing project structure')
        fill_dir(folder, ['blaze.json', 'index.html', 'entries/', 'static/'])
        fill_dir(folder / Path('static'), ['js/', 'css/', 'views/', 'images/'])
        fill_dir(folder / Path('entries'), ['index.mdx'])

        # write defaults into config files and markdown templates
        folder / Path('entries') / Path('index.mdx').write_text('Ignite the web 🔥')
        blaze_json = folder / Path('blaze.json')
        blaze_json.write_text(set_default_settings(type))
    else: 
        # create folder structure
        print('Initializing project structure')
        fill_dir(folder, ['blaze.json', '_redirects', 'webpack.config.js', 'package.json', 'entries/', 'src/'])
        fill_dir(folder / Path('src/'), ['routes.js', 'index.js', 'index.html', 'views/', 'styles/', 'components/'])
        fill_dir(folder / Path('entries/'), ['index.mdx'])

        # download template config files
        print('Downloading config files')
        LIT_TEMPLATE = 'https://raw.githubusercontent.com/11/lit-boilerplate/master'
        filenames = ['_redirects', 'package.json', 'webpack.config.js', 'src/routes.js', 'src/index.js', 'src/index.html']
        template_files = batch_download([f'{LIT_TEMPLATE}/{file}' for file in filenames])

        # write defaults into config files and markdown templates
        for idx, file in enumerate(filenames):
            fd = folder / Path(file)
            text = template_files[idx].text
            fd.write_text(text)

        index_mdx = folder / Path('entries/index.mdx')
        index_mdx.write_text('Ignite the web 🔥')

        blaze_json = folder / Path('blaze.json')
        blaze_json.write_text(set_default_settings(type))

        # run install commands
        print('Installing JavaScript libraries')
        subprocess.run(['npm', 'install', '--prefix', str(folder)])

    print('Done 🔥')


def build():
    # validate settings
    settings = read_settings()
    validate_settings(settings)

    # iterate over markdown files 
    project_dir = find_project_dir() 
    for fd in entries.iterdir():
        if fd.is_file() and (fd.suffix == 'md' or fd.suffix == 'mdx'):
            # TODO parse markdown 
            pass


def serve(settings={}):
    settings = read_settings()
    PORT = settings.get('port', 3000)
    # TODO