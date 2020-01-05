import tbs.helper.filedescriptor as fd
import os
def downloadRepo(subpath="toslive"):
    """
    Try to download the tos image repository and make that the current directory
    """
    result = fd.CMD(["git", "clone", "https://github.com/ODEX-TOS/tos-live.git"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when trying to download build files", logger.LOG_ERROR)
        raise Exception(result.stderr)
    os.chdir("tos-live/"+subpath)