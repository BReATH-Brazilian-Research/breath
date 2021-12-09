from breath_api_interface import request
from breath_api_interface.proxy import ServiceProxy
from breath_api_interface.queue import Queue
from breath_api_interface.service_interface import Service
from breath_api_interface.request import Request, Response
from ..data_requester.climate_request import get_clima
import pdb

import sys
from datetime import date

class ConsoleApplication(Service):
	def __init__(self, proxy:ServiceProxy, request_queue:Queue, global_response_queue:Queue):
		'''ConsoleApplication constructor.
		'''
		super().__init__(proxy, request_queue, global_response_queue, "ConsoleApplication")

		sys.stdin = open(0)
		self._configured = False


	def run(self) -> bool:

		print("Escolha uma opção:")
		print("1 - Construir base de dados")
		print("2 - Dados climáticos de qualidade do ar de uma cidade")
		print("3 - Histórico de doenças respiratórias da cidade")
		print("4 - Probablidade de doenças agora")
		print("5 - Registrar meus sintomas")
		print("6 - Ver histórico de sintomas")
		print("7 - Sair da aplicação")

		
		opcao = sys.stdin.readline()
		opcao = int(opcao)

		if opcao == 2:
			get_clima()
		elif opcao == 5:
			self.register_symptom()
		elif opcao == 7:
			self._send_request("SESSION_MANAGER", "exit")
		return True

		#if opcao == 1:
		#    response = self._send_request(service_name="DataWorkflow", operation_name="load_open_sus_data")
#
		#if response.sucess:
		#    print("Operação realizada com sucesso!")
		#else:
		#    print("Erro: ", response.response_data["message"])
	
	def register_symptom(self) -> bool:
		# Registrar paciente
		email = input("Qual o seu email?\n")

		# Registrar cidade
		city = input("Em qual cidade você se encontra?\n")

		# Registrar tipo de sintoma
		symptom_name = input("Qual sintoma você deseja registrar?\n")

		# Coletar tempo
		today = date.today()
		today_str = today.strftime("%d/%m/%Y")
		day = int(today_str[:2])
		month = int(today_str[3:5])
		year = int(today_str[6:])

		# Registrar sintoma
		response : Response = self._send_request("BDAcessPoint", "register_symptom", request_info={"symptom_name": symptom_name,"year":year,"month":month,"day":day,"patient_id":email,"city":city})
		if (response.sucess == False):
			print(response.response_data["mensagem"])
		return response.sucess

	