from multiprocessing import Process
from typing import Union

from breath_api_interface import ProcessQueue, ServiceProxy
from breath_api_interface.service_interface import Service

from breath_data import BDAcessPoint, DataWorflow
from breath.console_application import ConsoleApplication

import multiprocessing

SERVICES = {"BDAcessPoint": BDAcessPoint, "DataWorflow" : DataWorflow, "ConsoleApplication": ConsoleApplication}

class ProcessServiceConstructor:
    def __init__(self):
        self._available_services : dict[str, type] = SERVICES
        self._manager = None 

    def register_available_service(self, service_name:str, service_class:type):
        self._available_services[service_name] = service_class

    def create_service(self, service_name: str, manager_queue: ProcessQueue) -> Union[ProcessQueue, None]:
        if service_name not in self._available_services:
            return None

        response_queue = ProcessQueue()
        request_queue = ProcessQueue()

        self._manager = ProcessQueue._manager
        
        proxy = ServiceProxy(manager_queue, response_queue)
        service : Service = self._available_services[service_name](proxy, request_queue)

        p = Process(target = service.run_forever)
        p.start()

        return request_queue

