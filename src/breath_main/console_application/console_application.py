from os import truncate
from breath_api_interface import request
from breath_api_interface.proxy import ServiceProxy
from breath_api_interface.queue import Queue
from breath_api_interface.service_interface import Service
from breath_api_interface.request import Request, Response
from .climate_request import get_clima
import pdb

import unicodedata
import sys

import numpy as np
from matplotlib import pyplot as plt

def strip_accents(text):
	#https://stackoverflow.com/questions/44431730/how-to-replace-accented-characters

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)


class ConsoleApplication(Service):
	def __init__(self, proxy:ServiceProxy, request_queue:Queue, global_response_queue:Queue):
		'''ConsoleApplication constructor.
		'''
		super().__init__(proxy, request_queue, global_response_queue, "ConsoleApplication")

		sys.stdin = open(0)
		self._configured = False

	def _input(self):
		return sys.stdin.readline()[:-1]

	def run(self):

		if not self._configured:
			response = self._send_request("BDAcessPoint", "is_workflow_runned", {"workflow_name":"BDDownloader"})
			if response.sucess == True:
				self._configured = True

		print("Escolha uma opção:")
		print("1 - Construir base de dados")
		print("2 - Dados climáticos atuais de qualidade do ar de uma cidade")

		if self._configured:
			print("3 - Histórico de doenças respiratórias da cidade")
			print("4 - Probablidade de doenças agora")
			print("5 - Registrar meus sintomas")
			print("6 - Ver histórico de sintomas")
		print("7 - Sair da aplicação")

		
		opcao = self._input()
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
			if opcao == 3:
				self._print_casos()

	def _print_casos(self):
		print("Digite o nome da cidade")
		
		nome_cidade = self._input()
		nome_cidade = strip_accents(nome_cidade)
		nome_cidade = str.lower(nome_cidade)

		response = self._send_request("BDAcessPoint", "get_casos", {"city_name":nome_cidade})

		data = response.response_data["data"]
		description = response.response_data["description"]

		description = np.asarray(description)
		dia_index = np.argwhere(description=="DIA")
		casos_index = np.argwhere(description=="Casos")

		data = np.asarray(data)

		dias = data[:, dia_index].flatten()
		casos = data[:, casos_index].flatten()

		plt.plot(dias, casos)
		plt.ylabel("Casos diários")
		plt.xlabel("Dia")
		plt.suptitle("Casos em "+nome_cidade)
		plt.title("Febre, gripe ou dor de garganta")

		plt.show()
