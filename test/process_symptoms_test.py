import unittest
import sys

sys.path.append("..\src")

from src.breath.breath_patient_portal import RegisterSymptoms

class SymptomsRegisterTest(unittest.TestCase):

    def test_1(self):
        registrator = RegisterSymptoms(None, None, None, "RegisterSymptoms")

        _input = registrator.createInputExample([False, True, False, True, False, True, True, False, False, False], True, "")
        output = {
            "FEBRE": False,
            "TOSSE": True,
            "CALAFRIO": False,
            "DISPNEIA": True,
            "GARGANTA": False,
            "ARTRALGIA": True,
            "MIALGIA": True,
            "CONJUNTIV": False,
            "CORIZA": False,
            "DIARREIA": False,
            "OUTRO_SIN": False,
            "OUTRO_DES": ""
        }

        self.assertEqual(registrator.processSymptomsInput(_input),  output)
    
    def test_2(self):
        registrator = RegisterSymptoms(None, None, None, "RegisterSymptoms")

        _input = registrator.createInputExample([True, False, True, False, True, False, False, True, False, True], False, "SUDORESE")
        output = {
            "FEBRE": True,
            "TOSSE": False,
            "CALAFRIO": True,
            "DISPNEIA": False,
            "GARGANTA": True,
            "ARTRALGIA": False,
            "MIALGIA": False,
            "CONJUNTIV": True,
            "CORIZA": False,
            "DIARREIA": True,
            "OUTRO_SIN": False,
            "OUTRO_DES": ""
        }

        self.assertEqual(registrator.processSymptomsInput(_input),  output)
    
    def test_3(self):
        registrator = RegisterSymptoms(None, None, None, "RegisterSymptoms")

        _input = registrator.createInputExample([False, False, False, True, True, False, True, True, True, False], True, "ENXAQUECA")
        output = {
            "FEBRE": False,
            "TOSSE": False,
            "CALAFRIO": False,
            "DISPNEIA": True,
            "GARGANTA": True,
            "ARTRALGIA": False,
            "MIALGIA": True,
            "CONJUNTIV": True,
            "CORIZA": True,
            "DIARREIA": False,
            "OUTRO_SIN": True,
            "OUTRO_DES": "ENXAQUECA"
        }

        self.assertEqual(registrator.processSymptomsInput(_input),  output)
    
    def test_4(self):
        registrator = RegisterSymptoms(None, None, None, "RegisterSymptoms")

        _input = registrator.createInputExample([False, True, True, False, True, True, False, False, True, True], False, "")
        output = {
            "FEBRE": False,
            "TOSSE": True,
            "CALAFRIO": True,
            "DISPNEIA": False,
            "GARGANTA": True,
            "ARTRALGIA": True,
            "MIALGIA": False,
            "CONJUNTIV": False,
            "CORIZA": True,
            "DIARREIA": True,
            "OUTRO_SIN": False,
            "OUTRO_DES": ""
        }

        self.assertEqual(registrator.processSymptomsInput(_input),  output)

    def test_5(self):
        registrator = RegisterSymptoms(None, None, None, "RegisterSymptoms")

        _input = registrator.createInputExample([True, False, True, False, False, True, False, True, True, False], True, "")
        output = {
            "FEBRE": True,
            "TOSSE": False,
            "CALAFRIO": True,
            "DISPNEIA": False,
            "GARGANTA": False,
            "ARTRALGIA": True,
            "MIALGIA": False,
            "CONJUNTIV": True,
            "CORIZA": True,
            "DIARREIA": False,
            "OUTRO_SIN": False,
            "OUTRO_DES": ""
        }

        self.assertEqual(registrator.processSymptomsInput(_input),  output)
    
    def test_6(self):
        registrator = RegisterSymptoms(None, None, None, "RegisterSymptoms")

        _input = registrator.createInputExample([True, True, False, False, False, False, True, False, True, True], False, "DESENTERIA")
        output = {
            "FEBRE": True,
            "TOSSE": True,
            "CALAFRIO": False,
            "DISPNEIA": False,
            "GARGANTA": False,
            "ARTRALGIA": False,
            "MIALGIA": True,
            "CONJUNTIV": False,
            "CORIZA": True,
            "DIARREIA": True,
            "OUTRO_SIN": False,
            "OUTRO_DES": ""
        }

        self.assertEqual(registrator.processSymptomsInput(_input),  output)

    def test_7(self):
        registrator = RegisterSymptoms(None, None, None, "RegisterSymptoms")

        _input = registrator.createInputExample([True, False, False, True, False, False, False, False, False, False], False, "")
        output = {
            "FEBRE": True,
            "TOSSE": False,
            "CALAFRIO": False,
            "DISPNEIA": True,
            "GARGANTA": False,
            "ARTRALGIA": False,
            "MIALGIA": False,
            "CONJUNTIV": False,
            "CORIZA": False,
            "DIARREIA": False,
            "OUTRO_SIN": False,
            "OUTRO_DES": ""
        }

        self.assertEqual(registrator.processSymptomsInput(_input),  output)
    
    def test_8(self):
        registrator = RegisterSymptoms(None, None, None, "RegisterSymptoms")

        _input = registrator.createInputExample([True, True, True, True, True, True, True, True, False, True], True, "TAQUICARDIA")
        output = {
            "FEBRE": True,
            "TOSSE": True,
            "CALAFRIO": True,
            "DISPNEIA": True,
            "GARGANTA": True,
            "ARTRALGIA": True,
            "MIALGIA": True,
            "CONJUNTIV": True,
            "CORIZA": False,
            "DIARREIA": True,
            "OUTRO_SIN": True,
            "OUTRO_DES": "TAQUICARDIA"
        }

        self.assertEqual(registrator.processSymptomsInput(_input),  output)