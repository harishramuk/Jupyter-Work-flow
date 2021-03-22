import logging
logger = logging.getLogger('consolelogger')
logger.setLevel(logging.WARNING)

consoleHandler =logging.StreamHandler(mode = 'w')
consoleHandler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s',
                              datefmt = '%d/%m/%Y  %I:%M:%S %p' )


consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

logger.critical('it is critical mes')
logger.error('it is error mes')
logger.warning('it is warning mes')
logger.info('it is info mes')
logger.debug('it is debug mes')