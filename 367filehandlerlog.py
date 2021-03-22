import logging

logger = logging.getLogger('flog')
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler('flog.log',mode = 'w')
fileHandler.setLevel(logging.WARNING)


formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                              datefmt = '%d/%m/%Y %I:%M:%S %p')

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.critical('it is critical mes')
logger.error('it is error mes')
logger.warning('it is warning mes')
logger.info('it is info mes')
logger.debug('it is debug mes')
