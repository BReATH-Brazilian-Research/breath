#from breath_api_interface import request
#from breath_api_interface.proxy import ServiceProxy
#from breath_api_interface.queue import Queue
#from breath_api_interface.service_interface import Service
#from breath_api_interface.request import Request, Response
import pdb

import sys

class ConsoleApplication():#Service):
	def __init__(self):#, proxy:ServiceProxy, request_queue:Queue, global_response_queue:Queue):
		'''ConsoleApplication constructor.
		'''
		super().__init__()#proxy, request_queue, global_response_queue, "ConsoleApplication")
		self._configured = False


	def run(self) -> bool:

		print("Escolha uma opção:")
		print("1 - Construir base de dados")
		print("2 - Dados climaticos de qualidade do ar de uma cidade")
		print("3 - Historico de doencas respiratorias da cidade")
		print("4 - Probablidade de doencas agora")
		print("5 - Registrar meus sintomas")
		print("6 - Ver historico de sintomas")
		print("7 - sair da aplicacao")

		
		opcao = int(input("Escolha:"))
		pdb.set_trace()

		if opcao == 7:
			return False
		return True

		#if opcao == 1:
		#    response = self._send_request(service_name="DataWorkflow", operation_name="load_open_sus_data")
#
		#if response.sucess:
		#    print("Operação realizada com sucesso!")
		#else:
		#    print("Erro: ", response.response_data["message"])

if __name__ == '__main__':
	console = ConsoleApplication()
	flag = True
	while flag == True:
		flag = console.run()
	