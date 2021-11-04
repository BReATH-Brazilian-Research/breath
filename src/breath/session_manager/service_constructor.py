from multiprocessing import Process
from typing import Union

from breath_api_interface import ProcessQueue, ServiceProxy
from breath.service_interface import Service


class ProcessServiceConstructor:
    def __init__(self):
        self._available_services : dict[str, type] = {}

    def register_available_service(self, service_name:str, service_class:type):
        self._available_services[service_name] = service_class

    def create_service(self, service_name: str, manager_queue: ProcessQueue) -> Union[ProcessQueue, None]:
        if service_name not in self._available_services:
            return None

        response_queue = ProcessQueue()
        request_queue = ProcessQueue()

        proxy = ServiceProxy(manager_queue, response_queue)
        service : Service = self._available_services[service_name](proxy, request_queue)

        Process(target = service.run_forever)

        return request_queue

