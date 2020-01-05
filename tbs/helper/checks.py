import os
import tbs.logger.log as logger

def checkRoot(message):
    """
    Check if the user is root otherwise error out
    """
    if os.geteuid() != 0:
        logger.log(message, logger.LOG_ERROR)
        raise Exception("You need root privileges to do this operation.")