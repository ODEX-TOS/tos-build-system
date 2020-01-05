"""
This module is used to extract filedescriptors from a given command
"""
from abc import ABC, abstractmethod 
import subprocess
import tbs.logger.log as logger

class Icmd(ABC):
    """
    This class is used to extract commands in the form of strings from a given input command
    """
    def __init__(self, command=['ls', '-la'], decoder='utf-8'):
        self.command = command
        self.decoder=decoder
        self.stdout = None
        self.stderr = None
    
    def execute(self):
        """
        execute the given command and return a Icmd object that holds the results
        """
        pass

class MockCMD(Icmd):
    def __init__(self, command=['ls', '-la'], decoder='utf-8'):
        self.command = command
        self.decoder=decoder
        self.stdout = None
        self.stderr = None
    def execute(self):
        self.stdout = "".join(self.command)
        self.stderr = self.stdout
        return self

class CMD(Icmd):
    def __init__(self, command=['ls', '-la'], decoder='utf-8'):
        self.command = command
        self.decoder=decoder
        self.stdout = None
        self.stderr = None
        self.exitcode = 0
    def execute(self, bPrintOutput=False):
        result = subprocess.Popen(self.command, 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT, bufsize=10)
        self.stdout = ""
        self.stderr = ""
        with result.stdout:
            for line in iter(result.stdout.readline, b''): # b'\n'-separated lines
                line = line.decode(self.decoder)
                if bPrintOutput:
                    logger.log(line.replace("\n", ""))
                self.stdout += line
        self.exitcode = result.wait()
        return self