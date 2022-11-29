from decouple import config

if config('ENV_TYPE', 'DEVELOPMENT') == 'DEVELOPMENT':
    from .local import *
else:
    from .production import *