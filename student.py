import logging

logger=logging.getLogger('studentlogger.log')
logger.setLevel(logging.INFO)

filehandler = logging.FileHandler('studentlog.log','w')
filehandler.setLevel(logging.INFO)

formatter= logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                             datefmt = '%d/%m/%Y %I:%M:%S %p')

filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

logger.critical('it is critical mes')
logger.error('it is error mes')
logger.warning('it is warning mes')
logger.info('it is info mes')
logger.debug('it is debug mes')