import logging

from celery.app.defaults import DEFAULT_TASK_LOG_FMT, DEFAULT_PROCESS_LOG_FMT


class CeleryTaskFilter(logging.Filter):

    def filter(self, record):
        return record.processName.find('Worker') != -1


class CeleryProcessFilter(logging.Filter):

    def filter(self, record):
        return record.processName == 'MainProcess'


class NotCeleryFilter(logging.Filter):
    def filter(self, record):
        return record.processName != 'MainProcess' and record.processName.find('Worker') == -1


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {  # Sets up the format of the logging output
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%y %b %d, %H:%M:%S',
        },
        'celeryTask': {
            '()': 'celery.app.log.TaskFormatter',
            'fmt': DEFAULT_TASK_LOG_FMT
        },
        'celeryProcess': {
            '()': 'celery.utils.log.ColorFormatter',
            'fmt': DEFAULT_PROCESS_LOG_FMT
        },
    },
    'filters': {
        'celeryTask': {
            '()': CeleryTaskFilter,
        },
        'celeryProcess': {
            '()': CeleryProcessFilter,
        },
        'notCelery': {
            '()': NotCeleryFilter,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['notCelery']
        },
        'console2': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'celeryTask',
            'filters': ['celeryTask']
        },
        'console3': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'celeryProcess',
            'filters': ['celeryProcess']
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'console2', 'console3'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}
