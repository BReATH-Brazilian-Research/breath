import unittest
import sys

from breath_main.session_manager import ProcessSessionManager

class ProcessCreationTest(unittest.TestCase):

    def test_creation_fail(self):
        session_manager = ProcessSessionManager()

        with self.assertRaises(ValueError):
            session_manager.create_service("random_wrong_service_name")

        del session_manager

    def test_creation(self):
        session_manager = ProcessSessionManager()

        session_manager.create_service("BDAcessPoint")

        del session_manager

if __name__ == '__main__':
	unittest.main()