import os
import logging.config
from pathlib import Path

from django.utils.log import DEFAULT_LOGGING

ENV = os.environ

logging_config_path = Path(__file__).parent / "logging.conf"
logging.config.fileConfig(logging_config_path)
logger = logging.getLogger("time_log")
logger_level = ENV.get('LOG_LEVEL', 'INFO').upper()
logger.setLevel(getattr(logging, 'INFO'))

# the basic logger other apps can import
log = logging.getLogger(__name__)

LOGLEVEL = os.environ.get('LOGLEVEL', 'debug').upper()

dev_level_logger = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': [],
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # change debug level as appropiate
            'propagate': False,
        },
    },
}

prod_level_logger = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'console': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        'console': {'level': 'INFO', 'class': 'logging.StreamHandler'},
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            'propagate': True,
        },
        'time_log': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            # required to avoid double logging with root logger
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}