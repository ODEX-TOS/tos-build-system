"""
This file contains helper classes and methods for installing and checking packages
"""
# used to implement abstract base classes (much like interfaces)
from abc import ABC, abstractmethod 
import tbs.helper.filedescriptor as filedescriptor
import tbs.logger.log as logger
# interfaces
class IPackage(ABC):
    def __init__(self, package="base"):
        pass
    
    def isInstalled(self):
        """
        This method should tell if the package is installed on your system or not
        Returns True is the package is installed and False otherwise
        """
        pass
    def Install(self):
        """
        This method should install the package
        Returns False is the package failed to install.
        Returns True otherwise
        """
        pass

class IPackages(ABC):
    def __init__(self, packages=["base"]):
        pass
    
    def isInstalled(self):
        """
        This method should tell if all packages are installed on the system or not
        Returns True if all packages are installed and False otherwise
        """
        pass
    def Install(self):
        """
        This method should install all packages
        Returns False if one package failed to install
        Returns True otherwise
        """
        pass
# end interfaces

class MockPackage(IPackage):
    """
    Used for testing. This uses a mock implementation of installing packages
    """
    def __init__(self, package):
        self.package = package
        self.installed = []
    def setMockInstalled(self, installed):
        self.installed = installed

    def isInstalled(self):
        return self.package in self.installed

    def Install(self):
        self.installed.append(self.package)
        return self.isInstalled

class Package(IPackage):
    def __init__(self, package):
        self.package = package

    def isInstalled(self):
        packages = filedescriptor.CMD(['pacman', '-Q']).execute().stdout.split("\n")
        # strip out version number
        packages = [package.split(" ")[0] for package in packages]
        mock = MockPackage(self.package)
        mock.setMockInstalled(packages)
        return mock.isInstalled()

    # TODO: implement Arch install script
    def Install(self):
        result = filedescriptor.CMD(['yay',  "-Syu" ,"--noconfirm", self.package]).execute(True)
        if not result.exitcode == 0:
            logger.log("Something failed during the package installation procedure", logger.LOG_ERROR)
            return False
        return self.isInstalled()


class MockPackages(IPackages):
    """
    Used for testing. This uses a mock implementation of installing packages
    """
    def __init__(self, packages):
        self.packages = packages
        self.installed = []
    def setMockInstalled(self, installed):
        self.installed = installed

    def isInstalled(self):
        for package in self.packages:
            if not package in self.installed:
                logger.log("Package is not in the installed list: {}".format(package), logger.LOG_WARM)
                return False
        return True

    def Install(self):
        for package in self.packages:
            self.installed.append(package)
        return self.isInstalled()

class Packages(IPackages):
    def __init__(self, packages):
        self.packages = packages

    def isInstalled(self):
        packages = filedescriptor.CMD(['pacman', '-Q']).execute().stdout.split("\n")
        # strip out version number
        packages = [package.split(" ")[0] for package in packages]
        mock = MockPackages(self.packages)
        mock.setMockInstalled(packages)
        return mock.isInstalled()

    # TODO: implement arch install script
    def Install(self):
        result = filedescriptor.CMD(['yay',  "-Syu" ,"--noconfirm"] + self.packages).execute(True)
        if not result.exitcode == 0:
            logger.log("Something failed during the package installation procedure", logger.LOG_ERROR)
            return False
        return self.isInstalled()

    