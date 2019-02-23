#!/bin/python
import sys

from infrastructure.configuration.Configuration import AppConfiguration

from application.usecase.StartMiningUseCase import StartMiningUseCase
from application.usecase.ReportUseCase import ReportUseCase

configuration = AppConfiguration()
logger = configuration.getLogger(__name__)

def mining():
    try:
        response = StartMiningUseCase().execute()
        logger.info('SizeOf: %d' % (len(response,)))
    except Exception as err:
        logger.fatal(err)
        pass

def report():
    try:
        ReportUseCase().execute()
    except Exception as err:
        logger.fatal(err)
        pass

if __name__ == '__main__':
    sizeOf = len(sys.argv)
    if sizeOf > 1:
        action = str(sys.argv[1])
        if action == 'mining':
            mining()
        elif action == 'report':
            report()
        else:
            logger.fatal('Action method not found!')
    else:
        mining()
        report()
