import tbs.dependencies.main as dependency
import tbs.helper.checks as checks
import tbs.helper.download as download
import tbs.logger.log as logger
import os

def main(args):
    """
    This is the main function of the kernel runner
    It will be executed with the arguments suplied if the end user called this.
    """
    dependency.installCommon()
    dependency.installKernel()
    if not checks.inCorrectDirectory("repo"):
        logger.log("Could not detect build files in the current directory, Setting up environment")
        download.downloadRepo("repo")
    logger.log("Build files should be here: {}".format(os.getcwd()))
    cores = args.cores
    if args.auto:
        logger.log("Automatically detecting the amount of cores your system has...")
        import multiprocessing
        cores = multiprocessing.cpu_count() 
        logger.log("Detected {} cores".format(cores))
    if args.build:
        logger.log("Building the kernel using {} cores".format(cores))
        buildKernel(cores)

def buildKernel(cores):
    """
    This should only be executed if you are in the correct repo
    cores should be an integer telling us howmany cores to use to compile the kernel
    """
    result = fd.CMD(["bash", "-c", "./build.sh -k {}".format(cores)]).execute(True)
    if not result.exitcode == 0:
        logger.log("Failed to build the kernel, please review the logs", logger.LOG_ERROR)
        raise Exception(result.stderr)