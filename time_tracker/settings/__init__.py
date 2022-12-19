from .common import *
import os


if os.environ.get("ENV_NAME") == 'production':
    from .prod import *
elif os.environ.get("ENV_NAME") == 'development':
    from .dev import *
else:
    from .local import *
