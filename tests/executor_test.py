import unittest
import mock
from mock import *

from resources.utils import *
from resources.disk_IO import *
from resources.executors import *
from resources.utils_kodi import *

class Test_executortests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        set_use_print(True)
        set_log_level(LOG_DEBUG)
        
    @patch('resources.executors.sys')            
    def test_if_on_linux_factory_loads_with_correct_executor(self, mock_sys):
        
        # arrange
        mock_sys.configure_mock(platform='linux')
        set_log_level(LOG_VERB)
        set_use_print(True)

        launcherPath = FileNameFactory.create('path')

        settings = {}
        settings['lirc_state'] = True

        # act
        factory = ExecutorFactory(settings, None)
        executor = factory.create(launcherPath)
        
        # assert
        actual = executor.__class__.__name__
        expected = 'LinuxExecutor'
        self.assertEqual(actual, expected)
                
    @patch('resources.executors.sys')            
    def test_if_on_windows_factory_loads_with_correct_executor(self, mock_sys):
        
        # arrange
        mock_sys.configure_mock(platform='win32')
        set_log_level(LOG_VERB)
        set_use_print(True)
        
        launcherPath = FileNameFactory.create('path')

        settings = {}
        settings['windows_cd_apppath'] = ''
        settings['windows_close_fds'] = ''

        # act
        factory = ExecutorFactory(settings, None)
        executor = factory.create(launcherPath)
        
        # assert
        actual = executor.__class__.__name__
        expected = 'WindowsExecutor'
        self.assertEqual(actual, expected)  
        
    @patch('resources.executors.sys')            
    def test_if_on_windows_with_bat_files_factory_loads_with_correct_executor(self, mock_sys):

        # arrange
        mock_sys.configure_mock(platform='win32')
        set_log_level(LOG_VERB)
        set_use_print(True)
        
        launcherPath = FileNameFactory.create('c:\\app\\testcase.bat')

        settings = {}
        settings['show_batch_window'] = False

        # act
        factory = ExecutorFactory(settings, None)
        executor = factory.create(launcherPath)
        
        # assert
        actual = executor.__class__.__name__
        expected = 'WindowsBatchFileExecutor'
        self.assertEqual(actual, expected)  

    @patch('resources.executors.sys')            
    def test_if_on_windows_with_lnk_files_factory_loads_with_correct_executor(self, mock_sys):

        # arrange
        mock_sys.configure_mock(platform='win32')
        set_log_level(LOG_VERB)
        set_use_print(True)
        
        launcherPath = FileNameFactory.create('c:\\app\\testcase.lnk')

        settings = {}

        # act
        factory = ExecutorFactory(settings, None)
        executor = factory.create(launcherPath)

        # assert
        actual = executor.__class__.__name__
        expected = 'WindowsLnkFileExecutor'
        self.assertEqual(actual, expected)
        
    def test_if_xbmc_apppath_factory_loads_with_correct_executor(self):
         
        # arrange
        set_log_level(LOG_VERB)
        set_use_print(True)
        
        launcherPath = FileNameFactory.create('c:\\boop\\xbmc.exe')

        settings = {}

        # act
        factory = ExecutorFactory(settings, None)
        executor = factory.create(launcherPath)

        # assert
        actual = executor.__class__.__name__
        expected = 'XbmcExecutor'
        self.assertEqual(actual, expected)
        
    @patch('resources.executors.sys')            
    def test_if_on_osx_factory_loads_with_correct_executor(self, mock_sys):

        # arrange
        mock_sys.configure_mock(platform='darwin')
        set_log_level(LOG_VERB)
        set_use_print(True)

        launcherPath = FileNameFactory.create('durp\\apple\\durp')

        settings = {}

        # act
        factory = ExecutorFactory(settings, None)
        executor = factory.create(launcherPath)

        # assert
        actual = executor.__class__.__name__
        expected = 'OSXExecutor'
        self.assertEqual(actual, expected)
       
    def test_when_using_urls_the_correct_web_executor_loads(self):
        
        # arrange
        launcherPath = FileNameFactory.create('durp\\apple\\durp')

        settings = {}

        # act
        factory = ExecutorFactory(settings, None)
        executor = factory.create(FileNameFactory.create('steam://rungameid/'))

        # assert
        actual = executor.__class__.__name__
        expected = 'WebBrowserExecutor'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
