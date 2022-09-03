from pathlib import Path 

from lib import read_settings, find_project_root, fill_dir, batch_download


def init(folder=Path('./'), type='static'):
    if not folder.exists():
        folder.mkdir()

    if type == 'static':
        # create folder structure
        fill_dir(folder, ['blaze.json', 'index.html', 'entries/', 'static/'])
        fill_dir(folder / Path('static'), ['js/', 'css/', 'views/', 'images/'])
        fill_dir(folder / Path('entries'), ['index.mdx'])

        # write defaults into config files and markdown templates
        folder / Path('entries') / Path('index.mdx').write_text('Ignite the world 🔥')
    else: 
        # create folder structure
        fill_dir(folder, ['blaze.json', '_redirects', 'webpack.config.js', 'package.json', 'entries/', 'src/'])
        fill_dir(folder / Path('src/'), ['routes.js', 'index.js', 'index.html', 'views/', 'styles/', 'components/'])
        fill_dir(folder / Path('entries/'), ['index.mdx'])

        # write defaults into config files and markdown templates
        index_mdx = folder / Path('entries/index.mdx')
        index_mdx.write_text('Ignite the world 🔥')

        LIT_TEMPLATE = 'https://raw.githubusercontent.com/11/lit-boilerplate/master'
        filenames = ['_redirects', 'package.json', 'webpack.config.js', 'src/routes.js', 'src/index.js', 'src/index.html']
        template_files = batch_download([f'{LIT_TEMPLATE}/{file}' for file in filenames])
        for idx, file in enumerate(filenames):
            fd = folder / Path(file)
            text = template_files[idx].text
            fd.write_text(text)


def build(settings={}):
    settings = read_settings()
    project_dir = find_project_dir() 
    # TODO


def serve(settings={}):
    settings = read_settings()
    PORT = settings.get('port', 3000)
    # TODO