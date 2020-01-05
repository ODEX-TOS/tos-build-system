import unittest
import tbs.helper.filedescriptor as filedescriptor

# TODO: write a test case for testing stderr

class TestFileDescriptor(unittest.TestCase):
    def test_mock_command_set(self):
        desc = filedescriptor.MockCMD()
        self.assertTrue(desc.command == ['ls', '-la'])
        self.assertTrue(desc.decoder == 'utf-8')
    
    def test_mock_std_equals_input(self):
        desc = filedescriptor.MockCMD()
        desc.execute()
        self.assertTrue(desc.stdout == "".join(desc.command))
        self.assertTrue(desc.stderr == "".join(desc.command))
    
    def test_mock_stdout_equals_input_with_object_return(self):
        desc = filedescriptor.MockCMD()
        desc = desc.execute()
        self.assertTrue(desc.stdout == "".join(desc.command))
        self.assertTrue(desc.stderr == "".join(desc.command))
    
    def test_real_cmd_runner_works_with_echo(self):
        desc = filedescriptor.CMD(['echo', 'hello']).execute()
        self.assertTrue(desc.stdout == "hello\n")
        self.assertFalse(desc.stderr == "hello\n")
    
    def test_real_cmd_runner_works_with_printf(self):
        desc = filedescriptor.CMD(['printf', 'hello']).execute()
        self.assertTrue(desc.stdout == "hello")
        self.assertFalse(desc.stderr == "hello")

