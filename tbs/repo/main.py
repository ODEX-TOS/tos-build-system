import tbs.dependencies.main as dependency
import tbs.helper.checks as checks
import tbs.helper.download as download
import tbs.logger.log as logger
import tbs.helper.filedescriptor as fd
import tbs.kernel.main as kernel
import tbs.upload.main as upload
import os

def main(args):
    """
    This is the main function of the repo runner
    It will be executed with the arguments suplied if the end user called this.
    """
    dependency.installCommon()
    dependency.installFullRepo()
    if not checks.inCorrectDirectory("repo"):
        logger.log("Could not detect build files in the current directory, Setting up environment")
        download.downloadRepo("repo")
    logger.log("Build files should be here: {}".format(os.getcwd()))

    if args.packages:
        buildBase(args.upload)
    elif args.fonts:
        buildFonts(args.upload)
    elif args.kernel:
        buildKernel(args.upload)
    elif args.sync:
        syncRepo(args.upload)
    elif args.list:
        listAllPackages()
    elif args.list_fonts:
        listFonts()
    elif args.list_packages:
        listPackages()
    elif args.all:
        BuildFullRepo(args.upload)


def buildBase():
    """
    Build all base packages
    """
    result = fd.CMD(["./build.sh", "-a"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when building packages")
        raise Exception(result.stderr)

def buildFonts():
    """
    Build all fonts
    """
    result = fd.CMD(["./build.sh", "-f"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when building fonts")
        raise Exception(result.stderr)

def buildKernel():
    """
    Build the tos kernel using auto settings
    """
    kernel.main({"auto": True, "build": True})

def syncRepo():
    """
    Sync the repository packages with the package database
    """
    result = fd.CMD(["bash", "-c", "cd arch && repo-add tos.db.tar.gz *.pkg.tar.*"]).execute(True)
    if not result.exitcode == 0:
        logger.log("Something went wrong when syncing packages to the repo")
        raise Exception(result.stderr)

def BuildFullRepo(bUpload=True):
    """
    Build the base packages together with the font packages and the tos kernel.
    Afterwards sync the tos repo and upload it all to the cloud
    """
    buildBase()
    buildFonts()
    buildKernel()
    syncRepo()
    if bUpload:
        logger.log("Detected upload option after full build.")
        upload.main({"all": True}) # upload everything

def listFonts():
    """
    List all fonts to build
    """
    packages = fd.CMD(["bash", "-c", "sed -e 's:#.*::g' -e '/^\s*$/d' packages.conf | tr -s ' ' "]).execute()
    print(packages.stdout)

def listPackages():
    """
    List packages that will be build for the current repo
    """
    packages = fd.CMD(["bash", "-c", """
    grep -R -h "^pkgname=[a-zA-Z0-9-]*\s*" BUILD | sed -e 's:pkgname=::g' -e ':["$_]*::'
    """]).execute()
    print(packages.stdout)
    packages = fd.CMD(["bash", "-c", "sed -e 's:#.*::g' -e '/^\s*$/d' packages.conf | tr -s ' ' "]).execute()
    print(packages.stdout)

def listAllPackages():
    """
    List packages that will be build for the current repo
    """
    listPackages()
    listFonts()
