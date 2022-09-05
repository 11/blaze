import subprocess
import pdb

from pathlib import Path 

from touchdown import Markdown, Html
from .settings import (
    read_settings, 
    validate_settings, 
    set_default_settings,
)
from .lib import (
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
        (folder / Path('entries') / Path('index.mdx')).write_text('Ignite the web 🔥')
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
    settings = read_settings()

    for entry in settings['entries'].iterdir():
        # only parse markdown files
        if not entry.is_file() or (entry.suffix != '.md' and entry.suffix != '.mdx'):
            continue

        # parse html
        tokenizer = Markdown(entry)
        tokens = tokenizer.tokenize()
        interpreter = Html(tokens)
        html = interpreter.interpret()

        # write HTML to correct file and folder
        if settings['project'] == 'static':
            dest = settings['views'] / Path(f'{entry.stem}.html') \
                if entry.stem != 'index' \
                else find_project_root() / Path('index.html')

            dest.touch()
            dest.write_text(html)
        else:
            # TODO: 
            pass


def serve(settings={}):
    settings = read_settings()
    PORT = settings.get('port', 3000)
    # TODO