import tbs.helper.packages as installer
import tbs.dependencies.packages as packages
import tbs.logger.log as logger
def main(args):
    """
    This is the main function of the dependency runner
    It will be executed with the arguments suplied if the end user called this.
    You can install multiple things by supplying multiple options
    """
    logger.log("Trying to install dependencies with the following settings: {}".format(args))
    # always perform this install
    checkInstall(packages.GENERAL_PACKAGES)
    if args.all:
        installAll()
    elif args.repo_full:
        installFullRepo()
    else:
        if args.image:
            installImage()
        if args.kernel:
            installKernel()
        if args.upload:
            installUpload()
        if args.repo:
            installRepo()

def checkInstall(payload):
    """
    Check if packages are already installed otherwise install them
    This will trow an error if we are unable to install packages.
    Payload is a list of packages to install
    """
    logger.log("Trying to install: {}".format(payload))
    state = installer.Packages(payload)
    logger.log("State of package install: {}".format(state.isInstalled()))
    if state.isInstalled():
        return
    if not state.Install():
        logger.log("Something went wrong when trying to install packages to your system", logger.LOG_ERROR)
        raise Exception("Cannot install packages to your system. The culprit is in one of the following packages: \n {}".format(payload))
    logger.log("All packages are installed correctly")


def installImage():
    """
    Install all image dependencies
    """
    checkInstall(packages.IMAGE_PACKAGES)

def installKernel():
    """
    Install all kernel dependencies
    """
    checkInstall(packages.KERNEL_PACKAGES)

def installRepo():
    """
    Install all repo dependencies
    """
    checkInstall(packages.REPO_PACKAGES)

def installFullRepo():
    """
    Install all repo and kernel dependencies
    """
    installRepo()
    installKernel()

def installUpload():
    """
    Install all upload dependencies
    """
    checkInstall(packages.UPLOAD_PACKAGES)

def installAll():
    """
    Install all dependencies
    """
    installFullRepo()
    installImage()
    installUpload()