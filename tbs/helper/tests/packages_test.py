import unittest
import tbs.helper.packages as packages
# installed packages as a mock
installed = ["base", "systemd", "zlib", "awesome-tos"]

class TestPackage(unittest.TestCase):
    def test_package_not_installed(self):
        package = packages.MockPackage("git")
        package.setMockInstalled(installed)
        self.assertFalse(package.isInstalled())
        self.assertTrue(package.Install())
        self.assertTrue(package.isInstalled)
    def test_package_already_installed(self):
        package = packages.MockPackage(installed[0])
        package.setMockInstalled(installed)
        self.assertTrue(package.isInstalled())
        self.assertTrue(package.Install())
        self.assertTrue(package.isInstalled)
    

class TestPackages(unittest.TestCase):
    def test_packages_not_installed(self):
        package = packages.MockPackage(["git"])
        package.setMockInstalled(installed)
        self.assertFalse(package.isInstalled())
        self.assertTrue(package.Install())
        self.assertTrue(package.isInstalled)

    def test_packages_already_installed(self):
        package = packages.MockPackage([installed[0]])
        package.setMockInstalled(installed)
        self.assertTrue(package.isInstalled())
        self.assertTrue(package.Install())
        self.assertTrue(package.isInstalled)

    def test_packages_not_installed_multiple(self):
        package = packages.MockPackage(["git", "awesome-tos"])
        package.setMockInstalled(installed)
        self.assertFalse(package.isInstalled())
        self.assertTrue(package.Install())
        self.assertTrue(package.isInstalled)

    def test_packages_already_installed(self):
        package = packages.MockPackage([installed[0], "gattlib"])
        package.setMockInstalled(installed)
        self.assertFalse(package.isInstalled())
        self.assertTrue(package.Install())
        self.assertTrue(package.isInstalled)
   

