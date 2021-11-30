import unittest
import sys

sys.path.append("..\src")

from breath.session_manager import ProcessSessionManager

class ProcessCreationTest(unittest.TestCase):

    def test_creation_fail(self):
        session_manager = ProcessSessionManager()

        with self.assertRaises(ValueError):
            session_manager.create_service("random_wrong_service_name")

    def test_creation(self):
        session_manager = ProcessSessionManager()

        session_manager.create_service("BDAcessPoint")