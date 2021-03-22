import logging


logging.basicConfig(level = logging.INFO, filemode = 'W')

print('logging demo')
logging.info('this is info mess')
logging.debug('this is dbug mess')
logging.critical('this is critical mess')
logging.error('this is error mess' )
logging.warning('this is warning mes')
