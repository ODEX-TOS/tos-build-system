import tbs.helper.filedescriptor as fd
import tbs.logger.log as logger
import os
def downloadRepo(subpath="toslive"):
    """
    Try to download the tos image repository and make that the current directory
    """
    result = fd.CMD(["git", "clone", "https://github.com/ODEX-TOS/tos-live.git"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when trying to download build files, checking for existing build files", logger.LOG_ERROR)
    os.chdir("tos-live/"+subpath)