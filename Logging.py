import logging

logging.basicConfig(filename='example.log', filemode='w', format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)  #logs to same directory as script, overwrite each time, add datetime

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')