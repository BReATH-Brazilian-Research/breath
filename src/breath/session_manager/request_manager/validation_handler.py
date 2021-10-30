from breath.api_interface.request import Request
from breath.session_manager.request_manager.request_handler import RequestHandler


class ValidationHandler(RequestHandler):
    def __init__(self):
        super().__init__()

    def handle(self, request:Request) -> None:
        '''Validates the request, looking for inconsistencies.

            TODO Implementar validação
        '''
        self._send_for_next(request)