import tbs.logger.log as logger
import tbs.helper.checks as checks
import tbs.helper.filedescriptor as fd
import tbs.helper.download as download
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
    if not checks.inCorrectDirectory():
        logger.log("Could not detect build files in the current directory. Setting up environment", logger.LOG_WARM)
        download.downloadRepo()
    logger.log("Build files should be here: {}".format(os.getcwd()))
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
    

