#!/bin/python
import sys
import json

from infrastructure.configuration.Configuration import AppConfiguration

from application.usecase.StartMiningUseCase import StartMiningUseCase
from application.usecase.ReportUseCase import ReportUseCase

configuration = AppConfiguration()
logger = configuration.getLogger(__name__)

def mining():
    try:
        response = StartMiningUseCase().execute()
        logger.info('Mining - SizeOf: %d' % (len(response,)))
    except Exception as err:
        logger.fatal(err)
        pass

def report():
    try:
        response = ReportUseCase().execute()
        logger.info('Report - SizeOf: %d' % (len(response,)))
        for data in response:
            logger.info('Name: %s - Price: %s - Capitalization: %s' % (data.name, data.price, data.capitalization,))
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
