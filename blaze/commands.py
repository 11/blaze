from lib import read_settings 


def init(folder=None, type='static'):
    pass


def build(settings={}):
    settings = read_settings()
    # TODO


def serve(settings={}):
    settings = read_settings()
    PORT = settings.get('port', 3000)
    # TODO