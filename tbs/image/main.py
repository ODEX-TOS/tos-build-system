import tbs.logger.log as logger
import tbs.helper.checks as checks
import tbs.helper.filedescriptor as fd
import tbs.dependencies.main as dependency
import os

def main(args):
    """
    This is the main function of the image runner
    It will be executed with the arguments suplied if the end user called this.
    """
    checks.checkRoot("Trying to build tos images without root privileges\nIf you are using environment variables don't forget to set them in your root session")
    dependency.installCommon()
    dependency.installImage()
    if not inCorrectDirectory():
        logger.log("Could not detect build files in the current directory. Setting up environment", logger.LOG_WARM)
        downloadRepo()
    logger.log("Build files should be here: {}".format(os.getcwd()))
    print(args)
    local = "-a" if args.azerty else ""
    if args.awesome:
        BuildAwesome(local)
    elif args.server:
        BuildServer(local)
    elif args.suite:
        BuildAwesome(local)
        BuildServer(local)
    elif args.all:
        BuildAwesome("")
        BuildServer("")
        BuildAwesome("-a")
        BuildServer("-a")
    

def inCorrectDirectory():
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
    os.chdir(result.stdout+"/toslive")
    return True

def downloadRepo():
    """
    Try to download the tos image repository and make that the current directory
    """
    result = fd.CMD(["git", "clone", "https://github.com/ODEX-TOS/tos-live.git"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when trying to download build files", logger.LOG_ERROR)
        raise Exception(result.stderr)
    os.chdir("tos-live/toslive")

def BuildAwesome(local=""):
    """
    local is the command to be supplied to the build script
    only call this command if you are have the build files in the current directory
    """
    result = fd.CMD(["bash", "-c", "./start.sh -awesome {}".format(local)]).execute(True)
    if not result.exitcode == 0:
        logger.log("Failed to build the package, please review the logs", logger.LOG_ERROR)
        raise Exception(result.stderr)

def BuildServer(local=""):
    """
    local is the command to be supplied to the build script
    only call this command if you are have the build files in the current directory
    """
    result = fd.CMD(["bash", "-c", "./start.sh -s {}".format(local)]).execute(True)
    if not result.exitcode == 0:
        logger.log("Failed to build the package, please review the logs", logger.LOG_ERROR)
        raise Exception(result.stderr)
    

