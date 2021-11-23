import unittest
import sys

sys.path.append("..\src")

from breath.session_manager import ProcessSessionManager

class BDTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		self.session_session = ProcessSessionManager()
		self.session_session.create_service("BDAcessPoint")

	@classmethod
	def tearDownClass(cls):
		self.bd.__del__()

	def setUp(cls):
		pass

	def tearDown(cls):
		pass

	def test_data_insertion(self):
		
		#send_request(self, service_name, operation_name, request_info=None, wait_for_response=True)
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "register_user", request_info = {name:'Joao',age:'19', gender:'Helicoptero Apache'}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "register_symptom", request_info = {symptom_name:'Tosse',year:'19', month:'Helicoptero Apache', day:'day'}, wait_for_response=False), second, "Sucesso")
		# self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "register_symptom_type", request_info = {name:'Joao',age:'19', gender:'Helicoptero Apache'}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "register_city", request_info = {cod:'323',nome:'Varginha', uf:'VW'}, wait_for_response=False), second, "Sucesso")
		# self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "register_patient", request_info = {name:'Joao',age:'19', gender:'Helicoptero Apache'}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "register_workflow", request_info = {name:'workflow1'}, wait_for_response=False), second, "Sucesso")

	def test_data_query(self):
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "search_symptom_type", request_info = {symptom_name:'Tosse'}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "search_user", request_info = {user_id: 1}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "get_symptoms_types", request_info = {}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "is_workflow_runned", request_info = {workflow_name:'workflow1'}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "get_climate_interval", request_info = {initial:'12/10/2016',final:'12/10/2017'}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "get_climate_date", request_info = {date:'12/10/2017'}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "get_SRAG_interval", request_info = {initial:'12/10/2016',final:'12/10/2017'}, wait_for_response=False), second, "Sucesso")
		self.assertAlmostEqual(self.session_session.send_request("BDAcessPoint", "get_SRAG_date", request_info = {date:'12/10/2017'}, wait_for_response=False), second, "Sucesso")




if __name__ == '__main__':
	unittest.main()