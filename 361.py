import logging


logging.basicConfig(format = '%(filename)s : %(name)s')
print('logging demo')
logging.critical('this is critical mess')
logging.error('this is error mess' )
logging.warning('this is warning mes')
logging.info('this is info mess')
logging.debug('this is dbug mess')