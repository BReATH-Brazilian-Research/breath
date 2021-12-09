import time 
from breath_api_interface import request
from breath_api_interface.proxy import ServiceProxy
from breath_api_interface.queue import Queue
from breath_api_interface.service_interface import Service
from breath_api_interface.request import Request, Response
from ..data_requester.climate_request import get_clima
import pdb

import unicodedata
import sys
from datetime import date
import datetime

import numpy as np
from matplotlib import pyplot as plt

SEC_IN_DAY = 86400

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
			print("3 - Histórico de sintomas em uma cidade")
			print("4 - Casos de sintomas em uma cidade por data")
			print("5 - Histórico de temperatura em uma cidade (Aviso: em otimização)")
			print("5 - Probablidade de doenças agora")
			print("7 - Registrar meus sintomas")
		print("0 - Sair da aplicação")

		
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
		elif opcao == 0:
			self._send_request("SESSION_MANAGER", "exit")
		elif self._configured:
			if opcao == 3:
				self._print_casos()
			elif opcao == 4:
				self._print_casos_dia()
			elif opcao == 5:
				self._plot_temperatura()
			elif opcao == 7:
				self._register_symptom()

	def _get_city_name(self) -> str:
		print("Digite o nome da cidade")
		
		nome_cidade = self._input()
		nome_cidade = strip_accents(nome_cidade)
		nome_cidade = str.lower(nome_cidade)

		return nome_cidade

	def _get_casos(self, nome_cidade):
		response = self._send_request("BDAcessPoint", "get_casos", {"city_name":nome_cidade})

		data = response.response_data["data"]
		description = response.response_data["description"]

		description = np.asarray(description)
		dia_index = np.argwhere(description=="DIA")
		casos_index = np.argwhere(description=="Casos")

		data = np.asarray(data)

		if len(data) == 0:
			print("Cidade não existente na base de dados")
			return None, None

		dias : np.ndarray= data[:, dia_index].flatten().astype(np.float32)
		casos : np.ndarray = data[:, casos_index].flatten().astype(np.float32)

		return dias, casos

	def _get_temperatura(self,  nome_cidade):
		response = self._send_request("BDAcessPoint", "get_temperature", {"city_name":nome_cidade})

		data = response.response_data["data"]
		description = response.response_data["description"]

		data = np.asarray(data)
		if len(data) == 0:
			print("Cidade não existente na base de dados")
			return None, None


		description = np.asarray(description)
		dia_index = np.argwhere(description=="DIA")
		temp_min_index = np.argwhere(description=="Temp_min")
		temp_max_index = np.argwhere(description=="Temp_max")

		dias : np.ndarray= data[:, dia_index].flatten().astype(np.float32)
		temp_min : np.ndarray = data[:, temp_min_index].flatten().astype(np.float32)
		temp_max : np.ndarray = data[:, temp_max_index].flatten().astype(np.float32)

		return dias, temp_min, temp_max

	def _print_casos(self):
		nome_cidade = self._get_city_name()
		dias, casos = self._get_casos(nome_cidade)

		if dias is None:
			return

		plt.plot(dias, casos)
		plt.ylabel("Casos diários")
		plt.xlabel("Dia")
		plt.suptitle("Casos em "+nome_cidade)
		plt.title("Febre, gripe ou dor de garganta")	

		plt.show()

	def _print_casos_dia(self):
		nome_cidade = self._get_city_name()
		dias, casos = self._get_casos(nome_cidade)

		if dias is None:
			return

		print("Digite o dia desejado no formato dd/mm/aaaa")
		data = self._input()

		try:
			dt = datetime.datetime.strptime(data, "%d/%m/%Y")
		except Exception:
			print("Formato de dia incorreto.")
			return

		dia = dt.timestamp()/SEC_IN_DAY
		dia = int(dia)

		index = np.argwhere(dias == dia)

		if len(index) == 0:
			print("Data não disponível.")

			data_min = datetime.datetime.fromtimestamp(dias.min()*SEC_IN_DAY).strftime("%d/%m/%Y")
			data_max = datetime.datetime.fromtimestamp(dias.max()*SEC_IN_DAY).strftime("%d/%m/%Y")

			print("Disponível datas entre: "+data_min+" e "+data_max)

			return

		casos_dia = casos[index].flatten()

		print("Casos em "+ data + " na cidade de "+nome_cidade+": "+str(casos_dia[0]))
	
	def _register_symptom(self) -> bool:
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
	def _plot_temperatura(self):
		nome_cidade = self._get_city_name()
		dias, temp_min, temp_max = self._get_temperatura(nome_cidade)

		plt.plot(dias, temp_min)
		plt.plot(dias, temp_max)
		plt.xlabel("Dias")
		plt.ylabel("Temperatura [ºC]")
		plt.legend(["Temperatura mínima", "Temperatura máxima"])
		plt.title("Histórico de temperatura na cidade de "+nome_cidade)
		plt.show()