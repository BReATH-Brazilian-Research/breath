from breath_api_interface import request
from breath_api_interface.proxy import ServiceProxy
from breath_api_interface.queue import Queue
from breath_api_interface.service_interface import Service
from breath_api_interface.request import Request, Response

import sys

class ConsoleApplication(Service):
    def __init__(self, proxy:ServiceProxy, request_queue:Queue):
        '''ConsoleApplication constructor.
        '''
        super().__init__(proxy=proxy, request_queue=request_queue)
        self._configured = False


    def run(self) -> None:

        print("Escolha uma opção:")
        print("1 - Construir base de dados")
        
        opcao = 1

        if opcao == 1:
            request = Request(service_name="DataWorflow", operation_name="load_open_sus_data")
            response = self._proxy.send_request(request)

        if response.sucess:
            print("Operação realizada com sucesso!")
        else:
            print("Erro: ", response.response_data["message"])