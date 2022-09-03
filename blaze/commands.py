from pathlib import Path 

from lib import read_settings, find_project_root


def init(folder=Path('./'), type='static'):
    if not folder.exists():
        folder.mkdir()

    folder.touch('blaze.json')

    if type == 'static':
        index = folder / Path('index.html')
        if not index.exists():
            index.touch()

        entries = folder / Path('entries/')
        if not entries.exists():
            entries.mkdir()

        hello_world = entries / Path('hello_world.mdx')
        if not hello_world.exists():
            hello_world.touch()
            hello_world.write_text('Hello world!')

        static = folder / Path('static/')
        if not static.exists():
            static.mkdir()

        js = static / Path('js')
        if not js.exists():
            js.mkdir()

        css = static / Path('css')
        if not css.exists():
            css.mkdir()

        views = static / Path('views')
        if not views.exists():
            views.mkdir()

        imgs = static / Path('imgs')
        if not imgs.exists():
            imgs.mkdir()
    else: 
        redirects = folder / Path('_redirects')
        if not redirects.exists():
            redirects.touch()
            redirects.write_text('/*    /index.html   200')

        webpack_config = folder / Path('webpack.config.js')
        if not webpack_config.exists():
            webpack_config.touch()

        package_json = folder / Path('package.json')
        if not package_json.exists():
            package_json.touch()

        entries = folder / Path('entries/')
        if not entries.exists():
            entries.mkdir()
        
        hello_world = entries / Path('hello_world.mdx')
        if not hello_world.exists():
            hello_world.touch()
            hello_world.write_text('Hello world!')

        src = folder / Path('src/')
        if not src.exists():
            src.mkdir()

        routes = src / Path('routes.js')
        if not routes.exists():
            routes.touch()

        index_js = src / Path('index.js')
        if not index_js.exists():
            index_js.touch()

        routes_html =  src / Path('index.html')
        if not routes_html.exists():
            routes_html.touch()

        views = src / Path('views')
        if not views.exists():
            views.mkdir()

        styles = src / Path('styles')
        if not styles.exists():
            styles.mkdir

        components = src / Path('components')
        if not components.exists():
            components.mkdir()


def build(settings={}):
    settings = read_settings()
    project_dir = find_project_dir() 
    # TODO


def serve(settings={}):
    settings = read_settings()
    PORT = settings.get('port', 3000)
    # TODO