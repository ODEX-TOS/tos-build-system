import tbs.dependencies.main as dependency
import tbs.helper.checks as checks
import tbs.helper.download as download
import tbs.logger.log as logger
import tbs.helper.filedescriptor as fd
import os

def uploadRepo():
    """
    Upload an existing repository.
    Only execute this if a full repository exists.
    Otherwise the repository will be incomplete
    """
    result = fd.CMD(["./upload.sh", "-y"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when uploading data to the server",logger.LOG_ERROR)
        raise Exception(result.stderr)

def uploadImage():
    """
    Upload already build images.
    It only works if images are build in the toslive setting.
    Otherwise the repository will be incomplete
    """
    result = fd.CMD(["./build.sh", "-u"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when moving existing images",logger.LOG_ERROR)
        raise Exception(result.stderr)
    result = fd.CMD(["./upload.sh", "-y"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when uploading data to the server",logger.LOG_ERROR)
        raise Exception(result.stderr)

def main(args):
    """
    This is the main function of the upload runner
    It will be executed with the arguments suplied if the end user called this.
    """
    dependency.installCommon()
    dependency.installUpload()
    if not checks.inCorrectDirectory("repo"):
        logger.log("Could not detect build files in the current directory, Setting up environment")
        download.downloadRepo("repo")
    logger.log("Build files should be here: {}".format(os.getcwd()))

    if args.repo:
        uploadRepo()
    elif args.image:
        uploadImage()
    elif args.all:
        uploadRepo()
        uploadImage()