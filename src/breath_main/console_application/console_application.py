from breath_api_interface import request
from breath_api_interface.proxy import ServiceProxy
from breath_api_interface.queue import Queue
from breath_api_interface.service_interface import Service
from breath_api_interface.request import Request, Response
from .climate_request import get_clima
import pdb

import sys

class ConsoleApplication(Service):
	def __init__(self, proxy:ServiceProxy, request_queue:Queue, global_response_queue:Queue):
		'''ConsoleApplication constructor.
		'''
		super().__init__(proxy, request_queue, global_response_queue, "ConsoleApplication")

		sys.stdin = open(0)
		self._configured = False


	def run(self):

		print("Escolha uma opção:")
		print("1 - Construir base de dados")
		print("2 - Dados climáticos atuais de qualidade do ar de uma cidade")

		if self._configured:
			print("3 - Histórico de doenças respiratórias da cidade")
			print("4 - Probablidade de doenças agora")
			print("5 - Registrar meus sintomas")
			print("6 - Ver histórico de sintomas")
		print("7 - Sair da aplicação")

		
		opcao = sys.stdin.readline()
		opcao = int(opcao)

		if opcao == 1:
			response = self._send_request("DataWorkflow", "run_workflow", request_info={"workflow_name":"BDDownloader"})

			if response.sucess:
				self._configured = True
			else:
				print("Problema ao iniciar banco de dados: "+response.response_data["message"])
		
		elif opcao == 2:
			get_clima()
		elif opcao == 7:
			self._send_request("SESSION_MANAGER", "exit")
		elif self._configured:
			...