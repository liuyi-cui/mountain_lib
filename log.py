import logging
from logging.config import dictConfig

logging_config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(name) -12s %(levelname) -8s %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname) -8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',  # 输出到控制台
            'formatter': 'default',
            'level': logging.DEBUG
        },
        'simple_console': {
            'class': "logging.FileHandler" ,  # 输出到本地文本
            'formatter': 'simple',
            'level': logging.WARNING,
            'filename': 'logging.log'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': logging.DEBUG,
        },
        'simple': {
            'handlers': ['simple_console'],
            'level': logging.ERROR,
            'propagate': False
        }
    },
}

dictConfig(logging_config)
logger = logging.getLogger(__name__)
logger.debug('这是debug级别的log：%s', 'debug')
logger.error('这是error级别的log:%s', 'error')

simple_logger = logging.getLogger('simple')
simple_logger.debug('这是debug级别的log')
simple_logger.error('这是error级别的log')
