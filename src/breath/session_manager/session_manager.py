from breath.api_interface.proxy import ServiceProxy
from breath.api_interface.queue import ProcessQueue
from breath.api_interface.request import Request
from breath.session_manager.request_manager.manager import RequestManager
from breath.session_manager.service_constructor import ProcessServiceConstructor


from breath.service_interface import Service

class ProcessSessionManager:
    def __init__(self):
        self._queue = ProcessQueue()

        self._service_constructor = ProcessServiceConstructor()
        self._request_manager = RequestManager(self._queue, self)

    def create_service(self, service_name:str) -> bool:
        request_queue = self._service_constructor.create_service(service_name, self._queue)

        if request_queue is None:
            return False

        self._request_manager.register_service(service_name, request_queue)

        return True

    def run(self):
        self._request_manager.process_request()