from decouple import config

if config('ENV_TYPE') == 'DEVELOPMENT':
    from .local import *
else:
    from .production import *