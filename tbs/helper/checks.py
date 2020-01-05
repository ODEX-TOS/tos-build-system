import os
import tbs.logger.log as logger
import tbs.helper.filedescriptor as fd
def checkRoot(message):
    """
    Check if the user is root otherwise error out
    """
    if os.geteuid() != 0:
        logger.log(message, logger.LOG_ERROR)
        raise Exception("You need root privileges to do this operation.")

def inCorrectDirectory(subpath="toslive"):
    """
    try to check if the current directory is the directory containing the build files
    """
    # check if the current repo is correct
    result = fd.CMD(["git", "remote", "-v"]).execute()
    if not result.exitcode == 0:
        logger.log("Something went wrong when scanning the current directory for build files")
        raise Exception(result.stderr)
    if not "ODEX-TOS/tos-live" in result.stdout:
        logger.log("Current directory does not contain build files, downloading files")
        return False
    result = fd.CMD(["git", "rev-parse", "--show-toplevel"]).execute()
    if not result.exitcode == 0:
        logger.log("Could not move to the correct location in the repo")
        raise Exception(result.stderr)
    os.chdir(result.stdout+"/"+subpath)
    return True